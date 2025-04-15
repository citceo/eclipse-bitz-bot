# Eclipse BITZ Mining Telegram Bot

Welcome to the Eclipse BITZ Mining Telegram Bot! 🚀 This bot makes it super easy to manage your BITZ mining on the Eclipse network. With a clean menu, you can check your BITZ and ETH balance, start or stop mining, claim tokens, switch RPC links, and more—all from Telegram. Plus, all messages auto-delete after 60 seconds for privacy. 🌌

Whether you're a crypto newbie or a pro, this guide will walk you through every step to set up and run the bot, with commands you can copy and paste. Let's get started!

## What This Bot Does
- **Check Balance**: See your BITZ and ETH balance in a nicely formatted message.
- **Start/Stop Mining**: Launch or halt mining with the `bitz collect` command.
- **Claim Tokens**: Claim your BITZ tokens with a confirmation step to avoid mistakes.
- **Manage Screen Sessions**: Check or terminate background mining processes.
- **Switch RPC Links**: Update the RPC endpoint for mining with a simple text input.
- **Coming Soon**: A placeholder for exciting future features!
- **Privacy First**: All bot messages vanish after 60 seconds.
- **Secure Setup**: Uses environment variables to keep your sensitive info safe.

## Who Can Use This?
Anyone with a Linux system (like an Ubuntu VPS) and a Telegram account! No advanced coding skills needed—just follow the steps below, and you'll have your bot running in no time.

## Prerequisites
Before you begin, make sure you have:
1. **A Linux System**: Ubuntu 20.04 or later is ideal (e.g., a VPS from DigitalOcean, AWS, or Google Cloud). Windows/macOS users can set up a Linux VM or VPS.
2. **Internet Access**: To download files, interact with Telegram, and connect to the Eclipse network.
3. **A Telegram Account**: For creating and using the bot.
4. **An Eclipse Wallet**: You'll need a wallet address and keypair for mining.
5. **Basic Terminal Access**: You’ll use a terminal (like PuTTY for VPS or Terminal on Linux) to run commands.
6. **Time**: About 15–30 minutes to set everything up, depending on your system.

Don't worry if any of this sounds unfamiliar—the steps below explain everything in detail!

## Step-by-Step Setup Guide
Follow these steps exactly, copying and pasting commands into your terminal. We’ll assume you’re using a fresh Ubuntu 20.04 VPS, but the steps are similar for other Linux systems. If you hit any snags, check the **Troubleshooting** section at the end.

### Step 1: Log In to Your Linux System
1. Open your terminal:
   - **On a VPS**: Use PuTTY (Windows) or `ssh` (Linux/macOS). For example:

     ```bash
     ssh username@your-vps-ip
     ```

     Replace `username` and `your-vps-ip` with your VPS details (e.g., `ssh ubuntu@192.168.1.1`).
   - **On a local Linux machine**: Open the Terminal app (search for "Terminal" or press `Ctrl+Alt+T`).
2. If prompted, enter your password. You’re now in the terminal!

- **What this does**: Connects you to your Linux system where you’ll run all commands.
- **Time**: 1 minute.
- **Tip**: If you don’t have a VPS, sign up for one (e.g., DigitalOcean) or use a local Linux machine.

### Step 2: Update Your System
Keep your system up to date to avoid software issues:

```bash
sudo apt-get update
sudo apt-get upgrade -y
```


What to expect: The terminal will download package lists and install updates. It might take a few minutes.

What this does: Ensures your system has the latest security patches and software.

Time: 2–5 minutes, depending on your internet and system.

Tip: If asked for a password, use your VPS or user password. If it hangs, check your internet connection.

Step 3: Install Python
The bot needs Python 3.8 or higher to run. Check if it’s installed:

 ```bash

python3 --version
```
What to expect: If you see Python 3.8.x or higher (e.g., Python 3.10.12), skip to Step 4.

If not: If you get an error or a lower version, install Python:

 ```bash

sudo apt-get install python3 python3-pip python3-venv -y
```
Verify Python and its tools:

 ```bash

python3 --version
pip3 --version
```
Expected output:
Python 3.8.x or higher (e.g., Python 3.10.12).

pip 20.x.x or similar (e.g., pip 22.0.2).

What this does: Installs Python (the bot’s language), pip (for installing libraries), and venv (for isolating the bot’s setup).

Time: 1–3 minutes.

Tip: If you get errors, rerun sudo apt-get update.

Step 4: Install screen
The bot uses screen to run mining processes in the background, so they continue even if you close your terminal. Install it:
 ```bash

sudo apt-get install screen -y
```
Check it’s installed:
 ```bash

screen --version
```
Expected output: Something like Screen version 4.08.00.

What this does: Adds screen, a tool for managing long-running tasks like mining.

Time: Less than a minute.

Tip: If the install fails, check your internet or rerun the command.

Step 5: Install git
You need git to download the bot’s code from GitHub:
 ```bash

sudo apt-get install git -y
```
Verify it’s installed:
 ```bash

git --version
```
Expected output: Something like git version 2.34.1.

What this does: Installs git, which lets you clone the bot’s repository.

Time: Less than a minute.

Tip: If you get a "command not found" error, ensure sudo apt-get update ran successfully.

Step 6: Clone the Bot’s Repository
Download the bot’s code from GitHub:
 ```bash

git clone https://github.com/citceo/eclipse-bitz-bot.git
cd eclipse-bitz-bot
```
What to expect: This creates a folder called eclipse-bitz-bot with the bot’s files and moves you into it.

What this does: Copies the bot’s code to your system so you can set it up.

Time: 1–2 minutes, depending on your internet speed.

Tip: If you get a "repository not found" error:
Check the link matches your GitHub repo (e.g., https://github.com/citceo/eclipse-bitz-bot.git).

Ensure the repo is public (in GitHub settings).

If you used a different repo name, replace citceo/eclipse-bitz-bot with your own.

Step 7: Set Up a Virtual Environment
A virtual environment keeps the bot’s libraries separate to avoid conflicts with other programs:
 ```bash

python3 -m venv venv
source venv/bin/activate
```
What to expect: After the second command, your terminal prompt will show (venv), meaning the environment is active.

What this does:
Creates a venv folder for the bot’s libraries.

Activates the environment so commands like pip only affect the bot.

Time: Less than a minute.

Tip: If you close your terminal later, reactivate with:

 ```bash

source venv/bin/activate
```
Step 8: Install Python Libraries
Install the bot’s required libraries using the requirements.txt file:
 ```bash

pip install -r requirements.txt
```
This installs everything listed in requirements.txt:
plaintext

python-telegram-bot==20.7
psutil
requests
python-dotenv

If requirements.txt doesn’t work, install manually:
 ```bash

pip install python-telegram-bot==20.7
pip install "python-telegram-bot[job-queue]"
pip install psutil requests python-dotenv
```
Verify the libraries:
 ```bash

pip list
```
Expected output: You’ll see:
python-telegram-bot (version 20.7)

psutil

requests

python-dotenv

Plus some dependencies like httpx.

What this does:
python-telegram-bot: Runs the Telegram bot.

job-queue: Auto-deletes messages after 60 seconds.

psutil: Manages mining processes.

requests: Handles network tasks.

python-dotenv: Loads sensitive settings securely.

Time: 1–3 minutes.

Tip: If errors occur, update pip:

 ```bash

pip install --upgrade pip
```
Step 9: Install the bitz CLI Tool
The bot uses the bitz CLI to interact with the Eclipse network for mining and wallet tasks. Eclipse provides the bitz CLI, but you’ll need their official instructions to install it (check their website, GitHub, or Discord). Since I don’t have the exact steps, here’s a placeholder—you’ll need to replace it with the real commands:
Download the bitz CLI (example—find the correct link):

 ```bash

wget https://example.com/bitz-cli-latest-linux
```
Make it executable and move it to a system path:

 ```bash

chmod +x bitz-cli-latest-linux
sudo mv bitz-cli-latest-linux /usr/local/bin/bitz
```
Check it’s installed:

 ```bash

bitz --version
```
Expected output: Something like bitz version x.y.z (depends on the tool).

What this does: Installs bitz, which the bot uses to check balances, mine, and claim tokens.

Time: 2–5 minutes, depending on Eclipse’s instructions.

Important: To find the real bitz installation steps:
Visit Eclipse’s Discord: https://discord.gg/eclipse-fnd (#powpow).

Check their website or GitHub for CLI documentation.

Tip: If you can’t install bitz yet, proceed with setup and return to this step before mining. The bot will still run for other tasks.

Step 10: Create a Telegram Bot
You need a Telegram bot to interact with the code:
Open Telegram (on your phone or computer) and search for @BotFather.

Start BotFather:

 ```bash

/start
```
Create a new bot:

 ```bash

/newbot
```
Follow the prompts:
Name: Pick anything, like "Eclipse BITZ Bot".

Username: Must end in "Bot", like @MyEclipseBitzBot.

BotFather will give you a Bot Token, looking like:

1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890

Copy the token and save it somewhere safe (e.g., a text file or password manager).

What this does: Registers your bot with Telegram so it can send and receive messages.

Time: 2 minutes.

Tip: Don’t share the token—it’s like a password for your bot.

Step 11: Find Your Telegram Chat ID
The bot only responds to you (or a specific chat) for security. To get your Chat ID:
In Telegram, search for @userinfobot.

Start it:

 ```bash

/start
```
It will reply with your Chat ID, like:

123456789

Copy the Chat ID and save it.

What this does: Tells the bot who’s allowed to use it, keeping it private.

Time: 1 minute.

Tip: If you want the bot in a group, add it to the group and use /start@UserInfoBot to get the group’s Chat ID.

Step 12: Set Up Your Eclipse Wallet
You need an Eclipse wallet address and a keypair file for mining:
Wallet Address:
If you have the bitz CLI installed, check your wallet:

 ```bash

bitz account
```
This should show your address, like:

YourWalletAddress123...

Copy the address and save it.

If bitz isn’t installed yet, skip this and return after Step 9.

Solana Keypair:
The bot expects a keypair at ~/.config/solana/id.json. Create one:

 ```bash

mkdir -p ~/.config/solana
```
If bitz supports key generation:

 ```bash

bitz keygen --outfile ~/.config/solana/id.json
```
If not, use the Solana CLI to create a keypair:

 ```bash

sudo apt-get install curl -y
curl -sSfL https://release.solana.com/stable/install | sh
export PATH="$HOME/.local/share/solana/install/active_release/bin:$PATH"
solana-keygen new --outfile ~/.config/solana/id.json
```
When prompted, set a passphrase (or press Enter for none). Back up the passphrase or seed phrase securely.

Verify the keypair file:

 ```bash

ls -l ~/.config/solana/id.json
```
Critical: This file is your private key. Never share it, and back it up (e.g., on an encrypted USB drive).

What this does: Sets up your wallet so the bot can check balances, mine, and claim tokens.

Time: 2–5 minutes.

Tip: If bitz account fails, ensure bitz is installed and your wallet has some ETH (at least 0.005 for mining).

Step 13: Configure Environment Variables
The bot uses a .env file to store sensitive info like your bot token. Create it:
```bash

cp .env.example .env
nano .env
```
You’ll see the contents of .env.example:
plaintext

BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
WALLET_ADDRESS=your_wallet_address
RPC_URL=https://mainnetbeta-rpc.eclipse.xyz

Replace the placeholders with your values, for example:
plaintext

BOT_TOKEN=1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
CHAT_ID=123456789
WALLET_ADDRESS=YourWalletAddress123...
RPC_URL=https://mainnetbeta-rpc.eclipse.xyz

Save and exit:
Press Ctrl+O, then Enter to save.

Press Ctrl+X to exit.

Verify the file:
```bash

cat .env
```
What to expect: You’ll see your settings (don’t share this output!).

What this does: Stores your bot token, Chat ID, wallet address, and RPC link securely so the bot can use them.

Time: 2 minutes.

Tip: The default RPC_URL works for Eclipse, but you can change it later using the bot’s "RPC" button.

Step 14: Test the Bot
Let’s see if the bot works! Run it:
 ```bash

python3 bitz_bot.py
```
If the virtual environment isn’t active:

 ```bash

source venv/bin/activate
python3 bitz_bot.py
```
What to expect:
The terminal may show logs but shouldn’t crash.

Open Telegram, find your bot (e.g., @MyEclipseBitzBot), and send:

 ```bash

/start
```
You should see:

Welcome to your Eclipse Mining Assistant! 🌌
Select an option below to manage your wallet and mining:
Support: https://discord.gg/eclipse-fnd (#powpow)
X: https://x.com/0xAsta2025

A menu with these buttons:
Start

Bitz Collect

Bitz Claim

Bitz Account

Check Screen

Kill All Screens

Coming Soon

RPC

Test the buttons:
Coming Soon: Should say "Coming soon..." and delete after 60 seconds.

Bitz Account: Should show your wallet balance (if bitz and keypair are set up).

RPC: Should prompt for a new RPC link.

Start: Should check if mining is running.

All messages should disappear after 60 seconds.

What this does: Confirms the bot is working and responding to commands.

Time: 2–3 minutes.

Tip: If nothing happens, check the Troubleshooting section.

Step 15: Run the Bot in the Background
To keep the bot running 24/7 (e.g., on a VPS):
Start a screen session:

 ```bash

screen -S bot
```
Activate the virtual environment and run the bot:

 ```bash

source venv/bin/activate
python3 bitz_bot.py
```
Detach from the session to leave it running:

Press Ctrl+A, then D

What to expect: You’ll see [detached from 12345.bot] or similar, and the bot keeps running.

What this does: Lets the bot stay active even if you close your terminal.

To check on the bot later:

 ```bash

screen -r bot
```
To stop the bot:
Return to the session:

 ```bash

screen -r bot
```
Stop the bot:

 ```bash

Press Ctrl+C
```
Exit the session:

 ```bash

exit
```
What this does: Makes the bot reliable for long-term use, like mining.

Time: 1 minute.

Tip: If screen -r bot shows no session, restart with Step 15.1.

Troubleshooting
Hit a problem? Here’s how to fix common issues with commands you can copy and paste:
Bot doesn’t respond in Telegram:
Check the bot’s log for errors:

 ```bash

cat bitz_bot.log
```
Verify your .env file:

 ```bash

cat .env
```
Ensure BOT_TOKEN and CHAT_ID match what you got from BotFather and UserInfoBot.

Restart the bot:

 ```bash

source venv/bin/activate
python3 bitz_bot.py
```
Error: "command not found: bitz":
The bitz CLI isn’t installed. Revisit Step 9 and find Eclipse’s installation guide (website, GitHub, or Discord).

Test if bitz is available:

 ```bash

bitz --version
```
Messages don’t auto-delete:
Ensure the job-queue library is installed:

 ```bash

pip install "python-telegram-bot[job-queue]"
```
Restart the bot:

 ```bash

python3 bitz_bot.py
```
Mining fails with "Error: insufficient balance":
Your wallet needs at least 0.005 ETH. Check your balance:

 ```bash

bitz account --keypair ~/.config/solana/id.json --rpc https://mainnetbeta-rpc.eclipse.xyz
```
Fund your wallet via an Eclipse-compatible exchange or faucet (ask in Discord for faucets).

Keypair errors:
Verify the keypair file exists:

 ```bash

ls -l ~/.config/solana/id.json
```
If missing, recreate it (Step 12).

Fix permissions if needed:

 ```bash

chmod 600 ~/.config/solana/id.json
```
"Permission denied" errors:
Fix file ownership:

 ```bash

sudo chown $USER:$USER ~/.config/solana/id.json
```
Or run commands with sudo if appropriate.

Bot crashes with Python errors:
Ensure all libraries are installed:

 ```bash

pip install -r requirements.txt
```
Update pip:

 ```bash

pip install --upgrade pip
```
Still stuck?:
Share your issue in the Eclipse community:
Discord: https://discord.gg/eclipse-fnd (#powpow)

X: https://x.com/0xAsta2025

Check bitz_bot.log for clues:

 ```bash

cat bitz_bot.log
```
Security Tips
Keep your bot and wallet safe:
Never share .env or keypair: Your .env file and ~/.config/solana/id.json contain sensitive data. Don’t upload them to GitHub or share them.

Back up your keypair: Copy ~/.config/solana/id.json to a secure place (e.g., an encrypted USB):

 ```bash

cp ~/.config/solana/id.json ~/backup-id.json
```
Secure your VPS: Use strong passwords and enable a firewall:

 ```bash

sudo ufw enable
sudo ufw allow ssh
```
Update regularly: Keep your system secure:

 ```bash

sudo apt-get update
sudo apt-get upgrade -y
```
Monitor logs: Check for suspicious activity:

 ```bash

cat bitz_bot.log
```
Revoke bot token if leaked: If you think your token was exposed, use BotFather:

 ```bash

/revoke
```
  Then update .env with the new token.
Advanced Usage
Once the bot is running, here’s how to make the most of it:
Monitor Balance: Use Bitz Account to check your BITZ and ETH regularly.

Run Mining: Click Bitz Collect to start mining in a screen session. It’ll keep going even if you disconnect.

Claim Tokens: Use Bitz Claim to collect mined BITZ. Confirm carefully to avoid errors.

Change RPC: If the default RPC is slow, use RPC to enter a new link (e.g., a premium endpoint).

Manage Sessions: Use Check Screen to list running sessions and Kill All Screens to stop them if needed.

Stay Updated: Click Coming Soon to see if new features are added (it’s just a placeholder for now).

To check mining status manually:
 ```bash

screen -r eclipse_bitz
```
To stop a mining session:
 ```bash

screen -S eclipse_bitz -X quit
```
Contributing
Want to improve the bot? We’d love your help!
Report Bugs: Open an issue on GitHub with what went wrong.

Suggest Features: Share ideas via GitHub Issues.

Add Code: Fork the repo, make changes, and submit a pull request.

To contribute:
 ```bash

git clone https://github.com/citceo/eclipse-bitz-bot.git
cd eclipse-bitz-bot
# Edit files (e.g., bitz_bot.py)
git add .
git commit -m "Describe your changes here"
git push origin main
# Create a pull request on GitHub
```
License
This project is licensed under the MIT License. See the LICENSE file for details. You’re free to use, modify, and share the bot, as long as you follow the license terms.
Acknowledgments
Built with  for the Eclipse mining community.

Thanks to python-telegram-bot for making Telegram bots easy.

Props to the Eclipse network for powering BITZ mining.

Created by @0xAsta2025
.

Questions? Need Help?
Get support from the community:
Discord: https://discord.gg/eclipse-fnd (#powpow)

X: https://x.com/0xAsta2025

Happy mining, and enjoy your bot! 

