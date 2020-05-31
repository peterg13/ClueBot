from django.shortcuts import render
from clue_bot.cards.card_handler import loadCards

# Create your views here.

def home(request):
    #suspects - list of class cards that contain the suspects
    #weapons - list of class cards that contain the suspects
    #rooms - list of class cards that contain the suspects
    suspects, weapons, rooms = loadCards()

    context = {
    	'suspects': cardsToJSON(suspects),
    	'weapons': cardsToJSON(weapons),
    	'rooms': cardsToJSON(rooms)
    }
  
    return render(request, 'clue_bot/home.html', context)

def cardsToJSON(cards):
	JSONArray = []

	for card in cards:
		JSONArray.append({'name': card.getName()})

	return JSONArray