from django.shortcuts import render
from django.http import JsonResponse
from random import choice

# Base index page here
def index(request):
    return render(request, 'index.html')

# Have to determine game running view func
def play(request):
    user_hand = request.GET.get('hand', None)
    cpu_hand = choice(['rock','scissors','paper'])
    result = game_rules(user_hand, cpu_hand),
    print(type(user_hand), type(cpu_hand)),
    return JsonResponse({'result': result, 'cpu_hand': cpu_hand})

# Janken rules func
def game_rules(user_hand, cpu_hand):
    win_cases = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
    
    if user_hand == cpu_hand:
        return 'draw'
    elif (user_hand, cpu_hand) in win_cases:
        return 'win'
    else:
        return 'lose'
    


