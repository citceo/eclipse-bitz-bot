# Eclipse Mining Telegram Bot

A user-friendly Telegram bot for managing BITZ mining on the Eclipse network. 🚀 Check your BITZ and ETH balance, start/stop mining, claim tokens, and switch RPC links—all from a simple menu. Messages auto-delete after 60 seconds for privacy. 🌌

## Features
- **Check Balance**: View your BITZ and ETH balance with a clean, formatted output.
- **Control Mining**: Start or stop mining with the `bitz collect` command.
- **Claim Tokens**: Claim BITZ tokens with a confirmation step.
- **Screen Management**: Check and terminate screen sessions for mining.
- **Switch RPC**: Easily update the RPC link for mining operations.
- **Coming Soon**: Placeholder for future features.
- **Auto-Delete Messages**: All bot messages disappear after 60 seconds.
- **Secure**: Uses environment variables to protect sensitive data.

## Prerequisites
To run this bot, you need a Linux-based system (like a VPS or Ubuntu) and the following:

1. **Python 3.8 or higher**: The programming language used to run the bot.
2. **Telegram Bot Token**: Get one from [BotFather](https://t.me/BotFather).
3. **Telegram Chat ID**: Your Telegram user ID for bot access.
4. **Eclipse Wallet Address**: Your wallet address for mining.
5. **Solana Keypair**: A keypair file (e.g., `id.json`) for wallet operations.
6. **bitz CLI Tool**: The command-line tool for BITZ mining (provided by Eclipse).
7. **screen Utility**: For running mining processes in the background.
8. **Internet Connection**: To interact with Telegram and the Eclipse network.

**Don't worry!** The steps below will guide you through installing everything, even if you're new to this.

## Step-by-Step Installation
Follow these instructions carefully. You can copy and paste each command into your terminal. The bot is designed to work on a Linux system (e.g., Ubuntu VPS). If you're using Windows or macOS, consider setting up a Linux VPS (like from AWS, Google Cloud, or DigitalOcean).

### Step 1: Set Up Your System
If you're using a fresh Ubuntu VPS, start by updating the system:

```bash
sudo apt-get update
sudo apt-get upgrade -y
