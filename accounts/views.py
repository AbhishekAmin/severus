from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # save the user with the data taken from the form
            user = form.save()

            # log the newly created user in
            auth_login(request, user)

            # redirect to the home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
