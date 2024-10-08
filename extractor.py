import os
import csv

met_locations_dict = {
    '0': 'Littleroot Town',
    '1': 'Oldale Town',
    '2': 'Dewford Town',
    '3': 'Lavaridge Town',
    '4': 'Fallarbor Town',
    '5': 'Verdanturf Town',
    '6': 'Pacifidlog Town',
    '7': 'Petalburg City',
    '8': 'Slateport City',
    '9': 'Mauville City',
    '10': 'Rustboro City',
    '11': 'Fortree City',
    '12': 'Lilycove City',
    '13': 'Mossdeep City',
    '14': 'Sootopolis City',
    '15': 'Ever Grande City',
    '16': 'Route 101',
    '17': 'Route 102',
    '18': 'Route 103',
    '19': 'Route 104',
    '20': 'Route 105',
    '21': 'Route 106',
    '22': 'Route 107',
    '23': 'Route 108',
    '24': 'Route 109',
    '25': 'Route 110',
    '26': 'Route 111',
    '27': 'Route 112',
    '28': 'Route 113',
    '29': 'Route 114',
    '30': 'Route 115',
    '31': 'Route 116',
    '32': 'Route 117',
    '33': 'Route 118',
    '34': 'Route 119',
    '35': 'Route 120',
    '36': 'Route 121',
    '37': 'Route 122',
    '38': 'Route 123',
    '39': 'Route 124',
    '40': 'Route 125',
    '41': 'Route 126',
    '42': 'Route 127',
    '43': 'Route 128',
    '44': 'Route 129',
    '45': 'Route 130',
    '46': 'Route 131',
    '47': 'Route 132',
    '48': 'Route 133',
    '49': 'Route 134',
    '50': 'Underwater (Route 124)',
    '51': 'Underwater (Route 126)',
    '52': 'Underwater (Route 127)',
    '53': 'Underwater (Route 128)',
    '54': 'Underwater (Sootopolis City)',
    '55': 'Granite Cave',
    '56': 'Mt. Chimney',
    '57': 'Safari Zone',
    '58': 'Battle TowerRS/Battle FrontierE',
    '59': 'Petalburg Woods',
    '60': 'Rusturf Tunnel',
    '61': 'Abandoned Ship',
    '62': 'New Mauville',
    '63': 'Meteor Falls',
    '64': 'Meteor Falls (unused)',
    '65': 'Mt. Pyre',
    '66': 'Hideout* (Magma HideoutR/Aqua HideoutS)',
    '67': 'Shoal Cave',
    '68': 'Seafloor Cavern',
    '69': 'Underwater (Seafloor Cavern)',
    '70': 'Victory Road',
    '71': 'Mirage Island',
    '72': 'Cave of Origin',
    '73': 'Southern Island',
    '74': 'Fiery Path',
    '75': 'Fiery Path (unused)',
    '76': 'Jagged Pass',
    '77': 'Jagged Pass (unused)',
    '78': 'Sealed Chamber',
    '79': 'Underwater (Route 134)',
    '80': 'Scorched Slab',
    '81': 'Island Cave',
    '82': 'Desert Ruins',
    '83': 'Ancient Tomb',
    '84': 'Inside of Truck',
    '85': 'Sky Pillar',
    '86': 'Secret Base',
    '87': 'Ferry',
    '88': 'Pallet Town',
    '89': 'Viridian City',
    '90': 'Pewter City',
    '91': 'Cerulean City',
    '92': 'Lavender Town',
    '93': 'Vermilion City',
    '94': 'Celadon City',
    '95': 'Fuchsia City',
    '96': 'Cinnabar Island',
    '97': 'Indigo Plateau',
    '98': 'Saffron City',
    '99': 'Route 4 (Pokémon Center)',
    '100': 'Route 10 (Pokémon Center)',
    '101': 'Route 1',
    '102': 'Route 2',
    '103': 'Route 3',
    '104': 'Route 4',
    '105': 'Route 5',
    '106': 'Route 6',
    '107': 'Route 7',
    '108': 'Route 8',
    '109': 'Route 9',
    '110': 'Route 10',
    '111': 'Route 11',
    '112': 'Route 12',
    '113': 'Route 13',
    '114': 'Route 14',
    '115': 'Route 15',
    '116': 'Route 16',
    '117': 'Route 17',
    '118': 'Route 18',
    '119': 'Route 19',
    '120': 'Route 20',
    '121': 'Route 21',
    '122': 'Route 22',
    '123': 'Route 23',
    '124': 'Route 24',
    '125': 'Route 25',
    '126': 'Viridian Forest',
    '127': 'Mt. Moon',
    '128': 'S.S. Anne',
    '129': 'Underground Path (Routes 5-6)',
    '130': 'Underground Path (Routes 7-8)',
    '131': 'Diglett\'s Cave',
    '132': 'Victory Road',
    '133': 'Rocket Hideout',
    '134': 'Silph Co.',
    '135': 'Pokémon Mansion',
    '136': 'Safari Zone',
    '137': 'Pokémon League',
    '138': 'Rock Tunnel',
    '139': 'Seafoam Islands',
    '140': 'Pokémon Tower',
    '141': 'Cerulean Cave',
    '142': 'Power Plant',
    '143': 'One Island',
    '144': 'Two Island',
    '145': 'Three Island',
    '146': 'Four Island',
    '147': 'Five Island',
    '148': 'Seven Island',
    '149': 'Six Island',
    '150': 'Kindle Road',
    '151': 'Treasure Beach',
    '152': 'Cape Brink',
    '153': 'Bond Bridge',
    '154': 'Three Isle Port',
    '155': 'Sevii Isle 6',
    '156': 'Sevii Isle 7',
    '157': 'Sevii Isle 8',
    '158': 'Sevii Isle 9',
    '159': 'Resort Gorgeous',
    '160': 'Water Labyrinth',
    '161': 'Five Isle Meadow',
    '162': 'Memorial Pillar',
    '163': 'Outcast Island',
    '164': 'Green Path',
    '165': 'Water Path',
    '166': 'Ruin Valley',
    '167': 'Trainer Tower (exterior)',
    '168': 'Canyon Entrance',
    '169': 'Sevault Canyon',
    '170': 'Tanoby Ruins',
    '171': 'Sevii Isle 22',
    '172': 'Sevii Isle 23',
    '173': 'Sevii Isle 24',
    '174': 'Navel Rock',
    '175': 'Mt. Ember',
    '176': 'Berry Forest',
    '177': 'Icefall Cave',
    '178': 'Rocket Warehouse',
    '179': 'Trainer Tower',
    '180': 'Dotted Hole',
    '181': 'Lost Cave',
    '182': 'Pattern Bush',
    '183': 'Altering Cave',
    '184': 'Tanoby Chambers',
    '185': 'Three Isle Path',
    '186': 'Tanoby Key',
    '187': 'Birth Island',
    '188': 'Monean Chamber',
    '189': 'Liptoo Chamber',
    '190': 'Weepth Chamber',
    '191': 'Dilford Chamber',
    '192': 'Scufib Chamber',
    '193': 'Rixy Chamber',
    '194': 'Viapois Chamber',
    '195': 'Ember Spa',
    '196': 'Celadon Dept.FRLG Special AreaE',
    '197': 'Aqua Hideout',
    '198': 'Magma Hideout',
    '199': 'Mirage Tower',
    '200': 'Birth Island',
    '201': 'Faraway Island',
    '202': 'Artisan Cave',
    '203': 'Marine Cave',
    '204': 'Underwater (Marine Cave)',
    '205': 'Terra Cave',
    '206': 'Underwater (Route 105)',
    '207': 'Underwater (Route 125)',
    '208': 'Underwater (Route 129)',
    '209': 'Desert Underpass',
    '210': 'Altering Cave',
    '211': 'Navel Rock',
    '212': 'Trainer Hill',
    '253': '(gift egg)',
    '254': '(in-game trade)',
    '255': '(fateful encounter)',
}

natures_dict = {
    '0': 'Hardy',
    '1': 'Lonely',
    '2': 'Brave',
    '3': 'Adamant',
    '4': 'Naughty',
    '5': 'Bold',
    '6': 'Docile',
    '7': 'Relaxed',
    '8': 'Impish',
    '9': 'Lax',
    '10': 'Timid',
    '11': 'Hasty',
    '12': 'Serious',
    '13': 'Jolly',
    '14': 'Naive',
    '15': 'Modest',
    '16': 'Mild',
    '17': 'Quiet',
    '18': 'Bashful',
    '19': 'Rash',
    '20': 'Calm',
    '21': 'Gentle',
    '22': 'Sassy',
    '23': 'Careful',
    '24': 'Quirky',
}
import requests
import json

# Configurable variables
DIRECTORY = "test_pokemon"  # Directory where the .pk3 files are located
OUTPUT_DIR = "exported_pokemon"  # Output directory for JSON files
CHARMAP_PATH = "charmap.csv"  # Path to the character map CSV file


# Utility functions
def read_personality_value(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            return int.from_bytes(file.read(4), byteorder="little")
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading personality value: {e}")
        return None


def read_ot_id(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x04)
            return int.from_bytes(file.read(4), byteorder="little")
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading OT ID: {e}")
        return None


def read_nickname_raw(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x08)
            return file.read(10)
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading nickname: {e}")
        return None


def load_charmap(charmap_path):
    charmap = {}
    try:
        with open(charmap_path, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            if "Hex" not in reader.fieldnames or "Char" not in reader.fieldnames:
                raise ValueError("CSV file must contain 'Hex' and 'Char' columns")
            for row in reader:
                try:
                    hex_value = int(row["Hex"], 16)
                    charmap[hex_value] = row["Char"]
                except ValueError as e:
                    print(f"Error processing row {row}: {e}")
    except (FileNotFoundError, IOError, ValueError) as e:
        print(f"Error loading charmap: {e}")
    return charmap


def load_moves(csv_file_path):
    moves = {}
    try:
        with open(csv_file_path, mode="r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                moves[int(row["Number"])] = row["Name"]
    except (FileNotFoundError, IOError) as e:
        print(f"Error loading moves CSV: {e}")
    return moves


def decode_nickname(nickname_raw, charmap):
    if nickname_raw is None:
        return "Unknown"
    nickname = ""
    for byte in nickname_raw:
        if (
            byte == 0x00 or byte not in charmap
        ):  # Assuming 0x00 is the termination character
            break
        nickname += charmap.get(byte, "?")
    return nickname


def read_language(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x12)
            language_byte = int.from_bytes(file.read(1), byteorder="little")
            language_map = {
                1: "Japanese",
                2: "English",
                3: "French",
                4: "Italian",
                5: "German",
                6: "unused",
                7: "Spanish",
            }
            return language_map.get(language_byte, "Unknown")
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading language: {e}")
        return "Unknown"


def read_misc_flags(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x13)
            misc_flags_byte = int.from_bytes(file.read(1), byteorder="little")
            flags = {
                "Is Bad Egg": bool(misc_flags_byte & 0b00000001),
                "Has Species": bool(misc_flags_byte & 0b00000010),
                "Use Egg Name": bool(misc_flags_byte & 0b00000100),
                "Block Box RS": bool(misc_flags_byte & 0b00001000),
            }
            return flags
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading misc flags: {e}")
        return None


def read_ot_name(pk3_file_path, charmap):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x14)
            ot_name_raw = file.read(7)
            return decode_nickname(ot_name_raw, charmap)
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading OT name: {e}")
        return "Unknown"


def read_markings(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x1B)
            markings_byte = int.from_bytes(file.read(1), byteorder="little")
            markings = []
            if markings_byte & 0b00000001:
                markings.append("Circle")
            if markings_byte & 0b00000010:
                markings.append("Square")
            if markings_byte & 0b00000100:
                markings.append("Triangle")
            if markings_byte & 0b00001000:
                markings.append("Heart")
            return markings if markings else ["None"]
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading markings: {e}")
        return ["None"]


def read_level(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x54)
            return int.from_bytes(file.read(1), byteorder="little")
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading level: {e}")
        return 0


def read_stat(pk3_file_path, offset):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(offset)
            return int.from_bytes(file.read(2), byteorder="little")
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading stat at offset {offset}: {e}")
        return 0


def read_species(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x20)  # Assuming species is stored at this offset
            species = int.from_bytes(file.read(2), byteorder="little")
            return species
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading species: {e}")
        return None

def read_item_held(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x22)
            return int.from_bytes(file.read(2), byteorder="little")
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading item held: {e}")
        return None


def read_experience(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x24)
            return int.from_bytes(file.read(4), byteorder="little")
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading experience: {e}")
        return 0


def read_friendship(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x29)
            return int.from_bytes(file.read(1), byteorder="little")
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading friendship: {e}")
        return 0

def read_move_set(pk3_file_path, moves):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x2C)
            move_names = []
            for _ in range(4):
                move_number = int.from_bytes(file.read(2), byteorder="little")
                move_name = moves.get(move_number, "")
                if move_number == 0:
                    move_name = ""  # Replace "Unknown Move (0)" with an empty string
                move_names.append(move_name)
            return move_names
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading move set: {e}")
        return []

def read_pp_values(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x34)
            pp_values = []
            for _ in range(4):
                pp = int.from_bytes(file.read(1), byteorder="little")
                pp_values.append(pp)
            return pp_values
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading PP values: {e}")
        return [0, 0, 0, 0]


def read_ev_and_contest_stats(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x38)
            return {
                "HP EV": int.from_bytes(file.read(1), byteorder="little"),
                "Attack EV": int.from_bytes(file.read(1), byteorder="little"),
                "Defense EV": int.from_bytes(file.read(1), byteorder="little"),
                "Speed EV": int.from_bytes(file.read(1), byteorder="little"),
                "Sp. Attack EV": int.from_bytes(file.read(1), byteorder="little"),
                "Sp. Defense EV": int.from_bytes(file.read(1), byteorder="little"),
                "Coolness": int.from_bytes(file.read(1), byteorder="little"),
                "Beauty": int.from_bytes(file.read(1), byteorder="little"),
                "Cuteness": int.from_bytes(file.read(1), byteorder="little"),
                "Smartness": int.from_bytes(file.read(1), byteorder="little"),
                "Toughness": int.from_bytes(file.read(1), byteorder="little"),
                "Feel": int.from_bytes(file.read(1), byteorder="little"),
            }
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading EV and contest stats: {e}")
        return {
            "HP EV": 0,
            "Attack EV": 0,
            "Defense EV": 0,
            "Speed EV": 0,
            "Sp. Attack EV": 0,
            "Sp. Defense EV": 0,
            "Coolness": 0,
            "Beauty": 0,
            "Cuteness": 0,
            "Smartness": 0,
            "Toughness": 0,
            "Feel": 0,
        }


def read_pokerus_status(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x44)  # Pokerus is at 0x44 (two bytes: 0x44 and 0x45)
            pokerus_byte = int.from_bytes(file.read(1), byteorder="little")
            days_left = pokerus_byte & 0b00001111  # Bits 0-3
            strain = (pokerus_byte & 0b11110000) >> 4  # Bits 4-7
            return {"Pokerus Days Left": days_left, "Pokerus Strain": strain}
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading Pokerus status: {e}")
        return {"Pokerus Days Left": 0, "Pokerus Strain": 0}


def read_met_location(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x45)  # Met Location is at 0x45
            met_location_code = int.from_bytes(file.read(1), byteorder="little")
            return met_locations_dict.get(str(met_location_code), "Unknown Location")
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading met location: {e}")
        return "Unknown Location"

def read_origin_info(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x46)  # Origin Info is at 0x46-0x47
            origin_info = int.from_bytes(file.read(2), byteorder="little")
            gender = "Female" if origin_info & (1 << 15) else "Male"  # Bit 15
            ball = (origin_info >> 11) & 0b1111  # Bits 11-14
            game_of_origin = (origin_info >> 7) & 0b1111  # Bits 7-10
            met_type = origin_info & 0b01111111  # Bits 0-6
            return {
                "Gender": gender,
                "Ball": ball,
                "Game of Origin": game_of_origin,
                "Met Type": "Hatched" if met_type == 0 else "Caught",
            }
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading origin info: {e}")
        return {
            "Gender": "Unknown",
            "Ball": 0,
            "Game of Origin": 0,
            "Met Type": "Unknown",
        }


def read_genetic_info(pk3_file_path):
    try:
        with open(pk3_file_path, "rb") as file:
            file.seek(0x48)  # Genetic info is at 0x48-0x4B (4 bytes)
            genetic_info = int.from_bytes(file.read(4), byteorder="little")

            # Extracting individual components from the genetic info
            hp_iv = genetic_info & 0b00000000000000000000000000011111  # Bits 0-4
            attack_iv = (
                genetic_info >> 5
            ) & 0b00000000000000000000000000011111  # Bits 5-9
            defense_iv = (
                genetic_info >> 10
            ) & 0b00000000000000000000000000011111  # Bits 10-14
            speed_iv = (
                genetic_info >> 15
            ) & 0b00000000000000000000000000011111  # Bits 15-19
            sp_attack_iv = (
                genetic_info >> 20
            ) & 0b00000000000000000000000000011111  # Bits 20-24
            sp_defense_iv = (
                genetic_info >> 25
            ) & 0b00000000000000000000000000011111  # Bits 25-29

            is_egg = (genetic_info >> 30) & 0b1  # Bit 30
            ability_number = (genetic_info >> 31) & 0b1  # Bit 31

            return {
                "HP IV": hp_iv,
                "Attack IV": attack_iv,
                "Defense IV": defense_iv,
                "Speed IV": speed_iv,
                "Sp. Attack IV": sp_attack_iv,
                "Sp. Defense IV": sp_defense_iv,
                "Is Egg": bool(is_egg),
                "Ability Number": 2 if ability_number else 1,
            }
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading genetic info: {e}")
        return {
            "HP IV": 0,
            "Attack IV": 0,
            "Defense IV": 0,
            "Speed IV": 0,
            "Sp. Attack IV": 0,
            "Sp. Defense IV": 0,
            "Is Egg": False,
            "Ability Number": 1,
        }

def get_nature(personality_value):
    try:
        nature_index = personality_value % 25
        return natures_dict.get(str(nature_index), "Unknown Nature")
    except TypeError as e:
        print(f"Error determining nature: {e}")
        return "Unknown Nature"

def is_shiny(ot_id, personality_value):
    try:
        tid = ot_id & 0xFFFF  # Lower 16 bits
        sid = (ot_id >> 16) & 0xFFFF  # Upper 16 bits
        tid_sid_xor = tid ^ sid

        upper_half_personality = (personality_value >> 16) & 0xFFFF
        lower_half_personality = personality_value & 0xFFFF

        shiny_value = tid_sid_xor ^ upper_half_personality ^ lower_half_personality

        return shiny_value < 8
    except TypeError as e:
        print(f"Error determining shiny status: {e}")
        return False


def clean_text(text):
    """
    Cleans the input text by removing newline and form feed characters, and replacing \u00e9 with é.
    :param text: The text to clean.
    :return: Cleaned text.
    """
    return text.replace('\n', ' ').replace('\f', ' ').replace('\u00e9', 'é')

def get_pokemon_data(species_identifier):
    """
    Fetches types, Pokédex entries, species name, and species number from the PokeAPI for a given Pokémon species identifier.
    :param species_identifier: The species name or ID of the Pokémon to fetch data for.
    :return: Dictionary containing species name, species number, types, and a list of the 5 longest, unique Pokédex entries.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{species_identifier}"
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{species_identifier}"

    try:
        # Fetching basic Pokémon data to get the types
        response = requests.get(url)
        response.raise_for_status()
        pokemon_data = response.json()

        # Extracting types
        types = [type_info["type"]["name"] for type_info in pokemon_data["types"]]

        # Fetching species data to get Pokédex entries, species name, and species number
        response = requests.get(species_url)
        response.raise_for_status()
        species_data = response.json()

        # Extracting species name and species number
        species_name = species_data["name"]
        species_number = species_data["id"]

        # Extracting and cleaning 8 Pokédex entries
        raw_entries = [entry["flavor_text"] for entry in species_data["flavor_text_entries"][:8]]
        cleaned_entries = list({clean_text(entry) for entry in raw_entries})  # Remove duplicates
        
        # Sorting by length and keeping the 5 longest entries
        cleaned_entries.sort(key=len, reverse=True)
        longest_entries = cleaned_entries[:5]

        return {
            "species_name": species_name.capitalize(),
            "species_number": species_number,
            "types": types,
            "pokedex_entries": longest_entries
        }

    except requests.RequestException as e:
        print(f"Error fetching data for species {species_identifier}: {e}")
        return None
    
def format_pokemon_data(filename, data):
    output = []
    output.append(f"=== {filename} ===")
    output.append(f"General Info:")
    output.append(f"  Personality Value: {data['Personality Value']}")
    output.append(f"  Nature: {data['Nature']}, Is Shiny: {data['Is Shiny']}")
    output.append(f"  Nickname: {data['Nickname']}")
    output.append(f"  Language: {data['Language']}")
    output.append(f"  Level: {data['Level']}")
    output.append(
        f"  Experience: {data['Experience']}, Friendship: {data['Friendship']}"
    )
    output.append(f"Trainer Info:")
    output.append(f"  OT ID: {data['Trainer']['OT ID (Decimal)']}")
    output.append(f"  OT Name: {data['Trainer']['OT Name']}")
    output.append(f"  Misc Flags: {data['Trainer']['Misc Flags']}")
    output.append(f"Stats:")
    output.append(
        f"  HP: {data['Stats']['HP']}, Attack: {data['Stats']['Attack']}, Defense: {data['Stats']['Defense']}, Speed: {data['Stats']['Speed']}, Sp. Attack: {data['Stats']['Sp. Attack']}, Sp. Defense: {data['Stats']['Sp. Defense']}"
    )
    output.append(f"  Species: {data['Species']}, Item Held: {data['Item Held']}")
    output.append(
        f"  IVs - HP: {data['IVs']['HP IV']}, Attack: {data['IVs']['Attack IV']}, Defense: {data['IVs']['Defense IV']}, Speed: {data['IVs']['Speed IV']}, Sp. Attack: {data['IVs']['Sp. Attack IV']}, Sp. Defense: {data['IVs']['Sp. Defense IV']}"
    )
    output.append(
        f"  EVs - HP: {data['EVs']['HP EV']}, Attack: {data['EVs']['Attack EV']}, Defense: {data['EVs']['Defense EV']}, Speed: {data['EVs']['Speed EV']}, Sp. Attack: {data['EVs']['Sp. Attack EV']}, Sp. Defense: {data['EVs']['Sp. Defense EV']}"
    )
    output.append(f"Moves:")
    output.append(f"  Moves: {data['Moves']}")
    output.append(f"  PP Values: {data['PP Values']}")
    output.append(f"Condition:")
    output.append(
        f"  Pokerus: Days Left: {data['Condition']['Pokerus Days Left']}, Strain: {data['Condition']['Pokerus Strain']}"
    )
    output.append(f"  Markings: {data['Condition']['Markings']}")
    output.append(f"Origin Info:")
    output.append(f"  Met Location: {data['Origin Info']['Met Location']}")
    output.append(
        f"  Gender: {data['Origin Info']['Gender']}, Ball: {data['Origin Info']['Ball']}, Game of Origin: {data['Origin Info']['Game of Origin']}, Met Type: {data['Origin Info']['Met Type']}"
    )
    output.append(
        f"  Is Egg: {data['Origin Info']['Is Egg']}, Ability Number: {data['Origin Info']['Ability Number']}"
    )
    output.append(f"Contest Stats:")
    output.append(
        f"  Coolness: {data['Contest Stats']['Coolness']}, Beauty: {data['Contest Stats']['Beauty']}, Cuteness: {data['Contest Stats']['Cuteness']}, Smartness: {data['Contest Stats']['Smartness']}, Toughness: {data['Contest Stats']['Toughness']}, Feel: {data['Contest Stats']['Feel']}"
    )

    if 'Additional Data' in data:
        output.append(f"Additional Data:")
        output.append(f"  Types: {', '.join(data['Additional Data']['types'])}")
        output.append(f"  Pokedex Entries: {', '.join(data['Additional Data']['pokedex_entries'])}")

    output.append("\n")
    return "\n".join(output)


def export_to_json(filename, data, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        json_path = os.path.join(output_dir, f"{filename}.json")
        with open(json_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
    except (FileNotFoundError, IOError) as e:
        print(f"Error exporting to JSON: {e}")


def process_pk3_files(directory, charmap, output_dir, moves):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.endswith(".pk3"):
            try:
                file_path = os.path.join(directory, filename)
                personality_value = read_personality_value(file_path)
                ot_id = read_ot_id(file_path)
                nickname_raw = read_nickname_raw(file_path)
                nickname = decode_nickname(nickname_raw, charmap)
                language = read_language(file_path)
                misc_flags = read_misc_flags(file_path)
                ot_name = read_ot_name(file_path, charmap)
                markings = read_markings(file_path)
                level = read_level(file_path)
                hp = read_stat(file_path, 0x58)
                attack = read_stat(file_path, 0x5A)
                defense = read_stat(file_path, 0x5C)
                speed = read_stat(file_path, 0x5E)
                sp_attack = read_stat(file_path, 0x60)
                sp_defense = read_stat(file_path, 0x62)
                species = read_species(file_path)
                item_held = read_item_held(file_path)
                experience = read_experience(file_path)
                friendship = read_friendship(file_path)
                moves_set = read_move_set(file_path, moves)
                pp_values = read_pp_values(file_path)
                ev_and_contest_stats = read_ev_and_contest_stats(file_path)
                pokerus_status = read_pokerus_status(file_path)
                met_location = read_met_location(file_path)
                origin_info = read_origin_info(file_path)
                genetic_info = read_genetic_info(file_path)
                nature = get_nature(personality_value)
                shiny = is_shiny(ot_id, personality_value)

                if species is None:
                    raise ValueError("Species ID could not be read from the file.")

                # Fetch additional Pokémon data using the PokeAPI
                additional_data = get_pokemon_data(species)

                if additional_data is None:
                    raise ValueError(f"Could not fetch additional data for species ID {species}.")

                # Create a data dictionary
                data = {
                    "Personality Value": (
                        f"{personality_value:08X}"
                        if personality_value is not None
                        else "Unknown"
                    ),
                    "Nature": nature if nature != "Unknown" else "Unknown",
                    "Is Shiny": shiny if shiny is not None else False,
                    "Nickname": nickname,
                    "Language": language,
                    "Level": level,
                    "Experience": experience,
                    "Friendship": friendship,
                    "Trainer": {
                        "OT ID (Decimal)": ot_id if ot_id is not None else "Unknown",
                        "OT Name": ot_name,
                        "Misc Flags": misc_flags if misc_flags is not None else {},
                    },
                    "Species": {
                        "ID": species,  # Ensure species ID is included here
                        "Name": additional_data["species_name"],  # Include species name
                        "Number": additional_data["species_number"]  # Include species number
                    },
                    "Stats": {
                        "HP": hp,
                        "Attack": attack,
                        "Defense": defense,
                        "Speed": speed,
                        "Sp. Attack": sp_attack,
                        "Sp. Defense": sp_defense,
                    },
                    "IVs": {
                        "HP IV": genetic_info["HP IV"],
                        "Attack IV": genetic_info["Attack IV"],
                        "Defense IV": genetic_info["Defense IV"],
                        "Speed IV": genetic_info["Speed IV"],
                        "Sp. Attack IV": genetic_info["Sp. Attack IV"],
                        "Sp. Defense IV": genetic_info["Sp. Defense IV"],
                    },
                    "EVs": {
                        "HP EV": ev_and_contest_stats["HP EV"],
                        "Attack EV": ev_and_contest_stats["Attack EV"],
                        "Defense EV": ev_and_contest_stats["Defense EV"],
                        "Speed EV": ev_and_contest_stats["Speed EV"],
                        "Sp. Attack EV": ev_and_contest_stats["Sp. Attack EV"],
                        "Sp. Defense EV": ev_and_contest_stats["Sp. Defense EV"],
                    },
                    "Moves": moves_set,
                    "PP Values": pp_values,
                    "Condition": {
                        "Pokerus Days Left": pokerus_status["Pokerus Days Left"],
                        "Pokerus Strain": pokerus_status["Pokerus Strain"],
                        "Markings": ", ".join(markings),
                    },
                    "Origin Info": {
                        "Met Location": met_location,  # Updated to store the name
                        "Gender": origin_info["Gender"],
                        "Ball": origin_info["Ball"],
                        "Game of Origin": origin_info["Game of Origin"],
                        "Met Type": origin_info["Met Type"],
                        "Is Egg": genetic_info["Is Egg"],
                        "Ability Number": genetic_info["Ability Number"],
                    },
                    "Contest Stats": {
                        "Coolness": ev_and_contest_stats["Coolness"],
                        "Beauty": ev_and_contest_stats["Beauty"],
                        "Cuteness": ev_and_contest_stats["Cuteness"],
                        "Smartness": ev_and_contest_stats["Smartness"],
                        "Toughness": ev_and_contest_stats["Toughness"],
                        "Feel": ev_and_contest_stats["Feel"],
                    },
                }

                # Ensure the item_held is added to the data dictionary, even if it's None
                if item_held is not None:
                    data["Item Held"] = item_held
                else:
                    data["Item Held"] = "None"

                # Include additional Pokémon data if available
                if additional_data:
                    data["Additional Data"] = additional_data

                # Print formatted data to the console
                print(format_pokemon_data(filename, data))

                # Export to JSON
                export_to_json(os.path.splitext(filename)[0], data, output_dir)

            except Exception as e:
                print(f"Error processing file {filename}: {e}")

# Load the moves from the CSV
moves_csv_path = "moves.csv"  # Path to your moves.csv file
moves = load_moves(moves_csv_path)

# Load the character map
charmap = load_charmap(CHARMAP_PATH)

# Process the files, print the formatted output, and export to JSON
process_pk3_files(DIRECTORY, charmap, OUTPUT_DIR, moves)