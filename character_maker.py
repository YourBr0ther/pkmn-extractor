import json

def load_pokemon_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def create_character_card(pokemon_data):
    personality = pokemon_data.get('Nature')
    friendship = pokemon_data.get('Friendship', 0)
    nickname = pokemon_data.get('Nickname', 'Unknown')
    species = pokemon_data.get('Species', 'Unknown Species')
    trainer = pokemon_data.get('Trainer', {}).get('OT Name', 'Unknown Trainer')
    stats = pokemon_data.get('Stats', {})
    moves = pokemon_data.get('Moves', [])
    pokedex_entries = pokemon_data.get('Additional Data', {}).get('pokedex_entries', [])

    # Generic behavior based on available data
    behavior = f"{nickname} is a {species} with a nature that influences its personality. "
    
    if friendship >= 200:
        behavior += "It is very close to its trainer and responds positively to affection. "
    else:
        behavior += "It seems to have a neutral or distant attitude towards its trainer. "

    if 'Speed' in stats and stats['Speed'] > 15:
        behavior += "It’s quick and agile, often hard to catch. "
    if 'Attack' in stats and stats['Attack'] > 15:
        behavior += "It’s strong and tends to be assertive in battles. "
    if 'Sp. Attack' in stats and stats['Sp. Attack'] > 15:
        behavior += "It has a powerful special attack, making it a formidable opponent. "

    character_card = {
        "name": nickname,
        "species": species,
        "personality": behavior.strip(),
        "trainer": trainer,
        "moves": moves,
        "pokedex_entries": pokedex_entries,
        "stats": stats,
        "is_shiny": pokemon_data.get("Is Shiny", False),
        "level": pokemon_data.get("Level", 1)
    }

    return character_card

def trade_to_real_world(character_card):
    intro = f"{character_card['name']} has just been traded from the Pokémon world to the real world!"
    intro += f"\nTrainer: {character_card['trainer']}"
    intro += f"\nSpecies: {character_card['species']}"
    intro += f"\nLevel: {character_card['level']}"
    intro += f"\nIs Shiny: {'Yes' if character_card['is_shiny'] else 'No'}"
    intro += f"\nBehavior: {character_card['personality']}"
    
    # Add flavor text based on Pokédex entries
    if character_card['pokedex_entries']:
        intro += f"\n\nPokédex Entries:\n" + "\n".join(character_card['pokedex_entries'])

    return intro

file_path = r'.\exported_pokemon\Pikachu.json'  # This should be updated to the path of any Pokémon's JSON file
pokemon_data = load_pokemon_data(file_path)
character_card = create_character_card(pokemon_data)
real_world_intro = trade_to_real_world(character_card)

print(real_world_intro)


