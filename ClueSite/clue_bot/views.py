from django.shortcuts import render
from clue_bot.cards.card_handler import loadCards

# Create your views here.

def home(request):
    #suspects - list of class cards that contain the suspects
    #weapons - list of class cards that contain the suspects
    #rooms - list of class cards that contain the suspects
    suspects, weapons, rooms = loadCards()
    



    return render(request, 'clue_bot/home.html')