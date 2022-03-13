from django.shortcuts import render
from . import translate

# Create your views here.

def translatorView(request):
    if request.method == 'POST':
        input = request.POST['inp']
        output = translate.translate(input) 
        return render(request, 'translator.html', {'inp': input, 'out': output})
    else: 
        return render(request, 'translator.html')