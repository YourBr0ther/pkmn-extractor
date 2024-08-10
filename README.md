# Pokémon Gen 3 (.pk3) File Parser

## Description

This Python script is designed to parse and analyze Pokémon Generation 3 (.pk3) files from Game Boy Advance era games (Ruby, Sapphire, Emerald, FireRed, LeafGreen). It extracts a wide range of information from these files, including basic stats, moves, IVs, EVs, origin information, and more.

## Features

- Extracts and decodes Pokémon nicknames and trainer names
- Reads personality values, OT IDs, and determines if a Pokémon is shiny
- Parses basic stats (HP, Attack, Defense, etc.)
- Extracts IVs and EVs for all stats
- Reads move sets and PP values
- Decodes Pokérus status
- Extracts origin information (met location, game of origin, etc.)
- Reads contest stats
- Determines Pokémon nature
- Exports data to both console output and JSON files

## Requirements

- Python 3.x
- CSV file containing character map for decoding names

## Setup

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Place your .pk3 files in a directory named `test_pokemon` in the same folder as the script.
4. Ensure you have a `charmap.csv` file in the same directory as the script. This file should contain the mapping for decoding Pokémon and trainer names.

## Usage

Run the script using Python: ```python app.py```

The script will process all .pk3 files in the `test_pokemon` directory, print the formatted data to the console, and export JSON files to an `exported_pokemon` directory.

## File Structure

- `app.py`: The main Python script containing all the parsing logic.
- `test_pokemon/`: Directory containing .pk3 files to be processed.
- `charmap.csv`: CSV file containing the character map for decoding names.
- `exported_pokemon/`: Output directory for JSON files (created by the script).

## Key Functions

- `read_personality_value`: Reads the Pokémon's personality value.
- `read_ot_id`: Extracts the original trainer's ID.
- `read_nickname_raw` and `decode_nickname`: Read and decode the Pokémon's nickname.
- `read_language`: Determines the language of the Pokémon data.
- `read_misc_flags`: Extracts miscellaneous flags.
- `read_ot_name`: Reads and decodes the original trainer's name.
- `read_markings`: Extracts Pokémon markings.
- `read_level`: Reads the Pokémon's current level.
- `read_stat`: Reads individual stat values.
- `read_species` and `read_item_held`: Extracts species and held item information.
- `read_experience` and `read_friendship`: Reads experience and friendship values.
- `read_move_set` and `read_pp_values`: Extracts move information and PP values.
- `read_ev_and_contest_stats`: Reads EVs and contest stats.
- `read_pokerus_status`: Determines Pokérus infection status.
- `read_met_location` and `read_origin_info`: Extracts information about where and how the Pokémon was obtained.
- `read_genetic_info`: Reads IVs and other genetic information.
- `get_nature` and `is_shiny`: Determines the Pokémon's nature and shiny status.

## Output

The script provides two types of output:

1. Console output: Formatted text displaying all extracted information for each Pokémon.
2. JSON files: Detailed data for each Pokémon exported as individual JSON files in the `exported_pokemon` directory.

## Customization

You can modify the script to handle different input/output directories by changing the `directory` and `output_dir` variables at the bottom of the script.

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please feel free to submit pull requests or open issues for any bugs or feature requests.

## License

GPL-3.0 license

## Acknowledgements

This script was created to analyze Pokémon data from Generation 3 games. It is not affiliated with or endorsed by Nintendo, Game Freak, or The Pokémon Company.