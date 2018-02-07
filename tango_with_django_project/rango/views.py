from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rango.models import Category   #starting to put in ordered pages
from rango.models import Page
from rango.forms import CategoryForm, PageForm
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index (request):    #Responsible for the main page view
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    #  Retrieve the top 5 only - or all if less than 5.
    #  Place the list in our context_dict dictionary
    #  that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5] #Order by method - descending order
    #context_dict = {'categories': category_list}

    page_list = Page.objects.order_by('-views')[:5] #order by views
    #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    context_dict = {'categories': category_list, 'pages': page_list}
    return render(request, 'rango/index.html', context = context_dict)
   #return HttpResponse("Rango says hey there partner! ")

def about(request):
##
    #context_dict = { 'Rango says here is the about page.'}

    print(request.method)

    print(request.user)

    return render(request, 'rango/about.html',{})

    #return HttpResponse("Rango  says here is the about page. <a href='/rango/'>View index page</a>")  #The HTML link is a reference back to the starter page


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

    return render(request, 'rango/category.html', context_dict )

def add_category(request):
    form = CategoryForm()

    #A HTTP POST?
    if request.method == 'POST': #User submitted data via form
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            #Save the new category to the database
            form.save(commit=True)
            #print(category, category.slug)

            #Now that the category is saved
            #We could give the confirmation message
            #But since the most recent category added is on the Index page
            #Then we can direct the user back to the index page
            return index(request)
        else:
            #The supplied form contained errors -
            #Just print them to the terminal.
            print(form.errors)

        #Will handle the bad form, new form or no form supplied cases
        #Render the form with error messages (if any)
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)

        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
    else:
        ## ON the PDF of tangowithdjango19,the e.g is like that:
        #          else:
        #              print(user_form.errors, profile_form.errors)
        #  	else:
        # user_form = UserForm()
        #      	profile_form = UserProfileForm()

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'rango/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                   })

def user_login(request):
    if request.method == 'POST':
        #POST.get because returns none if not exist
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Check if combo valid
        user = authenticate(username=username, password=password)

        #If we have a user object, details correct
        if user:
            #Account active?
            if user.is_active:
                #valid
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                #Inactive account used
                return HttpResponse("Your Rango account is disabled")
        else:
            #Bad login details provided
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    #Request not in POST, so display login form
    else:
        return render(request, 'rango/login.html', {})

