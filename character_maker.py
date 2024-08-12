import json
import os
import requests
import base64
import struct
import zlib

def load_pokemon_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def determine_friendship_level(friendship):
    if friendship >= 255:
        return "Inseparable"
    elif friendship >= 235:
        return "Very Close"
    elif friendship >= 215:
        return "Best Friends"
    elif friendship >= 195:
        return "Close"
    elif friendship >= 175:
        return "Friendly"
    elif friendship >= 155:
        return "Neutral"
    elif friendship >= 135:
        return "Distant"
    elif friendship >= 115:
        return "Aloof"
    elif friendship >= 95:
        return "Wary"
    elif friendship >= 75:
        return "Distrustful"
    elif friendship >= 55:
        return "Suspicious"
    else:
        return "Hostile"

def download_sprite(species_number, save_path):
    url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{species_number}.png"
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded sprite for species {species_number}")
    else:
        print(f"Failed to download sprite for species {species_number}")

def create_character_card(pokemon_data):
    nickname = pokemon_data.get('Nickname', None) or pokemon_data.get('Species', {}).get('Name', 'Unknown Species')
    trainer = "{{user}}"
    
    species_name = pokemon_data.get('Species', {}).get('Name', 'Unknown Species')
    species_number = pokemon_data.get('Species', {}).get('Number', '0')
    met_location = pokemon_data.get('Origin Info', {}).get('Met Location', 'Unknown Location')
    friendship = pokemon_data.get('Friendship', 0)
    level = pokemon_data.get('Level', 1)
    age = max(level, 18)  # Set minimum age to 18
    nature = pokemon_data.get('Nature', 'Unknown Nature')
    gender = pokemon_data.get('Origin Info', {}).get('Gender', 'Unknown Gender')
    met_type = pokemon_data.get('Origin Info', {}).get('Met Type', 'Unknown Type')
    stats = pokemon_data.get('Stats', {})
    moves = pokemon_data.get('Moves', [])
    pokedex_entries = pokemon_data.get('Additional Data', {}).get('pokedex_entries', [])

    friendship_level = determine_friendship_level(friendship)
    
    personality = f"Based on its {nature} nature, {nickname} is likely to be "
    if nature.lower() == "adamant":
        personality += "bold and confident, often taking initiative in battles."
    else:
        personality += "a unique individual with a personality shaped by its experiences."

    if 'Speed' in stats and stats['Speed'] > 15:
        personality += " It’s quick and agile, often hard to catch."
    if 'Attack' in stats and stats['Attack'] > 15:
        personality += " It’s strong and assertive in battles."
    if 'Sp. Attack' in stats and stats['Sp. Attack'] > 15:
        personality += " It has a powerful special attack, making it a formidable opponent."

    character_card = {
        "name": nickname,
        "species": species_name,
        "species_number": species_number,
        "personality": personality.strip(),
        "trainer": trainer,
        "met_location": met_location,
        "friendship_level": friendship_level,
        "level": age,  # Using adjusted age here
        "gender": gender,
        "met_type": met_type,
        "moves": moves,
        "pokedex_entries": pokedex_entries,
        "stats": stats,
        "is_shiny": pokemon_data.get("Is Shiny", False)
    }

    return character_card

def trade_to_real_world(character_card):
    intro = f"{character_card['name']} has just been transferred out of the video game world and into a virtual console where they can interact with their trainer!"
    intro += f"\nTrainer: {character_card['trainer']}"
    intro += f"\nSpecies: {character_card['species']}"
    intro += f"\nLevel (Age): {character_card['level']}"
    intro += f"\nFriendship Level: {character_card['friendship_level']}"
    intro += f"\nGender: {character_card['gender']}"
    intro += f"\nMet Location: {character_card['met_location']}"
    intro += f"\nMet Type: {character_card['met_type']}"
    intro += f"\nIs Shiny: {'Yes' if character_card['is_shiny'] else 'No'}"

    intro += f"\n\n{character_card['name']} can now see, smell, and hear this new world but cannot touch it. The transfer process can be a bit rough, so they might feel a bit confused or disoriented as they wake up and adjust to this new environment."

    intro += f"\nBehavior: {character_card['personality']}"
    
    if character_card['pokedex_entries']:
        intro += f"\n\nPokédex Entries:\n" + "\n".join(character_card['pokedex_entries'])

    return intro

def encode_json_to_base64(json_data):
    json_str = json.dumps(json_data)
    base64_str = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    return base64_str

def create_png_with_embedded_json(input_png_path, output_png_path, base64_json_str):
    with open(input_png_path, 'rb') as f:
        png_data = f.read()

    # Split the PNG into chunks
    chunks = []
    i = 8  # PNG header is 8 bytes, start after that
    while i < len(png_data):
        length = struct.unpack('>I', png_data[i:i+4])[0]
        chunk_type = png_data[i+4:i+8]
        chunk_data = png_data[i+8:i+8+length]
        crc = struct.unpack('>I', png_data[i+8+length:i+12+length])[0]
        chunks.append((chunk_type, chunk_data, crc))
        i += length + 12

    # Create new tEXt chunk with the embedded JSON data
    tEXt_chunk_type = b'tEXt'
    tEXt_chunk_data = b'chara\x00' + base64_json_str.encode('utf-8')
    tEXt_crc = zlib.crc32(tEXt_chunk_type + tEXt_chunk_data) & 0xffffffff
    tEXt_chunk = (tEXt_chunk_type, tEXt_chunk_data, tEXt_crc)

    # Insert the tEXt chunk after the IHDR chunk (which is always the first chunk)
    chunks.insert(1, tEXt_chunk)

    # Reassemble the PNG
    with open(output_png_path, 'wb') as f:
        f.write(png_data[:8])  # PNG header
        for chunk_type, chunk_data, crc in chunks:
            f.write(struct.pack('>I', len(chunk_data)))
            f.write(chunk_type)
            f.write(chunk_data)
            f.write(struct.pack('>I', crc))

    print(f"Character card saved as {output_png_path} with embedded JSON data")

def export_to_sillytavern(character_card, file_name, image_file):
    # Prepare character card data
    card_data = {
        "data": {
            "alternate_greetings": [],
            "avatar": image_file,  # Link to the sprite image
            "character_version": "1.0",
            "creator": "Pokémon Import Script",
            "creator_notes": "",
            "description": trade_to_real_world(character_card),
            "extensions": {
                "chub": {
                    "alt_expressions": {},
                    "expressions": None,
                    "full_path": f"Pokémon/{character_card['species']}",
                    "id": 0,
                    "related_lorebooks": []
                },
                "depth_prompt": {
                    "depth": 4,
                    "prompt": "",
                    "role": "system"
                },
                "fav": False,
                "talkativeness": "0.5",
                "world": ""
            },
            "first_mes": f"*{character_card['name']} awakens, disoriented, in a strange new environment.*\n\n'Where am I? What happened?' \n\n*The surroundings are unfamiliar, but there's a comforting presence nearby.*",
            "mes_example": "<START>",
            "name": character_card["name"],
            "personality": character_card["personality"],
            "post_history_instructions": "",
            "scenario": "The Pokémon was transferred into a virtual console where they can interact with their trainer, but cannot touch anything.",
            "system_prompt": "",
            "tags": [],
            "group_only_greetings": []
        },
        "spec": "chara_card_v3",
        "spec_version": "3.0",
        "name": character_card["name"],
        "fav": False,
        "description": trade_to_real_world(character_card),
        "personality": character_card["personality"],
        "scenario": "The Pokémon was transferred into a virtual console where they can interact with their trainer, but cannot touch anything.",
        "first_mes": f"*{character_card['name']} awakens, disoriented, in a strange new environment.*\n\n'Where am I? What happened?' \n\n*The surroundings are unfamiliar, but there's a comforting presence nearby.*",
        "mes_example": "<START>",
        "talkativeness": "0.5",
        "tags": [],
        "chat": "",
        "create_date": "",
        "creatorcomment": "",
        "avatar": image_file
    }
    
    # Encode the character card data to base64
    base64_json_str = encode_json_to_base64(card_data)
    
    # Embed the JSON into the PNG file
    create_png_with_embedded_json(image_file, file_name + ".png", base64_json_str)

def process_pokemon_files(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(input_dir, filename)
            pokemon_data = load_pokemon_data(file_path)
            character_card = create_character_card(pokemon_data)
            
            # Determine the file name based on the nickname or species name
            sprite_name = character_card['name'].replace(" ", "_")
            sprite_path = os.path.join(output_dir, f"{sprite_name}.png")
            
            # Download the sprite
            species_number = character_card.get('species_number', '0')
            download_sprite(species_number, sprite_path)
            
            # Export to SillyTavern format with embedded JSON
            export_to_sillytavern(character_card, os.path.join(output_dir, sprite_name), sprite_path)

# Define the input and output directories
input_dir = r'D:\Scripts\pkmn-extractor\exported_pokemon'
output_dir = r'D:\Scripts\pkmn-extractor\pokemon_character_cards'

# Process all Pokémon JSON files
process_pokemon_files(input_dir, output_dir)
