import json

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

def create_character_card(pokemon_data):
    nickname = pokemon_data.get('Nickname', None) or pokemon_data.get('Species', {}).get('Name', 'Unknown Species')
    trainer = "{{user}}"
    
    species_name = pokemon_data.get('Species', {}).get('Name', 'Unknown Species')
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

def export_to_sillytavern(character_card, file_name):
    card_data = {
        "data": {
            "alternate_greetings": [],
            "avatar": "none",
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
        "avatar": "none"
    }
    
    with open(file_name, 'w') as file:
        json.dump(card_data, file, indent=4)
    
    print(f"Character card saved as {file_name}")

# Use the correct path for your environment
file_path = r'D:\Scripts\pkmn-extractor\exported_pokemon\Pikachu.json'  # Update this path
pokemon_data = load_pokemon_data(file_path)
character_card = create_character_card(pokemon_data)
export_to_sillytavern(character_card, r'D:\Scripts\pkmn-extractor\pokemon_character_cards\Pikachu_character_card.json')
