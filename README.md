# Eclipse Bitz Bot

Welcome to the **Eclipse Bitz Bot**! This is a Telegram bot that makes it easy to manage your Eclipse mining operations. With this bot, you can start or stop mining, claim your BITZ rewards, check your wallet balance, and more—all from your Telegram app. This guide is written step-by-step for beginners, so you can set up and use the bot even if you’re new to this.

## What This Bot Does

- **Start Mining**: Begin mining BITZ in a background session.
- **Claim BITZ**: Collect your earned BITZ rewards safely.
- **Check Balance**: See how much BITZ and ETH you have in your wallet.
- **Manage Sessions**: Control background processes to keep mining running smoothly.
- **Change Settings**: Update the network connection (RPC URL) if needed.
- **Stay Running**: The bot runs in the background, even if you close your terminal.
- **Safe and Secure**: Keeps your private information (like your bot token) safe in a special file.

## Before You Start

This guide assumes you’ve already set up the following:
- A Solana wallet with a keypair file at `~/.config/solana/id.json`.
- At least **0.0005 ETH** in your wallet to cover mining fees.
- The Bitz CLI tool installed and ready to use.
- A Telegram account and a bot token from [BotFather](https://t.me/BotFather).

If you haven’t done these yet, please contact our support team for help (see [Support](#support) below).

## Step-by-Step Installation

Follow these steps to set up the Eclipse Bitz Bot on your computer. Each step is explained clearly, and you can copy-paste the commands.

### Step 1: Download the Bot’s Code
1. Open your terminal (on Linux or macOS).
2. Type the following command to download the bot’s code from GitHub:
   ```bash
   git clone https://github.com/citceo/eclipse-bitz-bot.git
 ```
Move into the bot’s folder:
 ```bash

cd eclipse-bitz-bot
 ```
You’re now in the eclipse-bitz-bot folder, where the bot’s files are located.

Step 2: Set Up a Virtual Environment
To keep the bot’s files organized, we’ll use a Python virtual environment. This is like a separate space for the bot’s tools.
Create a virtual environment in the /root/bitz_env folder:
 ```bash

python3 -m venv /root/bitz_env
 ```
Activate the virtual environment:
 ```bash

source /root/bitz_env/bin/activate
 ```
Your terminal prompt should change to show (bitz_env). This means the virtual environment is active. All commands from now on should be run in this environment.

Step 3: Install the Bot’s Tools
The bot needs some Python tools to work. These are listed in a file called requirements.txt.
While the virtual environment is active, run:
 ```bash

pip install -r requirements.txt
 ```
Wait for the installation to finish. This might take a minute or two. You’ll see messages showing the tools being installed.

Step 4: Create a Configuration File
The bot needs some private information (like your Telegram bot token) to work. We’ll store this in a file called .env to keep it safe.
Create a new file called .env in the eclipse-bitz-bot folder. You can use a text editor like nano:
 ```bash

nano .env
 ```
Copy and paste the following lines into the file, replacing the placeholders with your own information:
 ```plaintext

BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
WALLET_ADDRESS=your_wallet_public_key
RPC_URL=https://mainnetbeta-rpc.eclipse.xyz
 ```
BOT_TOKEN: Get this from BotFather on Telegram after creating a bot.

CHAT_ID: Send a message to your bot, then check the bitz_bot.log file (created later) for the chat ID, or use a bot like @userinfobot.

WALLET_ADDRESS: Your Solana wallet’s public key (from your wallet setup).

RPC_URL: Use https://mainnetbeta-rpc.eclipse.xyz or another Eclipse RPC URL (e.g., https://eclipse.helius-rpc.com).

Save the file:
In nano, press Ctrl + O, then Enter to save, and Ctrl + X to exit.

Double-check that the .env file is in the eclipse-bitz-bot folder.

Step 5: Check Your Setup
Before running the bot, make sure:
Your Solana wallet file is at ~/.config/solana/id.json.

Your wallet has at least 0.0005 ETH (check with the bitz account command).

The virtual environment is active (you see (bitz_env) in your terminal).

If you’re unsure about any of these, contact our support team (see Support (#support)).
Running the Bot
To keep the bot running even if you close your terminal, we’ll run it in a screen session. This is like a background window that stays open.
Step 1: Start a Screen Session
Create a new screen session called eclipse_bot:
 ```bash

screen -S eclipse_bot
 ```
Your terminal will change to a new screen session.

Step 2: Activate the Virtual Environment
If the virtual environment isn’t active, activate it:
 ```bash

source /root/bitz_env/bin/activate
 ```
You should see (bitz_env) in your terminal prompt.

Step 3: Run the Bot
Start the bot by running:
 ```bash

python bot.py
 ```
The bot will connect to Telegram and start listening for your commands.

Step 4: Detach from the Screen
To leave the bot running in the background:
Press Ctrl + A, then D (one after the other).

You’ll see a message like [detached from ... eclipse_bot], and you’ll return to your normal terminal.

The bot is now running in the background!

Step 5: Check on the Bot Later
To go back and see what the bot is doing:
 ```bash

screen -r eclipse_bot
 ```
This will reopen the screen session, showing the bot’s activity.

Step 6: Stop the Bot (Optional)
If you want to stop the bot:
Reattach to the screen session: screen -r eclipse_bot.

Press Ctrl + C to stop the bot.

Exit the screen session by typing exit or pressing Ctrl + D.

To completely close the screen session:
 ```bash

screen -S eclipse_bot -X quit
 ```
Using the Bot
Now that the bot is running, you can control it from Telegram:
Start the Bot:
Open Telegram and find your bot (the one you created with BotFather).

Send the /start command.

A menu with buttons will appear.

What Each Button Does:
Start: Checks if mining is already running.

Bitz Collect: Starts mining in a background session called eclipse_bitz. Your wallet needs at least 0.0005 ETH.

Bitz Claim: Claims your mined BITZ rewards (you’ll confirm before it happens).

Bitz Account: Shows your wallet’s BITZ and ETH balances in a neat format.

Check Screen: Lists all background sessions (like eclipse_bitz or eclipse_bot).

Kill All Screens: Stops all background sessions (useful if something gets stuck).

Status: (Not ready yet, says “Coming soon”).

RPC: Lets you change the network connection by typing a new URL (e.g., https://mainnetbeta-rpc.eclipse.xyz).

Example:
Send /start, then click Bitz Collect to start mining.

Click Bitz Account to check your balance.

Use Bitz Claim to collect your rewards when ready

