
# Pokémon Generation 3 Data Extractor

This Python script extracts and decodes data from Generation 3 Pokémon game files (`.pk3`) and outputs the information in a human-readable format or as JSON files.

## Features

- **Extract Personality Value**: Reads and interprets the Pokémon's personality value.
- **Trainer Information**: Extracts the Original Trainer's ID, name, and language.
- **Pokémon Attributes**: Retrieves the Pokémon's nickname, gender, markings, level, and species.
- **Battle Stats**: Extracts IVs, EVs, contest stats, and move sets.
- **Genetic Information**: Reads genetic info such as IVs and ability numbers.
- **Shiny Determination**: Calculates if the Pokémon is shiny based on its data.
- **Met Information**: Retrieves where and how the Pokémon was obtained.
- **Output Options**: Provides data as console output or exports it as JSON files.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/pokemon-gen3-extractor.git
    cd pokemon-gen3-extractor
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Place your `.pk3` files in the `input` directory and run the script:

```bash
python app.py
```

### Example Output

#### Console Output
```plaintext
Reading file: Pikachu.pk3
Species: Pikachu
Level: 25
OT Name: Ash
Shiny: No
...
```

#### JSON Output

The JSON files will be saved in the `exported_pokemon` directory. Here is an example structure:

```json
{
    "Species": "Pikachu",
    "Level": 25,
    "OT Name": "Ash",
    "Shiny": false,
    ...
}
```

## Key Functions

- `read_personality_value`: Reads the Pokémon's personality value.
- `read_ot_id`: Extracts the original trainer's ID.
- `read_nickname_raw` and `decode_nickname`: Read and decode the Pokémon's nickname.
- `read_level`: Reads the Pokémon's current level.
- `read_stat`: Reads individual stat values.
- `read_species` and `read_item_held`: Extracts species and held item information.
- `read_genetic_info`: Reads IVs and other genetic information.
- `get_nature` and `is_shiny`: Determines the Pokémon's nature and shiny status.

## Customization

You can modify the script to handle different input/output directories by changing the `directory` and `output_dir` variables at the bottom of the script.

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please feel free to submit pull requests or open issues for any bugs or feature requests.

## License

This project is licensed under the GPL-3.0 License.

## Acknowledgements

This script was created to analyze Pokémon data from Generation 3 games. It is not affiliated with or endorsed by Nintendo, Game Freak, or The Pokémon Company.

