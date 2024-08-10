import os
import csv

def read_personality_value(pk3_file_path):
    with open(pk3_file_path, 'rb') as file:
        personality_value = int.from_bytes(file.read(4), byteorder='little')
        return personality_value

def read_ot_id(pk3_file_path):
    with open(pk3_file_path, 'rb') as file:
        file.seek(0x04)
        ot_id = int.from_bytes(file.read(4), byteorder='little')
        return ot_id

def read_nickname_raw(pk3_file_path):
    with open(pk3_file_path, 'rb') as file:
        file.seek(0x08)
        nickname_raw = file.read(10)
        return nickname_raw

def load_charmap(charmap_path):
    charmap = {}
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
    return charmap

def decode_nickname(nickname_raw, charmap):
    nickname = ''
    for byte in nickname_raw:
        if byte == 0x00 or byte not in charmap:  # Assuming 0x00 is the termination character
            break
        nickname += charmap.get(byte, '?')
    return nickname

def read_language(pk3_file_path):
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

def read_misc_flags(pk3_file_path):
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

def read_ot_name(pk3_file_path, charmap):
    with open(pk3_file_path, 'rb') as file:
        file.seek(0x14)
        ot_name_raw = file.read(7)
        ot_name = decode_nickname(ot_name_raw, charmap)
        return ot_name

def read_markings(pk3_file_path):
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

def read_level(pk3_file_path):
    with open(pk3_file_path, 'rb') as file:
        file.seek(0x54)
        level_byte = int.from_bytes(file.read(1), byteorder='little')
        return level_byte

def read_stat(pk3_file_path, offset):
    with open(pk3_file_path, 'rb') as file:
        file.seek(offset)
        stat_value = int.from_bytes(file.read(2), byteorder='little')
        return stat_value

def read_species(pk3_file_path):
    with open(pk3_file_path, 'rb') as file:
        file.seek(0x20)
        species_value = int.from_bytes(file.read(2), byteorder='little')
        return species_value

def read_item_held(pk3_file_path):
    with open(pk3_file_path, 'rb') as file:
        file.seek(0x22)
        item_held_value = int.from_bytes(file.read(2), byteorder='little')
        return item_held_value

def read_experience(pk3_file_path):
    with open(pk3_file_path, 'rb') as file:
        file.seek(0x24)
        experience_value = int.from_bytes(file.read(4), byteorder='little')
        return experience_value

def read_friendship(pk3_file_path):
    with open(pk3_file_path, 'rb') as file:
        file.seek(0x29)
        friendship_value = int.from_bytes(file.read(1), byteorder='little')
        return friendship_value

def read_move_set(pk3_file_path):
    with open(pk3_file_path, 'rb') as file:
        file.seek(0x2C)  # Corrected offset to 0x2C
        moves = []
        for _ in range(4):
            move_bytes = file.read(2)
            move = move_bytes[0]  # Use only the first byte
            moves.append(move)
        return moves

def process_pk3_files(directory, charmap):
    pokemon_data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.pk3'):
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
            moves = read_move_set(file_path)
            pokemon_data[filename] = {
                'Personality Value': f'{personality_value:08X}',
                'OT ID (Decimal)': ot_id,
                'Nickname': nickname,
                'Language': language,
                'Misc Flags': misc_flags,
                'OT Name': ot_name,
                'Markings': ', '.join(markings),
                'Level': level,
                'HP': hp,
                'Attack': attack,
                'Defense': defense,
                'Speed': speed,
                'Sp. Attack': sp_attack,
                'Sp. Defense': sp_defense,
                'Species': species,
                'Item Held': item_held,
                'Experience': experience,
                'Friendship': friendship,
                'Moves': moves
            }
    return pokemon_data

# Specify the directory where the .pk3 files are located
directory = 'test_pokemon'

# Load the character map
charmap_path = 'charmap.csv'
charmap = load_charmap(charmap_path)

# Process the files and print all the extracted information including the move set
pokemon_data = process_pk3_files(directory, charmap)
for filename, data in pokemon_data.items():
    print(f'{filename}: Personality Value = {data["Personality Value"]}, OT ID (Decimal) = {data["OT ID (Decimal)"]}, Nickname = {data["Nickname"]}, Language = {data["Language"]}, Misc Flags = {data["Misc Flags"]}, OT Name = {data["OT Name"]}, Markings = {data["Markings"]}, Level = {data["Level"]}, HP = {data["HP"]}, Attack = {data["Attack"]}, Defense = {data["Defense"]}, Speed = {data["Speed"]}, Sp. Attack = {data["Sp. Attack"]}, Sp. Defense = {data["Sp. Defense"]}, Species = {data["Species"]}, Item Held = {data["Item Held"]}, Experience = {data["Experience"]}, Friendship = {data["Friendship"]}, Moves = {data["Moves"]}')
