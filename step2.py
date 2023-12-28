from pokemontcgsdk import Card

# Get all cards (will take awhile, automatically pages through data)
cards = Card.all()

# Get a single page of cards
cards = Card.where(page=1, pageSize=250)

# Filter cards via query parameters
cards = Card.where(q='set.name:generations subtypes:mega')

# Order by release date (descending)
cards = Card.where(q='subtypes:mega', orderBy='-set.releaseDate')

print(cards)