# Eclipse Mining Bot

The **Eclipse Mining Bot** is a Telegram-based bot designed to simplify and automate mining operations on the Eclipse network. It allows users to manage mining processes, claim BITZ rewards, check wallet balances, and control screen sessions directly from Telegram. This bot is built to work with the Bitz CLI and Solana keypair, providing a user-friendly interface for miners.

## Features

- **Start/Stop Mining**: Initiate or terminate mining processes in a screen session.
- **Claim BITZ**: Claim your mined BITZ rewards with confirmation prompts.
- **Check Balances**: View your wallet's BITZ and ETH balances, along with proof-of-work details.
- **Screen Management**: Check and terminate active screen sessions.
- **RPC Configuration**: Dynamically change the RPC URL for Bitz CLI commands.
- **Logging**: Detailed logs saved to `bitz_bot.log` for debugging and monitoring.
- **Secure Configuration**: Sensitive data stored in a `.env` file to prevent exposure.

Installation
Follow these steps to set up the Eclipse Mining Bot on your system.
1. Clone the Repository
bash

git clone https://github.com/your-username/eclipse-mining-bot.git
cd eclipse-mining-bot

2. Install Python Dependencies
The bot requires Python 3.8+ and specific libraries. Install them using:
bash

pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file in the project root directory to store sensitive information:
plaintext

BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
WALLET_ADDRESS=your_wallet_public_key
RPC_URL=https://mainnetbeta-rpc.eclipse.xyz

BOT_TOKEN: Obtain from BotFather on Telegram.

CHAT_ID: Find by messaging your bot and checking the logs (bitz_bot.log) or using a bot like @userinfobot.

WALLET_ADDRESS: Your Solana wallet's public key (from solana-keygen new).

RPC_URL: One of the Eclipse RPC URLs (e.g., https://mainnetbeta-rpc.eclipse.xyz).

4. Verify Setup
Ensure the following:
The Solana keypair exists at ~/.config/solana/id.json.

Your wallet has at least 0.005 ETH.

The Bitz CLI is installed and accessible via the bitz command.

Running the Bot
To ensure the bot continues running even after closing the terminal, execute it in a screen session.
1. Start a Screen Session
bash

screen -S eclipse_bot

2. Run the Bot
bash

python bot.py

3. Detach from Screen
To keep the bot running in the background, detach from the screen session:
Press Ctrl + A, then D.

4. Reattach to Screen
To check on the bot or stop it:
bash

screen -r eclipse_bot

To stop the bot, press Ctrl + C in the screen session.

5. Stop the Screen Session
If you want to terminate the screen session completely:
bash

screen -S eclipse_bot -X quit

Using the Bot
Once the bot is running, interact with it via Telegram:
Send the /start command to your bot.

Use the provided buttons to perform actions:
Start: Check the status of the mining process.

Bitz Collect: Start mining in a screen session (eclipse_bitz).

Bitz Claim: Claim your BITZ rewards (with confirmation).

Bitz Account: Display your wallet's BITZ and ETH balances, plus proof-of-work details.

Check Screen: List active screen sessions.

Kill All Screens: Terminate all detached screen sessions.

Status: (Under development)

RPC: Change the RPC URL by entering a new link.

Troubleshooting
Bot Doesn't Respond:
Check bitz_bot.log for errors.

Verify BOT_TOKEN and CHAT_ID in the .env file.

Ensure the bot is running in the eclipse_bot screen session (screen -r eclipse_bot).

Mining Fails:
Confirm your wallet has at least 0.005 ETH (bitz account).

Check the RPC URL (RPC_URL in .env or via the bot's RPC button).

Ensure the Solana keypair exists at ~/.config/solana/id.json.

Screen Issues:
List all screen sessions: screen -ls.

Terminate stuck sessions: screen -S session_name -X quit.

Command Timeouts:
Increase the max_runtime value in the run_command function in bot.py if commands take too long.

Security Notes
Never share your .env file or Solana keypair (id.json). These contain sensitive information.

Backup your mnemonic phrase in a secure location.

Use a strong passphrase for your Solana wallet.

The .gitignore file ensures sensitive files (.env, logs, JSON files) are not uploaded to GitHub.

Contributing
Contributions are welcome! To contribute:
Fork the repository.

Create a new branch (git checkout -b feature/your-feature).

Make changes and commit (git commit -m "Add your feature").

Push to your fork (git push origin feature/your-feature).

Open a pull request.

Support
For help or questions:
Discord: https://discord.gg/eclipse-fnd (#powpow channel)

X: https://x.com/EclipseFND

License
This project is licensed under the MIT License. See the LICENSE file for details.

