# Created Manually

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text

    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)

    if removepunc == "on":
    
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {
            'purpose' : 'Remove Punctuation',
            'analyzed_text' : analyzed
        }

        # Analyze The Text

        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")














# def removepunc(request):
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze The Text
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")

# def charcount(request):
#     return HttpResponse("char count")