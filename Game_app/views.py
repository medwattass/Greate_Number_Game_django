from django.shortcuts import render, redirect
import random


def root(request):
    if not 'number' in request.session:
        request.session['number'] = random.randint(1,100)
    if not 'guessed' in request.session:
        request.session['guessed'] = 2
    if 'guess_attempts' not in request.session:
        request.session['guess_attempts'] = 0
    
    return render(request, 'index.html')


def destroy_session(request):
    del request.session['number']
    del request.session['guessing']
    del request.session['guessed']
    del request.session['guess_attempts']
    return redirect('/')


def guessing(request):
    request.session['guessing'] = int(request.POST['guessing'])
    request.session['guess_attempts'] += 1
    if request.session['guess_attempts'] < 5:
        if request.session['guessing'] == request.session['number']:
            request.session['guessed'] = 0
        elif request.session['guessing'] > request.session['number']:
            request.session['guessed'] = 1
        else:
            request.session['guessed'] = -1
    else:
        request.session['guessed'] = -2

    return redirect('/')