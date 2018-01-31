from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rango.models import Category   #starting to put in ordered pages
from rango.models import Page

def index (request):    #Responsible for the main page view
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    #  Retrieve the top 5 only - or all if less than 5.
    #  Place the list in our context_dict dictionary
    #  that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5] #Order by method - descending order
    context_dict = {'categories': category_list}
    #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}


    return render(request, 'rango/index.html', context = context_dict)
   #return HttpResponse("Rango says hey there partner! ")

def about(request):
##
    #context_dict = { 'Rango says here is the about page.'}

    return HttpResponse("Rango  says here is the about page. <a href='/rango/'>View index page</a>")  #The HTML link is a reference back to the starter page
<<<<<<< HEAD

=======
<<<<<<< HEAD:rango/views.py
>>>>>>> 73f47a3d8b2bd0cbb42b6221925de510406ae607

def show_category (request, category_name_slug):
# Create a context dictionary which we can pass
#  to the template rendering engine.
    context_dict = {}

    try:
    # Can we find a category name slug with the given name?
    #  If we can't, the .get() method raises a DoesNotExist exception.
    #  So the .get() method returns one model instance or raises an exception

        category = Category.objects.get(slug=category_name_slug)

    # Retrieve all of the associated pages.
    # Note that filter() will return a list of page objects or an empty list

        pages = Page.objects.filter(category=category)

    # Adds our results list to the template context under name pages.

        context_dict['pages'] = pages

    # We also add the category object from
    # the database to the context dictionary.
    # We'll use this in the template to verify that the category exists.

        context_dict['category'] = category

    except Category.DoesNotExist:
    # We get here if we didn't find the specified category.
    # Don't do anything
    # the template will display the "no category" message for us

        context_dict ['category'] = None
        context_dict ['pages'] = None

    # Go render the response and return it to the client

    return render(request, 'rango/category.html', context_dict)
<<<<<<< HEAD

=======
=======
>>>>>>> d9087ff183b901744eb70f92da5a3f29a9167b04:tango_with_django_project/rango/views.py
>>>>>>> 73f47a3d8b2bd0cbb42b6221925de510406ae607
