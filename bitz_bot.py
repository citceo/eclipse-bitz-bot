from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import subprocess
import psutil
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
RPC_URL = os.getenv("RPC_URL")

# Handle /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != CHAT_ID:
        return
    buttons = [
        [KeyboardButton("Start"), KeyboardButton("Bitz Collect")],
        [KeyboardButton("Bitz Claim"), KeyboardButton("Bitz Account")],
        [KeyboardButton("Check Screen"), KeyboardButton("Kill All Screens")],
        [KeyboardButton("Coming Soon"), KeyboardButton("RPC")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text(
        "Welcome to your Eclipse Mining Assistant! 🌌\n"
        "Select an option to manage your wallet and mining:\n"
        "Support: https://discord.gg/eclipse-fnd (#powpow)\n"
        "X: https://x.com/0xAsta2025",
        reply_markup=reply_markup
    )

# Run shell commands and capture output
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        return result.stdout or result.stderr or "Command executed."
    except subprocess.TimeoutExpired:
        return "Command timed out."
    except Exception as e:
        return f"Error: {str(e)}"

# Handle button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != CHAT_ID:
        return
    text = update.message.text

    if text == "Start":
        await update.message.reply_text("Bot is already running! Use the buttons to manage your mining.")

    elif text == "Bitz Collect":
        # Start mining in a new screen session
        output = run_command("screen -dmS eclipse bitz collect")
        await update.message.reply_text(f"Starting mining in screen session 'eclipse'...\nOutput: {output}")

    elif text == "Bitz Claim":
        # Claim BITZ tokens
        output = run_command("bitz claim")
        await update.message.reply_text(f"Claiming BITZ tokens...\nOutput: {output}")

    elif text == "Bitz Account":
        # Check wallet balance
        output = run_command("bitz account")
        await update.message.reply_text(f"Your wallet balance ({WALLET_ADDRESS}):\n{output}")

    elif text == "Check Screen":
        # List active screen sessions
        output = run_command("screen -ls")
        await update.message.reply_text(f"Active screen sessions:\n{output}")

    elif text == "Kill All Screens":
        # Terminate all screen sessions
        output = run_command("killall screen")
        await update.message.reply_text(f"Stopping all screen sessions...\nOutput: {output}")

    elif text == "Coming Soon":
        await update.message.reply_text("Coming soon... Stay tuned for updates!")

    elif text == "RPC":
        # Show current RPC and ask for new one
        output = run_command("solana config get")
        await update.message.reply_text(
            f"Current RPC: {RPC_URL}\n"
            f"Config: {output}\n"
            "Reply with a new RPC URL (e.g., https://mainnetbeta-rpc.eclipse.xyz) to update."
        )
        context.user_data["awaiting_rpc"] = True

# Handle text input (for RPC updates)
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != CHAT_ID:
        return
    if context.user_data.get("awaiting_rpc"):
        new_rpc = update.message.text.strip()
        # Update RPC with solana config
        output = run_command(f"solana config set --url {new_rpc}")
        # Update .env file
        try:
            with open(".env", "r") as f:
                lines = f.readlines()
            with open(".env", "w") as f:
                for line in lines:
                    if line.startswith("RPC_URL="):
                        f.write(f"RPC_URL={new_rpc}\n")
                    else:
                        f.write(line)
            global RPC_URL
            RPC_URL = new_rpc
            await update.message.reply_text(f"RPC updated to {new_rpc}\nOutput: {output}")
        except Exception as e:
            await update.message.reply_text(f"Failed to update .env: {str(e)}")
        context.user_data["awaiting_rpc"] = False
    else:
        await update.message.reply_text("Please select a button from the menu.")

# Main function to run the bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
