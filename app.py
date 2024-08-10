import os
import csv
import json

# Configurable variables
DIRECTORY = 'test_pokemon'          # Directory where the .pk3 files are located
OUTPUT_DIR = 'exported_pokemon'     # Output directory for JSON files
CHARMAP_PATH = 'charmap.csv'        # Path to the character map CSV file

# Utility functions
def read_personality_value(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            return int.from_bytes(file.read(4), byteorder='little')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading personality value: {e}")
        return None

def read_ot_id(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x04)
            return int.from_bytes(file.read(4), byteorder='little')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading OT ID: {e}")
        return None

def read_nickname_raw(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x08)
            return file.read(10)
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading nickname: {e}")
        return None

def load_charmap(charmap_path):
    charmap = {}
    try:
        with open(charmap_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'Hex' not in reader.fieldnames or 'Char' not in reader.fieldnames:
                raise ValueError("CSV file must contain 'Hex' and 'Char' columns")
            for row in reader:
                try:
                    hex_value = int(row['Hex'], 16)
                    charmap[hex_value] = row['Char']
                except ValueError as e:
                    print(f"Error processing row {row}: {e}")
    except (FileNotFoundError, IOError, ValueError) as e:
        print(f"Error loading charmap: {e}")
    return charmap

def load_moves(csv_file_path):
    moves = {}
    try:
        with open(csv_file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                moves[int(row['Number'])] = row['Name']
    except (FileNotFoundError, IOError) as e:
        print(f"Error loading moves CSV: {e}")
    return moves

def decode_nickname(nickname_raw, charmap):
    if nickname_raw is None:
        return "Unknown"
    nickname = ''
    for byte in nickname_raw:
        if byte == 0x00 or byte not in charmap:  # Assuming 0x00 is the termination character
            break
        nickname += charmap.get(byte, '?')
    return nickname

def read_language(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x12)
            language_byte = int.from_bytes(file.read(1), byteorder='little')
            language_map = {
                1: 'Japanese',
                2: 'English',
                3: 'French',
                4: 'Italian',
                5: 'German',
                6: 'unused',
                7: 'Spanish'
            }
            return language_map.get(language_byte, 'Unknown')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading language: {e}")
        return 'Unknown'

def read_misc_flags(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x13)
            misc_flags_byte = int.from_bytes(file.read(1), byteorder='little')
            flags = {
                'Is Bad Egg': bool(misc_flags_byte & 0b00000001),
                'Has Species': bool(misc_flags_byte & 0b00000010),
                'Use Egg Name': bool(misc_flags_byte & 0b00000100),
                'Block Box RS': bool(misc_flags_byte & 0b00001000),
            }
            return flags
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading misc flags: {e}")
        return None

def read_ot_name(pk3_file_path, charmap):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x14)
            ot_name_raw = file.read(7)
            return decode_nickname(ot_name_raw, charmap)
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading OT name: {e}")
        return 'Unknown'

def read_markings(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x1B)
            markings_byte = int.from_bytes(file.read(1), byteorder='little')
            markings = []
            if markings_byte & 0b00000001:
                markings.append('Circle')
            if markings_byte & 0b00000010:
                markings.append('Square')
            if markings_byte & 0b00000100:
                markings.append('Triangle')
            if markings_byte & 0b00001000:
                markings.append('Heart')
            return markings if markings else ['None']
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading markings: {e}")
        return ['None']

def read_level(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x54)
            return int.from_bytes(file.read(1), byteorder='little')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading level: {e}")
        return 0

def read_stat(pk3_file_path, offset):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(offset)
            return int.from_bytes(file.read(2), byteorder='little')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading stat at offset {offset}: {e}")
        return 0

def read_species(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x20)
            return int.from_bytes(file.read(2), byteorder='little')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading species: {e}")
        return None

def read_item_held(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x22)
            return int.from_bytes(file.read(2), byteorder='little')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading item held: {e}")
        return None

def read_experience(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x24)
            return int.from_bytes(file.read(4), byteorder='little')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading experience: {e}")
        return 0

def read_friendship(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x29)
            return int.from_bytes(file.read(1), byteorder='little')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading friendship: {e}")
        return 0

def read_move_set(pk3_file_path, moves):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x2C)
            move_names = []
            for _ in range(4):
                move_number = int.from_bytes(file.read(2), byteorder='little')
                move_name = moves.get(move_number, f"Unknown Move ({move_number})")
                move_names.append(move_name)
            return move_names
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading move set: {e}")
        return []


def read_pp_values(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x34)
            pp_values = []
            for _ in range(4):
                pp = int.from_bytes(file.read(1), byteorder='little')
                pp_values.append(pp)
            return pp_values
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading PP values: {e}")
        return [0, 0, 0, 0]

def read_ev_and_contest_stats(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x38)
            return {
                'HP EV': int.from_bytes(file.read(1), byteorder='little'),
                'Attack EV': int.from_bytes(file.read(1), byteorder='little'),
                'Defense EV': int.from_bytes(file.read(1), byteorder='little'),
                'Speed EV': int.from_bytes(file.read(1), byteorder='little'),
                'Sp. Attack EV': int.from_bytes(file.read(1), byteorder='little'),
                'Sp. Defense EV': int.from_bytes(file.read(1), byteorder='little'),
                'Coolness': int.from_bytes(file.read(1), byteorder='little'),
                'Beauty': int.from_bytes(file.read(1), byteorder='little'),
                'Cuteness': int.from_bytes(file.read(1), byteorder='little'),
                'Smartness': int.from_bytes(file.read(1), byteorder='little'),
                'Toughness': int.from_bytes(file.read(1), byteorder='little'),
                'Feel': int.from_bytes(file.read(1), byteorder='little')
            }
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading EV and contest stats: {e}")
        return {
            'HP EV': 0, 'Attack EV': 0, 'Defense EV': 0, 'Speed EV': 0,
            'Sp. Attack EV': 0, 'Sp. Defense EV': 0, 'Coolness': 0,
            'Beauty': 0, 'Cuteness': 0, 'Smartness': 0, 'Toughness': 0,
            'Feel': 0
        }

def read_pokerus_status(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x44)  # Pokerus is at 0x44 (two bytes: 0x44 and 0x45)
            pokerus_byte = int.from_bytes(file.read(1), byteorder='little')
            days_left = pokerus_byte & 0b00001111  # Bits 0-3
            strain = (pokerus_byte & 0b11110000) >> 4  # Bits 4-7
            return {'Pokerus Days Left': days_left, 'Pokerus Strain': strain}
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading Pokerus status: {e}")
        return {'Pokerus Days Left': 0, 'Pokerus Strain': 0}

def read_met_location(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x45)  # Met Location is at 0x45
            return int.from_bytes(file.read(1), byteorder='little')
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading met location: {e}")
        return 0

def read_origin_info(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x46)  # Origin Info is at 0x46-0x47
            origin_info = int.from_bytes(file.read(2), byteorder='little')
            gender = 'Female' if origin_info & (1 << 15) else 'Male'  # Bit 15
            ball = (origin_info >> 11) & 0b1111  # Bits 11-14
            game_of_origin = (origin_info >> 7) & 0b1111  # Bits 7-10
            met_type = origin_info & 0b01111111  # Bits 0-6
            return {
                'Gender': gender,
                'Ball': ball,
                'Game of Origin': game_of_origin,
                'Met Type': 'Hatched' if met_type == 0 else 'Caught'
            }
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading origin info: {e}")
        return {
            'Gender': 'Unknown',
            'Ball': 0,
            'Game of Origin': 0,
            'Met Type': 'Unknown'
        }

def read_genetic_info(pk3_file_path):
    try:
        with open(pk3_file_path, 'rb') as file:
            file.seek(0x48)  # Genetic info is at 0x48-0x4B (4 bytes)
            genetic_info = int.from_bytes(file.read(4), byteorder='little')
            
            # Extracting individual components from the genetic info
            hp_iv = genetic_info & 0b00000000000000000000000000011111  # Bits 0-4
            attack_iv = (genetic_info >> 5) & 0b00000000000000000000000000011111  # Bits 5-9
            defense_iv = (genetic_info >> 10) & 0b00000000000000000000000000011111  # Bits 10-14
            speed_iv = (genetic_info >> 15) & 0b00000000000000000000000000011111  # Bits 15-19
            sp_attack_iv = (genetic_info >> 20) & 0b00000000000000000000000000011111  # Bits 20-24
            sp_defense_iv = (genetic_info >> 25) & 0b00000000000000000000000000011111  # Bits 25-29
            
            is_egg = (genetic_info >> 30) & 0b1  # Bit 30
            ability_number = (genetic_info >> 31) & 0b1  # Bit 31

            return {
                'HP IV': hp_iv,
                'Attack IV': attack_iv,
                'Defense IV': defense_iv,
                'Speed IV': speed_iv,
                'Sp. Attack IV': sp_attack_iv,
                'Sp. Defense IV': sp_defense_iv,
                'Is Egg': bool(is_egg),
                'Ability Number': 2 if ability_number else 1
            }
    except (FileNotFoundError, IOError) as e:
        print(f"Error reading genetic info: {e}")
        return {
            'HP IV': 0,
            'Attack IV': 0,
            'Defense IV': 0,
            'Speed IV': 0,
            'Sp. Attack IV': 0,
            'Sp. Defense IV': 0,
            'Is Egg': False,
            'Ability Number': 1
        }

def get_nature(personality_value):
    try:
        return personality_value % 25
    except TypeError as e:
        print(f"Error determining nature: {e}")
        return 'Unknown'

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

def format_pokemon_data(filename, data):
    output = []
    output.append(f"=== {filename} ===")
    output.append(f"General Info:")
    output.append(f"  Personality Value: {data['Personality Value']}")
    output.append(f"  Nature: {data['Nature']}, Is Shiny: {data['Is Shiny']}")
    output.append(f"  Nickname: {data['Nickname']}")
    output.append(f"  Language: {data['Language']}")
    output.append(f"  Level: {data['Level']}")
    output.append(f"  Experience: {data['Experience']}, Friendship: {data['Friendship']}")
    output.append(f"Trainer Info:")
    output.append(f"  OT ID: {data['Trainer']['OT ID (Decimal)']}")
    output.append(f"  OT Name: {data['Trainer']['OT Name']}")
    output.append(f"  Misc Flags: {data['Trainer']['Misc Flags']}")
    output.append(f"Stats:")
    output.append(f"  HP: {data['Stats']['HP']}, Attack: {data['Stats']['Attack']}, Defense: {data['Stats']['Defense']}, Speed: {data['Stats']['Speed']}, Sp. Attack: {data['Stats']['Sp. Attack']}, Sp. Defense: {data['Stats']['Sp. Defense']}")
    output.append(f"  Species: {data['Species']}, Item Held: {data['Item Held']}")
    output.append(f"  IVs - HP: {data['IVs']['HP IV']}, Attack: {data['IVs']['Attack IV']}, Defense: {data['IVs']['Defense IV']}, Speed: {data['IVs']['Speed IV']}, Sp. Attack: {data['IVs']['Sp. Attack IV']}, Sp. Defense: {data['IVs']['Sp. Defense IV']}")
    output.append(f"  EVs - HP: {data['EVs']['HP EV']}, Attack: {data['EVs']['Attack EV']}, Defense: {data['EVs']['Defense EV']}, Speed: {data['EVs']['Speed EV']}, Sp. Attack: {data['EVs']['Sp. Attack EV']}, Sp. Defense: {data['EVs']['Sp. Defense EV']}")
    output.append(f"Moves:")
    output.append(f"  Moves: {data['Moves']}")
    output.append(f"  PP Values: {data['PP Values']}")
    output.append(f"Condition:")
    output.append(f"  Pokerus: Days Left: {data['Condition']['Pokerus Days Left']}, Strain: {data['Condition']['Pokerus Strain']}")
    output.append(f"  Markings: {data['Condition']['Markings']}")
    output.append(f"Origin Info:")
    output.append(f"  Met Location: {data['Origin Info']['Met Location']}")
    output.append(f"  Gender: {data['Origin Info']['Gender']}, Ball: {data['Origin Info']['Ball']}, Game of Origin: {data['Origin Info']['Game of Origin']}, Met Type: {data['Origin Info']['Met Type']}")
    output.append(f"  Is Egg: {data['Origin Info']['Is Egg']}, Ability Number: {data['Origin Info']['Ability Number']}")
    output.append(f"Contest Stats:")
    output.append(f"  Coolness: {data['Contest Stats']['Coolness']}, Beauty: {data['Contest Stats']['Beauty']}, Cuteness: {data['Contest Stats']['Cuteness']}, Smartness: {data['Contest Stats']['Smartness']}, Toughness: {data['Contest Stats']['Toughness']}, Feel: {data['Contest Stats']['Feel']}")
    output.append("\n")
    return "\n".join(output)

def export_to_json(filename, data, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        json_path = os.path.join(output_dir, f"{filename}.json")
        with open(json_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except (FileNotFoundError, IOError) as e:
        print(f"Error exporting to JSON: {e}")

def process_pk3_files(directory, charmap, output_dir, moves):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.endswith('.pk3'):
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
                moves_set = read_move_set(file_path, moves)  # Use the move names here
                pp_values = read_pp_values(file_path)
                ev_and_contest_stats = read_ev_and_contest_stats(file_path)
                pokerus_status = read_pokerus_status(file_path)
                met_location = read_met_location(file_path)
                origin_info = read_origin_info(file_path)
                genetic_info = read_genetic_info(file_path)
                nature = get_nature(personality_value)
                shiny = is_shiny(ot_id, personality_value)

                # Create a data dictionary
                data = {
                    'Personality Value': f'{personality_value:08X}' if personality_value is not None else 'Unknown',
                    'Nature': nature if nature != 'Unknown' else 'Unknown',
                    'Is Shiny': shiny if shiny is not None else False,
                    'Nickname': nickname,
                    'Language': language,
                    'Level': level,
                    'Experience': experience,
                    'Friendship': friendship,
                    'Trainer': {
                        'OT ID (Decimal)': ot_id if ot_id is not None else 'Unknown',
                        'OT Name': ot_name,
                        'Misc Flags': misc_flags if misc_flags is not None else {}
                    },
                    'Stats': {
                        'HP': hp,
                        'Attack': attack,
                        'Defense': defense,
                        'Speed': speed,
                        'Sp. Attack': sp_attack,
                        'Sp. Defense': sp_defense
                    },
                    'IVs': {
                        'HP IV': genetic_info['HP IV'],
                        'Attack IV': genetic_info['Attack IV'],
                        'Defense IV': genetic_info['Defense IV'],
                        'Speed IV': genetic_info['Speed IV'],
                        'Sp. Attack IV': genetic_info['Sp. Attack IV'],
                        'Sp. Defense IV': genetic_info['Sp. Defense IV']
                    },
                    'EVs': {
                        'HP EV': ev_and_contest_stats['HP EV'],
                        'Attack EV': ev_and_contest_stats['Attack EV'],
                        'Defense EV': ev_and_contest_stats['Defense EV'],
                        'Speed EV': ev_and_contest_stats['Speed EV'],
                        'Sp. Attack EV': ev_and_contest_stats['Sp. Attack EV'],
                        'Sp. Defense EV': ev_and_contest_stats['Sp. Defense EV']
                    },
                    'Moves': moves_set,
                    'PP Values': pp_values,
                    'Condition': {
                        'Pokerus Days Left': pokerus_status['Pokerus Days Left'],
                        'Pokerus Strain': pokerus_status['Pokerus Strain'],
                        'Markings': ', '.join(markings)
                    },
                    'Origin Info': {
                        'Met Location': met_location,
                        'Gender': origin_info['Gender'],
                        'Ball': origin_info['Ball'],
                        'Game of Origin': origin_info['Game of Origin'],
                        'Met Type': origin_info['Met Type'],
                        'Is Egg': genetic_info['Is Egg'],
                        'Ability Number': genetic_info['Ability Number']
                    },
                    'Contest Stats': {
                        'Coolness': ev_and_contest_stats['Coolness'],
                        'Beauty': ev_and_contest_stats['Beauty'],
                        'Cuteness': ev_and_contest_stats['Cuteness'],
                        'Smartness': ev_and_contest_stats['Smartness'],
                        'Toughness': ev_and_contest_stats['Toughness'],
                        'Feel': ev_and_contest_stats['Feel']
                    }
                }

                # Make sure species and item held are included
                if species is not None:
                    data['Species'] = species
                if item_held is not None:
                    data['Item Held'] = item_held

                # Print formatted data to the console
                print(format_pokemon_data(filename, data))

                # Export to JSON
                export_to_json(os.path.splitext(filename)[0], data, output_dir)
            
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

# Load the moves from the CSV
moves_csv_path = 'moves.csv'  # Path to your moves.csv file
moves = load_moves(moves_csv_path)

# Load the character map
charmap = load_charmap(CHARMAP_PATH)

# Process the files, print the formatted output, and export to JSON
process_pk3_files(DIRECTORY, charmap, OUTPUT_DIR, moves)
