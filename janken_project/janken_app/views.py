from django.shortcuts import render
from django.http import JsonResponse
from random import choice

# Base index page here
def index(request):
    return render(request, 'index.html')

# Janken rules func
def game_rules(user_hand, cpu_hand):
    if user_hand == cpu_hand:
        return 'draw'
    elif (user_hand == 'rock' and cpu_hand == 'scissors') or \
            (user_hand == 'scissors' and cpu_hand == 'paper') or \
            (user_hand == 'paper' and cpu_hand == 'rock'):
        return 'win'
    else:
        return 'lose'
    
# Have to determine game running view func
def play(request):
    user_hand = request.GET.get('hand', None),
    cpu_hand = choice(['rock','scissors','paper'])
    result = game_rules(user_hand, cpu_hand),
    return JsonResponse({'result': result, 'cpu_hand': cpu_hand})

