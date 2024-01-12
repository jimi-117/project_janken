"""
Define 7 functions bellow to make view which to realise janken game appli:
- signup_view : register user
- login_view : to login
- logout_view : to logout
- janken_view : janken gameplay
- index_view : to display user info who logined
- user_view : to display other user info
- ranking_view : to display ranking
"""
# Create your views here.

from django.shortcuts import render, redirect, get_list_or_404
from .forms import SignupUserForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import random

User = get_user_model()

def signup_view():
    if request.method == 'POST':
        form = SignupUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            return redirect(to='/janken_app/')
        
    else:
        form = SignupUserForm()
    
    param = {
        'form' : form
    }
    
    return render(request, 'janken_app/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            
            if user:
                login(request,user)
                return redirect(to='/janken_app/')
            
        else:
            form = LoginForm()
        
        param = {
            'form' : form
        }
        
        return render(request, 'janken_app/login.html', param)
    
@login_required
def ranking_view(request):
    users = User.objects.order_by('-win_rate')
    params = {
        'users' : users
    }
    return render(request, 'janken_app/ranking.html', params)

@login_required
def user_view(request, id=0):
    other = get_list_or_404(User, id=id)
    
    params= {
        'user' : request.user,
        'other' : other
    }
    return render(request, 'janken_app/user.html', params)

@login_required
def janken_view(request):
    if request.method == 'POST':
        com_hand = random.choice(('stone', 'scissors', 'paper'))
        player_hand = request.POST.get('hand')
        
        player = player.play(player_hand, com_hand)
        player.save()
        
        params = {
            'user' : request.user,
            'result' : result,
            'player_hand' : player_hand,
            'com_hand' : com_hand
        }
        return render(request, 'janken_app/result.html', params)
    else:
        params = {
            'user' : request.user
        }
        return render(request, 'janken_app/janken.html', params)