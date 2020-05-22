from django.shortcuts import render
from cards.card_handler import loadCards

# Create your views here.

def home(request):
    suspects, weapons, rooms = loadCards()
    print(suspects)
    return render(request, 'clue_bot/home.html')