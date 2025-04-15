# Eclipse BITZ Mining Telegram Bot

Welcome to the Eclipse BITZ Mining Telegram Bot! 🚀 This bot lets you manage your BITZ mining on the Eclipse network right from Telegram. With a simple menu, you can check your BITZ and ETH balance, start or stop mining, claim tokens, switch RPC links, and more. All messages auto-delete after 60 seconds for privacy. 🌌

If you’ve already set up Rust, Solana CLI, `bitz` CLI, and your Eclipse wallet, this guide will help you get the bot running quickly. Just copy and paste the commands below, and you’ll be controlling your mining from Telegram in no time!

## What This Bot Does
- **Check Balance**: View your BITZ and ETH balance in a clear message.
- **Start/Stop Mining**: Run or halt mining with the `bitz collect` command.
- **Claim Tokens**: Claim your BITZ tokens with a confirmation step.
- **Manage Screen Sessions**: Check or stop background mining processes.
- **Switch RPC Links**: Update the RPC endpoint with a text input.
- **Coming Soon**: Placeholder for future features!
- **Privacy First**: Messages vanish after 60 seconds.
- **Secure Setup**: Uses environment variables to keep your info safe.

## Who Can Use This?
Anyone with a Linux system (like an Ubuntu VPS), a Telegram account, and the `bitz` CLI already installed. No coding skills needed—just follow the steps below.

## Prerequisites
This guide assumes you’ve already:
1. **Installed Rust**: Using `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` and sourced the environment.
2. **Installed Solana CLI**: Using `curl --proto '=https' --tlsv1.2 -sSfL https://solana-install.solana.workers.dev | bash`.
3. **Created an Eclipse Wallet**: With `solana-keygen new`, saved at `~/.config/solana/id.json`, and backed up your public key and mnemonic.
4. **Installed `bitz` CLI**: Using `cargo install bitz`.
5. **Set an RPC Endpoint**: Configured with `solana config set --url https://mainnetbeta-rpc.eclipse.xyz/` (or another Eclipse RPC).
6. **Funded Your Wallet**: Sent at least 0.005 ETH to your public key for mining.
7. **Tested Mining**: Ran `bitz collect` in a `screen` session and know how to detach/reattach.

You’ll also need:
- **A Linux System**: Ubuntu 20.04 or later (e.g., a VPS or local Linux machine).
- **Internet Access**: To download files and connect to Telegram.
- **A Telegram Account**: To create and use the bot.
- **Terminal Access**: To run commands (e.g., PuTTY for VPS or Terminal on Linux).
- **Time**: About 10–20 minutes to set up the bot.

If any of this sounds unfamiliar, double-check your setup or ask for help in the [Eclipse Discord](https://discord.gg/eclipse-fnd) (#powpow).

## Step-by-Step Setup Guide
Follow these steps, copying and pasting commands into your terminal. We assume you’re using an Ubuntu 20.04 VPS with `bitz` CLI already installed. If you hit issues, check the **Troubleshooting** section.

### Step 1: Log In to Your Linux System
1. Open your terminal:
   - **On a VPS**: Use PuTTY (Windows) or `ssh` (Linux/macOS):

```bash
ssh username@your-vps-ip
```
 Replace `username` and `your-vps-ip` with your VPS details (e.g., `ssh ubuntu@192.168.1.1`).


On a local Linux machine: Open Terminal (Ctrl+Alt+T).

Enter your password if prompted.

What this does: Gets you into your Linux system to run commands.

Time: Less than a minute.

### Step 2: Update Your System
Ensure your system is up to date:
```bash

sudo apt-get update
sudo apt-get upgrade -y
```
What to expect: Downloads and installs updates. May take a few minutes.

What this does: Keeps your system secure and compatible.

Time: 1–5 minutes.

Tip: If prompted, enter your password. If it hangs, check your internet.

### Step 3: Verify bitz CLI and Wallet
Confirm your bitz CLI and wallet are ready:
Check bitz CLI:

```bash

bitz --version
```
Expected output: Something like bitz version x.y.z.

If you get "command not found," reinstall bitz with:

```bash

cargo install bitz
```
Verify your keypair:

```bash

ls -l ~/.config/solana/id.json
```
Expected output: Shows the file exists (e.g., -rw------- 1 user user ... id.json).

If missing, recreate it (but back up any existing wallet first):

```bash

solana-keygen new --outfile ~/.config/solana/id.json
```
Check your wallet balance:

```bash

bitz account
```
Expected output: Shows your BITZ and ETH balance (e.g., 0.005 ETH).

If you have less than 0.005 ETH, send more to your public key via an exchange.

What this does: Ensures bitz CLI works and your wallet is funded.

Time: 1–3 minutes.

Tip: If bitz account fails, check your RPC:

```bash

solana config get
```
   Set it if needed:
```bash

solana config set --url https://mainnetbeta-rpc.eclipse.xyz/
```
### Step 4: Install Python
The bot needs Python 3.8 or higher. Check if it’s installed:
```bash

python3 --version
```
What to expect:
If you see Python 3.8.x or higher (e.g., Python 3.10.12), skip to Step 5.

If not, install Python:

```bash

sudo apt-get install python3 python3-pip python3-venv -y
```
Verify:
```bash

python3 --version
pip3 --version
```
Expected output:
Python 3.8.x or higher.

pip 20.x.x or similar.

What this does: Installs Python, pip (for libraries), and venv (for isolation).

Time: 1–3 minutes.

### Step 5: Install screen
If you’ve used screen for mining, it’s probably installed. Confirm:
```bash

screen --version
```
What to expect: Output like Screen version 4.08.00.

If not installed, add it:

```bash

sudo apt-get install screen -y
```
What this does: Allows the bot to manage mining sessions.

Time: Less than a minute.

### Step 6: Install git
You need git to download the bot’s code:
```bash

sudo apt-get install git -y
```
Verify:
```bash

git --version
```
Expected output: Something like git version 2.34.1.

What this does: Installs git for cloning the repository.

Time: Less than a minute.

### Step 7: Clone the Bot’s Repository
Download the bot’s code:
```bash

git clone https://github.com/citceo/eclipse-bitz-bot.git
cd eclipse-bitz-bot
```
What to expect: Creates a folder eclipse-bitz-bot and moves you into it.

What this does: Gets the bot’s files onto your system.

Time: 1–2 minutes.

Tip: If the clone fails, check the repo URL (https://github.com/citceo/eclipse-bitz-bot.git) or your internet.

### Step 8: Set Up a Virtual Environment
Create a virtual environment to keep the bot’s libraries separate:
```bash

python3 -m venv venv
source venv/bin/activate
```
What to expect: Your prompt shows (venv) after activation.

What this does: Isolates the bot’s dependencies.

Time: Less than a minute.

Tip: Reactivate later with:

```bash

source venv/bin/activate
```
### Step 9: Install Python Libraries
Install the bot’s required libraries:
```bash

pip install -r requirements.txt
```
If that doesn’t work, install manually:
```bash

pip install python-telegram-bot==20.7
pip install "python-telegram-bot[job-queue]"
pip install psutil requests python-dotenv
```
Verify:
```bash

pip list
```
Expected output:
python-telegram-bot (version 20.7)

psutil

requests

python-dotenv

What this does:
python-telegram-bot: Runs the bot.

job-queue: Deletes messages after 60 seconds.

psutil: Manages processes.

requests: Handles network calls.

python-dotenv: Loads secure settings.

Time: 1–3 minutes.

Tip: Update pip if errors occur:

```bash

pip install --upgrade pip
```
### Step 10: Create a Telegram Bot
Set up a Telegram bot for the code:
Open Telegram and search for @BotFather.

Send:

```bash

/start
```
Create a bot:

```bash

/newbot
```
Follow prompts:
Name: Anything (e.g., "Eclipse BITZ Bot").

Username: Must end in "Bot" (e.g., @MyEclipseBitzBot).

Copy the Bot Token (e.g., 1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890) and save it.

What this does: Registers your bot with Telegram.

Time: 2 minutes.

Tip: Keep the token private.

### Step 11: Find Your Telegram Chat ID
The bot only responds to you for security:
In Telegram, search for @userinfobot.

Send:

```bash

/start
```
Copy the Chat ID (e.g., 123456789) from the reply.

What this does: Restricts bot access to you.

Time: 1 minute.

Tip: For group chats, add the bot to the group and use /start@getidsbot.

### Step 12: Configure Environment Variables
Set up the bot’s settings:
Copy the example file:

```bash

cp .env.example .env
```
Edit it:

```bash

nano .env
```
Replace placeholders with your values, like:

```plaintext

BOT_TOKEN=1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
CHAT_ID=123456789
WALLET_ADDRESS=YourWalletAddress123...
RPC_URL=https://mainnetbeta-rpc.eclipse.xyz
```
Use your wallet’s public key from bitz account.

Keep the RPC URL from your solana config get output.

Save and exit:
Ctrl+O, Enter to save.

Ctrl+X to exit.

Verify:

```bash

cat .env
```
What this does: Stores your bot token, chat ID, wallet address, and RPC securely.

Time: 2 minutes.

Tip: Ensure no typos in .env.

### Step 13: Test the Bot
Run the bot to check it works:
```bash

python3 bitz_bot.py
```
If the virtual environment isn’t active:

```bash

source venv/bin/activate
python3 bitz_bot.py
```
What to expect:
Terminal shows logs (no errors).

In Telegram, send /start to your bot (e.g., @MyEclipseBitzBot):
```
Welcome to your Eclipse Mining Assistant! 🌌
Select an option below to manage your wallet and mining:
Support: https://discord.gg/eclipse-fnd (#powpow)
X: https://x.com/0xAsta2025
```
Menu buttons:
Start

Bitz Collect

Bitz Claim

Bitz Account

Check Screen

Kill All Screens

Coming Soon

RPC

Test buttons:
Coming Soon: Shows "Coming soon..." and deletes after 60 seconds.

Bitz Account: Displays your wallet balance.

Bitz Collect: Starts mining in a screen session.

RPC: Lets you update the RPC link.

What this does: Confirms the bot is working.

Time: 2–3 minutes.

Step 14: Run the Bot in the Background
Keep the bot running 24/7:
Start a screen session:

```bash

screen -S bot
```
Run the bot:

```bash

source venv/bin/activate
python3 bitz_bot.py
```
Detach (leave it running):
```
Press Ctrl+A, then D
```
What to expect: Shows [detached from 12345.bot].

Reattach later:

```bash

screen -r bot
```
Stop the bot:
Reattach:

```bash

screen -r bot
```
Stop:
```
Press Ctrl+C
```
Exit:

```bash

exit
```
What this does: Keeps the bot online for continuous use.

Time: 1 minute.

Troubleshooting
Fix common issues with these commands:
Bot doesn’t respond:
Check logs:

```bash

cat bitz_bot.log
```
Verify .env:

```bash

cat .env
```
Ensure BOT_TOKEN and CHAT_ID are correct.

Restart:

```bash

python3 bitz_bot.py
```
"command not found: bitz":
Reinstall bitz:

```bash

cargo install bitz
```
Verify:

```bash

bitz --version
```
Messages don’t auto-delete:
Install job-queue:

```bash

pip install "python-telegram-bot[job-queue]"
```
Restart:

```bash

python3 bitz_bot.py
```
Mining doesn’t start:
Check balance (needs 0.005 ETH):

```bash

bitz account
```
Verify keypair:

```bash

ls -l ~/.config/solana/id.json
```
Check RPC:

```bash

solana config get
```
Set if needed:

```bash

solana config set --url https://mainnetbeta-rpc.eclipse.xyz/
```
Python errors:
Reinstall libraries:

```bash

pip install -r requirements.txt
```
Update pip:

```bash

pip install --upgrade pip
```
Need help?:
Eclipse Discord: https://discord.gg/eclipse-fnd (#powpow)

X: https://x.com/0xAsta2025

Security Tips
Protect .env: Never share it or upload it to GitHub.

Back up keypair: Copy ~/.config/solana/id.json to a secure place:

```bash

cp ~/.config/solana/id.json ~/backup-id.json
```
Secure your VPS: Update regularly:

```bash

sudo apt-get update
sudo apt-get upgrade -y
```
Monitor logs: Check for issues:

```bash

cat bitz_bot.log
```
Revoke token if leaked: Use @BotFather’s /revoke, then update .env.

Advanced Usage
Check Balance: Use Bitz Account often.

Mining: Bitz Collect runs mining in a screen session.

Claim Tokens: Bitz Claim to collect BITZ.

RPC Switch: Update with RPC if the default is slow.

Sessions: Use Check Screen and Kill All Screens to manage mining.

Manual mining commands (outside the bot):
```bash

screen -S eclipse
bitz collect
# Detach: Ctrl+A, D
# Reattach: screen -r eclipse
```
Contributing
Improve the bot by:
Reporting bugs on GitHub Issues.

Suggesting features via Issues.

Submitting code:

```bash

git clone https://github.com/citceo/eclipse-bitz-bot.git
cd eclipse-bitz-bot
# Edit files
git add .
git commit -m "Your changes"
git push origin main
# Create a pull request
```
License
MIT License. See LICENSE for details.
Acknowledgments
Built for the Eclipse mining community. 

Thanks to python-telegram-bot and Eclipse.

By @0xAsta2025
.

Questions?
Discord: https://discord.gg/eclipse-fnd (#powpow)

X: https://x.com/0xAsta2025

Happy mining! 

