from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ProfileRegistrationForm

def register(request):
    if request.method == 'POST':
        # load the HTTP Request into two forms, for the User, and the Profile
        form = UserCreationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST, request.Files)
        
        # If both forms are valid, we create the User and Profile in the Database
        if form.is_valid() and profile_form.is_valid():
            # Save the User object to DB, by calling dave directly on the Form.
            # Return the User object so that we can use it later to set the user of the Profile
            form.save()
            
            #Get the Profile form the profile_form, without actually saving anything to the Database
            profile_form.save(commit=False)
            
            # Use the User created above to set the user property of the Profile
            profile.user = user
            
            if profile.gender == "M":
            
            # Now we actually save the profile to the Database
                profile.save()
            
            # Now we can log in as the new user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        profile_form = ProfileRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form, 'profile_form': profile_form})