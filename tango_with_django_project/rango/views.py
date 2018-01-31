from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rango.models import Category

def index (request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    #  Retrieve the top 5 only - or all if less than 5.
    #  Place the list in our context_dict dictionary
    #  that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}


    return render(request, 'rango/index.html', context = context_dict)
   #return HttpResponse("Rango says hey there partner! ")

def about(request):
##
    #context_dict = { 'Rango says here is the about page.'}

    return HttpResponse("Rango  says here is the about page. <a href='/rango/'>View index page</a>")  #The HTML link is a reference back to the starter page
