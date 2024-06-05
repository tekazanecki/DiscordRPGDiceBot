# Discord RPG Dice Bot

A Discord bot that facilitates dice rolls for various RPG systems such as Dungeons & Dragons, World of Darkness, and Cyberpunk. The bot uses the Discord.py library and supports modular commands through cogs.

## Features

- General dice rolls
- World of Darkness dice rolls with custom rules
- Cyberpunk dice rolls with critical hit mechanics

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/discord-rpg-dice-bot.git
    cd discord-rpg-dice-bot
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `creds.py` file in the root directory with your Discord bot token:**
    ```python
    discord_bot_key = 'YOUR_DISCORD_BOT_TOKEN'
    ```

## Usage

### Starting the Bot

To start the bot, run the following command:

```sh
python main.py
```

### Available Commands

#### General Commands

- **`!roll <notation>`**: Rolls dice based on the provided notation.
    - Example: `!roll 2k6+3`
- **`!roll_sum <notation>`**: Rolls dice and sums the results based on the provided notation.
    - Example: `!roll_sum 2k6+3`

#### World of Darkness Commands

- **`!wod_roll <notation>`**: Rolls dice for World of Darkness based on the provided notation.
    - Example: `!wod_roll 10/6 e9` where 10 is a number of dice, 6 is difficulty of roll, an 9 is a number on with dice are exploding.

#### Cyberpunk Commands

- **`!roll_cyber <notation>`**: Rolls a single d10 with modifiers for Cyberpunk.
    - Example: `!roll_cyber 10` where 10 is modifier that is add to roll.
- **`!roll_cyber_dmg <notation>`**: Rolls damage dice for Cyberpunk with critical hit mechanics.
    - Example: `!roll_cyber_dmg 10 2 head` where 10 is number of dice rolled, 2 is modifier that is add to roll, head is location of attack (default is body) 

## Code Overview

### `main.py`

Initializes the bot, loads extensions from the `cogs` directory, and sets up event handlers for ready state and messages.

### `general.py`

Defines commands for general dice rolls using the `roll_dice` function from `dice_roller_general`.

### `wod.py`

Defines commands for World of Darkness dice rolls using the `roll_dice_wod` function from `dice_roller_wod`.

### `cyberpunk.py`

Defines commands for Cyberpunk dice rolls using the `roll_cyber` and `roll_cyber_dmg` functions from `dice_roller_cyberpunk`.

### `dice_roller_general.py`

Provides a `roll_dice` function to handle general dice roll notation and calculations.

### `dice_roller_wod.py`

Provides `roll_wod` and `roll_dice_wod` functions to handle dice rolls and success calculations for World of Darkness.

### `dice_roller_cyberpunk.py`

Provides `roll_cyber` and `roll_cyber_dmg` functions to handle dice rolls and damage calculations for Cyberpunk, including critical hit mechanics.

### `cyberpunk_critical_hits.py`

Contains dictionaries for critical hit effects in Cyberpunk, separated by body and head injuries.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.