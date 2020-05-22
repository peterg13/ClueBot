from django.shortcuts import render
from clue_bot.cards.card_handler import loadCards

# Create your views here.

def home(request):
    suspects, weapons, rooms = loadCards()
    print(suspects[0].getName())
    return render(request, 'clue_bot/home.html')