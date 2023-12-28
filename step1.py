from pokemontcgsdk import Card
from config import API_KEY

# Set the API key
Card.api_key = API_KEY

# Example: Fetch a specific card by ID
card_id = 'xy7-54'
card = Card.find(card_id)
print(f"Card ID: {card.id}")
print(f"Card Name: {card.name}")

# Example: Fetch cards based on parameters
cards = Card.where(q='supertype:pokemon subtypes:mega', pageSize=5)
for card in cards:
    print(f"Card Name: {card.name}")

# Example: Fetch all cards with pagination
all_cards = Card.where(page=1, pageSize=10)
for card in all_cards:
    print(f"Card Name: {card.name}")
