from pokemontcgsdk import Card
import json

def convert_to_serializable(obj):
    if isinstance(obj, Card):
        return obj.__dict__
    elif hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return str(obj)

# Get all cards (will take a while, automatically pages through data)
cards = Card.all()

# Convert cards to a list of dictionaries
card_data = []
for card in cards:
    card_data.append(card)

# Write the data to a JSON file
with open('pokemon_cards.json', 'w') as json_file:
    json.dump(card_data, json_file, default=convert_to_serializable, indent=2)

print("Data has been written to 'pokemon_cards.json'")
