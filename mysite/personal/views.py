from django.shortcuts import render
from account.models import Account

# Create your views here.

def home_screen_view(request):
    context = {}
    
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    
    
    
    
    # context['some_string'] = "This is some string that i am passing to the view."
    # context['some_number'] = "4849161894 some number that i am passing to the view."

    # context = { 
    #     'some_string' : "This is some string that i am passing to the view.",
    #     'some_number' : "4849161894 some number that i am passing to the view.",
    # }

    # list_of_values = []
    # list_of_values.append("First")
    # list_of_values.append("Second")
    # list_of_values.append("Third")
    # list_of_values.append("Forth")
    # context['list_of_values'] = list_of_values

    # questions = Question.objects.all()
    # context['questions'] = questions

    # return render(request, "personal/home.html", context)