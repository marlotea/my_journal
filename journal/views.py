from .models import Profile, Entry
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["password2"]
        
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                
                return redirect('signup')
                
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                
                return redirect('signup')
            
            else:
                try: 
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()

                    #log user in and redirect to settings page
                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)

                    #create a Profile object for the new user
                    user_model = User.objects.get(username=username)
                    new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                    new_profile.save()
                    return redirect('home')
            
                except ValueError as e:
                        print(f"Error creating user: {e}")
                        messages.error(request, 'An error occurred during signup. Please try again.')
                        return redirect('signup')

        
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')

    else: 
        return render(request, 'signup.html')

def login(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
        
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def home(request, pk):
    
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user = user_object)
    entries = Entry.objects.all().order_by('-created_on') 
    # !!!  ^^ Will this be an issue once I have multiple users?
    user_entry_amount = len(entries)
    # user_join_date = 
    
    context = {
        'user_object' : user_object,
        'user_profile' : user_profile,
        'entries' : entries,
        'user_entry_amount' : user_entry_amount
    }
    
    return render(request, 'home.html', context) 
