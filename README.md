# Pokémon Data Extractor and Character Card Creator

This repository contains two Python scripts for extracting data from Pokémon game files (.pk3) and creating character cards for use in AI role-playing scenarios.

## Scripts

### 1. extractor.py

This script extracts detailed information from .pk3 files, which are used to store individual Pokémon data in certain Pokémon games.

#### Features:
- Reads various attributes from .pk3 files (personality value, nickname, stats, moves, etc.)
- Decodes game-specific encodings using a character map
- Fetches additional Pokémon data from the PokeAPI
- Exports extracted data to JSON files
- Provides console output of formatted Pokémon data

#### Requirements:
- Python 3.x
- `requests` library
- CSV files: `charmap.csv` and `moves.csv`

#### Usage:
1. Place your .pk3 files in the specified input directory
2. Run the script: `python extractor.py`
3. Check the output directory for JSON files and console for formatted output

### 2. character_maker.py

This script takes the JSON files produced by `extractor.py` and creates character cards suitable for AI role-playing scenarios.

#### Features:
- Loads Pokémon data from JSON files
- Calculates friendship levels
- Downloads sprite images from PokeAPI
- Creates detailed character cards with personality traits
- Exports character cards in a format compatible with AI role-playing platforms (e.g., SillyTavern)

#### Requirements:
- Python 3.x
- `requests` library
- `Pillow` library (for image processing)

#### Usage:
1. Ensure you have JSON files produced by `extractor.py` in the input directory
2. Run the script: `python character_maker.py`
3. Check the output directory for character card files (.png with embedded JSON)

## Setup

1. Clone this repository
2. Install required libraries: `pip install requests pillow`
3. Prepare your .pk3 files and place them in the input directory
4. Run `extractor.py` followed by `character_maker.py`

## Configuration

Both scripts use configurable variables for input/output directories and file paths. Adjust these in the script files as needed:

- `DIRECTORY`: Input directory for .pk3 files
- `OUTPUT_DIR`: Output directory for JSON and character card files
- `CHARMAP_PATH`: Path to the character map CSV file
- Other paths like `moves.csv` file location

## Notes

- These scripts are designed for educational and personal use
- Ensure you have the right to use any Pokémon data extracted with these scripts
- The character cards created are intended for use in AI role-playing scenarios and may not accurately represent official Pokémon characteristics

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/YourBr0ther/pkmn-extractor/issues) if you want to contribute.

## License

This project is licensed under the GPL-3.0 License.

