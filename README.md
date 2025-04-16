# Eclipse Mining Bot

The **Eclipse Mining Bot** is a robust Telegram-based bot designed to simplify and automate mining operations on the Eclipse network. It offers a user-friendly interface for managing mining processes, claiming BITZ rewards, monitoring wallet balances, and controlling screen sessions, all from within Telegram. Integrated with the Bitz CLI and Solana keypair, this bot is tailored for miners looking to optimize their workflow with minimal effort.

## Features

- **Automated Mining**: Start and stop mining in a dedicated screen session with a single command.
- **BITZ Claiming**: Securely claim mined BITZ rewards with a confirmation prompt to avoid errors.
- **Balance Monitoring**: View formatted BITZ and ETH balances, along with proof-of-work details.
- **Screen Management**: Check and terminate active screen sessions for mining or bot processes.
- **Dynamic RPC Configuration**: Update the RPC URL for Bitz CLI commands directly via Telegram.
- **Comprehensive Logging**: All actions are logged to `bitz_bot.log` for easy debugging and monitoring.
- **Secure Configuration**: Sensitive data (bot token, chat ID, wallet address) stored in a `.env` file.
- **Isolated Execution**: Runs in a Python virtual environment to prevent dependency conflicts.
- **Persistent Operation**: Executes in a screen session to remain active after terminal closure.

## Prerequisites

This guide assumes you have already completed the following setup steps, which are required for Eclipse mining and Bitz CLI operations:

1. **Rust Installed**:
   - Installed using:
     ```bash
     curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
     source $HOME/.cargo/env
     ```

2. **Solana CLI Installed**:
   - Installed using:
     ```bash
     curl --proto '=https' --tlsv1.2 -sSfL https://solana-install.solana.workers.dev | bash
     ```

3. **Solana Wallet Created**:
   - A keypair generated with:
     ```bash
     solana-keygen new
     ```
   - Your public key and mnemonic phrase are saved securely.
   - The keypair is stored at `~/.config/solana/id.json`.

4. **Bitz CLI Installed**:
   - Installed using:
     ```bash
     cargo install bitz
     ```

5. **RPC URL Configured**:
   - Set to one of the following Eclipse RPC endpoints:
     ```bash
     solana config set --url https://mainnetbeta-rpc.eclipse.xyz/
     ```
     or
     ```bash
     solana config set --url https://eclipse.helius-rpc.com/
     ```
     or
     ```bash
     solana config set --url https://bitz-000.eclipserpc.xyz/
     ```

6. **Wallet Funded**:
   - At least **0.0005 ETH** sent to your wallet’s public key to cover mining transaction fees.
   - Verified using:
     ```bash
     bitz account
     ```

7. **Bitz CLI Tested**:
   - Familiarity with commands like:
     - Start mining:
       ```bash
       screen -S eclipse
       bitz collect
       ```
       Detach with `Ctrl + A + D`, reattach with `screen -r eclipse`.
     - Claim BITZ:
       ```bash
       bitz claim
       ```
     - Check balance:
       ```bash
       bitz account
       ```
     - Configure CPU cores (e.g., 8 cores):
       ```bash
       bitz collect --cores 8
       ```
     - Check hashpower:
       ```bash
       bitz benchmark
       ```
     - View all commands:
       ```bash
       bitz -h
       ```

If any of these steps are incomplete, please complete them before proceeding.

## Installation

Follow these steps to install and configure the Eclipse Mining Bot. These instructions start with setting up the bot itself, assuming the prerequisites above are met.

### 1. Clone the Repository
Download the bot’s source code from GitHub:
```bash
git clone https://github.com/citceo/eclipse-bitz-bot
cd eclipse-mining-bot
```
### 2. Set Up a Python Virtual Environment
To isolate dependencies and avoid conflicts, create a Python virtual environment:
```bash

python3 -m venv /root/bitz_env
```
Activate the virtual environment:
```bash

source /root/bitz_env/bin/activate
```
Your terminal prompt should change to indicate the virtual environment (e.g., (bitz_env)).

All subsequent commands in this section should be run within the virtual environment.

### 3. Install Python Dependencies
Install the required Python libraries specified in requirements.txt:
```bash

pip install -r requirements.txt
```
This installs:
python-telegram-bot: For Telegram bot functionality.

psutil: For process management.

python-dotenv: For loading environment variables from .env.

### 4. Configure Environment Variables
Create a .env file in the project root (eclipse-mining-bot/) to store sensitive information:
```plaintext

BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
WALLET_ADDRESS=your_wallet_public_key
RPC_URL=https://mainnetbeta-rpc.eclipse.xyz
```
BOT_TOKEN: Obtain from BotFather by creating a new bot.

CHAT_ID: Find by sending a message to your bot and checking bitz_bot.log for the chat ID, or use a bot like @userinfobot.

WALLET_ADDRESS: Your Solana wallet’s public key (from solana-keygen new).

RPC_URL: One of the Eclipse RPC URLs (e.g., https://mainnetbeta-rpc.eclipse.xyz).

### 5. Verify Setup
Before running the bot, confirm:
The Solana keypair exists at ~/.config/solana/id.json.

Your wallet has at least 0.0005 ETH (check with bitz account).

The Bitz CLI is installed and accessible (bitz -h should display help).

The virtual environment is active (source /root/bitz_env/bin/activate).

The .env file is correctly configured with no typos.

Running the Bot
To ensure the bot remains active after closing the terminal, run it in a Screen session within the Python virtual environment.
1. Activate the Virtual Environment
If not already active, activate the virtual environment:
```bash

source /root/bitz_env/bin/activate
```
2. Start a Screen Session
Create a new Screen session named eclipse_bot:
```bash

screen -S eclipse_bot
```
3. Run the Bot
Execute the bot script:
bash
```
python bot.py
```
The bot will initialize, connect to Telegram, and wait for commands.
4. Detach from Screen
To keep the bot running in the background, detach from the Screen session:
Press Ctrl + A, then D.

You’ll return to your terminal, and the bot will continue running in the eclipse_bot session.

5. Reattach to Screen
To check on the bot or stop it:
```bash

screen -r eclipse_bot
```
To stop the bot, press Ctrl + C within the Screen session.

6. Stop the Screen Session
To completely terminate the Screen session:
```bash

screen -S eclipse_bot -X quit
```
7. Deactivate the Virtual Environment (Optional)
If you no longer need the virtual environment in your current terminal session:
```bash

deactivate
```
Using the Bot
Once the bot is running, interact with it via Telegram:
Open Telegram and send the /start command to your bot.

A menu with buttons will appear, allowing you to perform the following actions:
Start: Check if a mining process is running.

Bitz Collect: Start a mining session in a Screen session named eclipse_bitz. Requires at least 0.0005 ETH.

Bitz Claim: Claim your mined BITZ rewards, with a confirmation prompt to prevent accidental claims.

Bitz Account: Display your wallet’s BITZ and ETH balances, plus proof-of-work details, in a formatted Markdown message.

Check Screen: List all active Screen sessions (e.g., eclipse_bitz or eclipse_bot).

Kill All Screens: Terminate all detached Screen sessions (useful for resetting mining processes).

Status: (Under development; currently displays "Coming soon").

RPC: Change the RPC URL by entering a new URL (e.g., https://eclipse.helius-rpc.com).

Example Workflow
Activate the virtual environment and start the bot:
```bash

source /root/bitz_env/bin/activate
screen -S eclipse_bot
python bot.py
```
Detach from the Screen session (Ctrl + A + D).

In Telegram, send /start and use the Bitz Collect button to start mining.

Monitor your balance with Bitz Account or claim rewards with Bitz Claim.

Use Check Screen to view active sessions or Kill All Screens to reset mining processes.

##Troubleshooting
Here are solutions to common issues you might encounter:
Bot Doesn’t Respond:
Check bitz_bot.log in the project directory for error messages (e.g., invalid BOT_TOKEN).

Verify BOT_TOKEN and CHAT_ID in .env are correct.

Ensure the bot is running in the eclipse_bot Screen session (screen -r eclipse_bot).

Confirm the virtual environment is active (source /root/bitz_env/bin/activate).

Mining Fails to Start:
Ensure your wallet has at least 0.0005 ETH (bitz account).

Check the RPC_URL in .env or update it via the RPC button.

Verify the Solana keypair exists at ~/.config/solana/id.json.

### Screen Session Issues:
List all Screen sessions: screen -ls.

Terminate a stuck session: screen -S session_name -X quit.

Use the Kill All Screens button to terminate all detached sessions.

## Command Timeouts:
If Bitz CLI commands (e.g., bitz account) take too long, increase the max_runtime parameter in the run_command function in bot.py.

### Virtual Environment Errors:
Ensure dependencies are installed in the virtual environment:
```bash

source /root/bitz_env/bin/activate
pip install -r requirements.txt
```
If the environment is corrupted, recreate it:
```bash

rm -rf /root/bitz_env
python3 -m venv /root/bitz_env
source /root/bitz_env/bin/activate
pip install -r requirements.txt
```
## Security Notes
Protect Sensitive Files:
Never share your .env file or Solana keypair (~/.config/solana/id.json). These contain critical information.

The .gitignore file ensures sensitive files are not uploaded to GitHub.

Backup Your Wallet:
Store your mnemonic phrase in a secure, offline location. Losing it will result in permanent loss of access to your wallet.

Use a Strong Passphrase:
Set a strong passphrase for your Solana wallet to enhance security.

## Monitor Logs:
Regularly review bitz_bot.log for errors or suspicious activity.

## Contributing
We welcome contributions to enhance the Eclipse Mining Bot! To contribute:
Fork the repository.

Create a feature branch:
```bash

git checkout -b feature/your-feature
```
Make changes and commit:
```bash

git commit -m "Add your feature"
```
Push to your fork:
```bash

git push origin feature/your-feature
```
Open a pull request on GitHub, describing your changes in detail.

Please ensure your code adheres to the existing style and includes updates to documentation where necessary.
## Support
For assistance or questions, contact the Eclipse community:
Discord: Join https://discord.gg/eclipse-fnd and visit the #powpow channel.

X: Follow and DM https://x.com/0xAsta2025
 for support and updates.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

