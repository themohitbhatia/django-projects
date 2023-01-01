from django.shortcuts import render
from django.http import HttpResponse

def menuitems(request, dish):
    items = {
        'pasta': 'pasta description',
        'Falafel': 'Falafel description',
        'cheesecake': 'cheesecake description'
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>"  + description)