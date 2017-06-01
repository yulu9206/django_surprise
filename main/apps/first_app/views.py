from django.shortcuts import render,redirect
from random import shuffle
VALUES = ['flipper','pyragravure','overage','sanguicolous','convulsed','ectopic','archegonium','wrinkleless','paraments','rgenise']
def index(request):
    return render(request, 'first_app/index.html')
def form_process(request):  
    request.session['pick'] = request.POST['pick']
    global VALUES 
    shuffle(VALUES)
    return redirect('/surprises')
def surprises(request):
    num = int(request.session['pick'])
    context = {
      'surprises': VALUES[0: num]
    }
    return render(request, 'first_app/surprises.html', context)  
