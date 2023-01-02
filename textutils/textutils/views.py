# Created Manually

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    params = {}


    # REMOVE PUNCTUATIONS

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

        djtext = analyzed


    # CAPITALIZE

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {
            'purpose' : 'Changed to Uppercase',
            'analyzed_text' : analyzed
        }

        djtext = analyzed

    
    # NEW LINE REMOVER

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char

        params = {
            'purpose' : 'Removed New Lines',
            'analyzed_text' : analyzed
        }

        djtext = analyzed


    # EXTRA SPACE REMOVER

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {
            'purpose' : 'Removed Extra Spaces',
            'analyzed_text' : analyzed
        }

        djtext = analyzed

        if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
            return HttpResponse("No Operation Selected!")

    return render(request, 'analyze.html', params)
