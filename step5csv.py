from pokemontcgsdk import Card
import csv

class Arrangement:
    def __init__(self, card):
        self.id = card.id
        self.name = card.name
        self.supertype = card.supertype
        self.hp = card.hp
        self.evolvesFrom = card.evolvesFrom
        self.convertedRetreatCost = card.convertedRetreatCost
        self.number = card.number
        self.artist = card.artist
        self.rarity = card.rarity

def get_all_cards_arranged():
    all_cards_arranged = []

    # Fetch all cards
    cards = Card.all()

    for card in cards:
        arranged_card = Arrangement(card)
        all_cards_arranged.append(arranged_card)
    return all_cards_arranged
#The all_cards_arranged list is a collection of instances of the Arrangement class, where each instance represents a card with its attributes

all_arranged_cards = get_all_cards_arranged()

# Save to CSV
csv_file_path = r'C:\Users\amrit\OneDrive\Desktop\InternGBD\API Pull Twitter\pokemon_cards.csv'

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['id', 'name', 'supertype', 'hp', 'evolvesFrom', 'convertedRetreatCost', 'number', 'artist', 'rarity']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for card in all_arranged_cards:
        writer.writerow({
            'id': card.id,
            'name': card.name,
            'supertype': card.supertype,
            'hp': card.hp,
            'evolvesFrom': card.evolvesFrom, 
            'convertedRetreatCost': card.convertedRetreatCost,
            'number': card.number,
            'artist': card.artist,
            'rarity': card.rarity,
        })

print(f"Data has been written to '{csv_file_path}'")
