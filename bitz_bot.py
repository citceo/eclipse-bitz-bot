import telegram
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
import subprocess
import psutil
import time
import logging
import re
import json
import asyncio
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configuration (loaded from .env)
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
RPC_URL = os.getenv("RPC_URL", "https://mainnetbeta-rpc.eclipse.xyz")

# Setup logging
logging.basicConfig(
    filename='bitz_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to check running processes
def check_process(process_name):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if process_name in ' '.join(proc.info['cmdline'] if proc.info['cmdline'] else []):
                return proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None

# Function to kill a process
def kill_process(pid):
    if not pid:
        return False
    logging.info(f"Attempting to kill process with PID: {pid}")
    try:
        process = psutil.Process(pid)
        process.terminate()
        time.sleep(3)
        if process.is_running():
            process.kill()
        logging.info(f"Process {pid} killed successfully")
        return True
    except (psutil.NoSuchProcess, OSError) as e:
        logging.error(f"Failed to kill process {pid}: {str(e)}")
        return False

# Function to kill all screen sessions
def kill_all_screens():
    try:
        result = subprocess.run(
            "screen -ls | grep Detached | awk '{print $1}' | xargs -I {} screen -S {} -X quit",
            shell=True,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return "All screen sessions closed successfully."
        return f"Error closing screens: {result.stderr}"
    except Exception as e:
        logging.error(f"Error killing screens: {str(e)}")
        return f"Error: {str(e)}"

# Function to run commands
def run_command(command, max_runtime=600, wait_for_output=True, input_data=None):
    logging.info(f"Executing command: {command}")
    logging.info(f"Input data: {input_data}")
    try:
        if not wait_for_output:
            subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            logging.info("Process started without waiting for output")
            return "Process started."
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE if input_data else None,
            text=True
        )
        start_time = time.time()
        stdout, stderr = process.communicate(input=input_data, timeout=max_runtime)
        # Remove ANSI escape codes
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        stdout = ansi_escape.sub('', stdout)
        logging.info(f"STDOUT: {stdout}")
        if stderr:
            logging.warning(f"STDERR: {stderr}")
        if process.returncode == 0:
            return stdout.strip() or "Process executed successfully."
        logging.error(f"Command failed: {stderr}")
        return f"Error: {stderr}"
    except subprocess.TimeoutExpired:
        process.kill()
        logging.error(f"Command timed out: {command}")
        return f"Error: Command timed out after {max_runtime} seconds."
    except Exception as e:
        logging.error(f"Exception in run_command: {str(e)}")
        return f"Error: {str(e)}"

# Function to check ETH balance
def check_eth_balance():
    command = f"bitz account --keypair ~/.config/solana/id.json --rpc {RPC_URL}"
    output = run_command(command, max_runtime=60)
    try:
        match = re.search(r'(\d+\.\d+)\s*ETH', output)
        if match:
            balance = float(match.group(1))
            if balance < 0.005:
                return False, f"Your ETH balance ({balance}) is less than 0.005. Please top up your wallet."
            return True, f"Sufficient balance: {balance} ETH"
        return False, f"Unable to check balance. Output: {output}"
    except Exception as e:
        logging.error(f"Error parsing balance: {str(e)}")
        return False, f"Error checking balance: {output}"

# Function to start mining in a screen session
def start_bitz_collect():
    session_name = "eclipse_bitz"
    command = (
        f"screen -dmS {session_name} bitz collect --keypair ~/.config/solana/id.json "
        f"--rpc {RPC_URL} --verbose"
    )
    try:
        subprocess.run(command, shell=True, check=True)
        return f"Mining started in screen session '{session_name}'. Check it with: `screen -r {session_name}`"
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to start bitz collect: {str(e)}")
        return f"Error starting mining: {str(e)}"

# Improved function to format bitz account output
def format_bitz_account_output(output):
    lines = output.split('\n')
    account_info = {}
    proof_info = {}
    current_section = None

    for line in lines:
        line = line.strip()
        if 'Account' in line:
            current_section = 'account'
        elif 'Proof' in line:
            current_section = 'proof'
        elif line and current_section:
            parts = line.split(None, 1)
            if len(parts) == 2:
                key, value = parts
                key = key.strip()
                value = value.strip()
                if current_section == 'account':
                    account_info[key] = value
                elif current_section == 'proof':
                    proof_info[key] = value

    # Formatted output
    formatted_output = (
        "📊 **Account Information** 📊\n"
        f"🔑 **Address**: `{account_info.get('Address', 'Unknown')}`\n"
        f"💰 **BITZ Balance**: {account_info.get('Balance', 'Unknown')} BITZ\n"
        f"🪙 **ETH Balance**: {account_info.get('ETH', 'Unknown')} ETH\n\n"
        "📈 **Proof of Work Details** 📈\n"
        f"💸 **Proof Balance**: {proof_info.get('Balance', 'Unknown')} BITZ\n"
        f"⚙️ **Lifetime Hashes**: {proof_info.get('Lifetime hashes', 'Unknown')}\n"
        f"🏆 **Lifetime Rewards**: {proof_info.get('Lifetime rewards', 'Unknown')} BITZ"
    )
    return formatted_output

# Function to delete messages automatically
async def delete_message_later(context, chat_id, message_id, delay=60):
    await asyncio.sleep(delay)
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        logging.warning(f"Failed to delete message {message_id}: {str(e)}")

# Handler for text messages (for receiving RPC link)
async def handle_text(update, context):
    if str(update.message.chat_id) != CHAT_ID:
        msg = await update.message.reply_text("Unauthorized access!")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )
        return
    if context.user_data.get("awaiting_rpc"):
        global RPC_URL
        new_rpc = update.message.text.strip()
        # Simple link validation
        if not new_rpc.startswith("http"):
            msg = await update.message.reply_text("Please enter a valid link (starting with http or https).")
            context.job_queue.run_once(
                delete_message_later,
                60,
                data={"chat_id": CHAT_ID, "message_id": msg.message_id}
            )
            return
        RPC_URL = new_rpc
        context.user_data["awaiting_rpc"] = False
        msg = await update.message.reply_text(f"RPC link successfully changed to {RPC_URL}.")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )
    else:
        msg = await update.message.reply_text("Please use the buttons.")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

# Handler for buttons
async def button_handler(update, context):
    global RPC_URL
    query = update.callback_query
    if str(query.message.chat_id) != CHAT_ID:
        msg = await query.message.reply_text("Unauthorized access!")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )
        return
    await query.answer()

    # Auto-delete button message
    if query.message:
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": query.message.chat_id, "message_id": query.message.message_id}
        )

    if query.data == "start":
        welcome_message = (
            "Welcome to the Eclipse Mining Bot! 🚀\n"
            "Checking mining process status..."
        )
        msg = await context.bot.send_message(chat_id=CHAT_ID, text=welcome_message)
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

        collect_pid = check_process("bitz collect")
        if collect_pid:
            msg = await context.bot.send_message(chat_id=CHAT_ID, text="Mining process is already running.")
        else:
            msg = await context.bot.send_message(chat_id=CHAT_ID, text="No mining process running. Start it with 'Bitz Collect'.")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

    elif query.data == "bitz_collect":
        has_enough_eth, balance_output = check_eth_balance()
        if not has_enough_eth:
            msg = await context.bot.send_message(chat_id=CHAT_ID, text=balance_output)
        else:
            collect_pid = check_process("bitz collect")
            if collect_pid:
                if not kill_process(collect_pid):
                    msg = await context.bot.send_message(chat_id=CHAT_ID, text="Error stopping previous process. Try again later.")
                    context.job_queue.run_once(
                        delete_message_later,
                        60,
                        data={"chat_id": CHAT_ID, "message_id": msg.message_id}
                    )
                    return
            output = kill_all_screens()
            if "Error" in output:
                msg = await context.bot.send_message(chat_id=CHAT_ID, text=output)
            else:
                output = start_bitz_collect()
                msg = await context.bot.send_message(chat_id=CHAT_ID, text=output)
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

    elif query.data == "bitz_claim":
        keyboard = [
            [
                telegram.InlineKeyboardButton("Confirm", callback_data="confirm_claim"),
                telegram.InlineKeyboardButton("Cancel", callback_data="cancel_claim")
            ]
        ]
        reply_markup = telegram.InlineKeyboardMarkup(keyboard)
        msg = await context.bot.send_message(
            chat_id=CHAT_ID,
            text="Are you sure you want to claim BITZ?",
            reply_markup=reply_markup
        )
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

    elif query.data == "confirm_claim":
        command = f"bitz claim --keypair ~/.config/solana/id.json --rpc {RPC_URL}"
        output = run_command(command, max_runtime=60, input_data="y\n")
        if "y/n only please" in output:
            output = run_command(command, max_runtime=60, input_data="Y\n")
        msg = await context.bot.send_message(chat_id=CHAT_ID, text=f"Bitz Claim Results:\n{output}")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

    elif query.data == "cancel_claim":
        msg = await context.bot.send_message(chat_id=CHAT_ID, text="BITZ claim canceled.")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

    elif query.data == "bitz_account":
        command = f"bitz account --keypair ~/.config/solana/id.json --rpc {RPC_URL}"
        output = run_command(command, max_runtime=300)
        if output.startswith("Error"):
            msg = await context.bot.send_message(chat_id=CHAT_ID, text=output)
        else:
            formatted_output = format_bitz_account_output(output)
            msg = await context.bot.send_message(chat_id=CHAT_ID, text=formatted_output, parse_mode="Markdown")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

    elif query.data == "check_screen":
        output = run_command("screen -ls", max_runtime=30)
        msg = await context.bot.send_message(chat_id=CHAT_ID, text=f"Screen status:\n{output}")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

    elif query.data == "kill_screens":
        output = kill_all_screens()
        msg = await context.bot.send_message(chat_id=CHAT_ID, text=output)
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

    elif query.data == "coming_soon":
        msg = await context.bot.send_message(chat_id=CHAT_ID, text="Coming soon...")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

    elif query.data == "rpc":
        context.user_data["awaiting_rpc"] = True
        msg = await context.bot.send_message(
            chat_id=CHAT_ID,
            text=f"Current RPC link: {RPC_URL}\nPlease enter the new RPC link (e.g., https://mainnetbeta-rpc.eclipse.xyz):"
        )
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )

# Function to send the button menu
async def start_command(update, context):
    if str(update.message.chat_id) != CHAT_ID:
        msg = await update.message.reply_text("Unauthorized access!")
        context.job_queue.run_once(
            delete_message_later,
            60,
            data={"chat_id": CHAT_ID, "message_id": msg.message_id}
        )
        return
    keyboard = [
        [
            telegram.InlineKeyboardButton("Start", callback_data="start"),
            telegram.InlineKeyboardButton("Bitz Collect", callback_data="bitz_collect")
        ],
        [
            telegram.InlineKeyboardButton("Bitz Claim", callback_data="bitz_claim"),
            telegram.InlineKeyboardButton("Bitz Account", callback_data="bitz_account")
        ],
        [
            telegram.InlineKeyboardButton("Check Screen", callback_data="check_screen"),
            telegram.InlineKeyboardButton("Kill All Screens", callback_data="kill_screens")
        ],
        [
            telegram.InlineKeyboardButton("Coming Soon", callback_data="coming_soon"),
            telegram.InlineKeyboardButton("RPC", callback_data="rpc")
        ]
    ]
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    msg = await context.bot.send_message(
        chat_id=CHAT_ID,
        text=(
            "Welcome to your Eclipse Mining Assistant! 🌌\n"
            "Select an option below to manage your wallet and mining:\n"
            "Support: https://discord.gg/eclipse-fnd (#powpow)\n"
            "X: https://x.com/0xAsta2025"
        ),
        reply_markup=reply_markup
    )
    context.job_queue.run_once(
        delete_message_later,
        60,
        data={"chat_id": CHAT_ID, "message_id": msg.message_id}
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.run_polling(allowed_updates=['message', 'callback_query'])

if __name__ == '__main__':
    main()
