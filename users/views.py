from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
	if request.method == 'POST': #if we are trying to use post method
		form = UserRegisterForm(request.POST) #creates a form with the post data
		if form.is_valid(): #checks valid when submitted
			form.save()
			username = form.cleaned_data.get('username') #gets the username of the valid data
			messages.success(request, f'Your account has been created! You are now able to login')
			return redirect('login')
	else:
		form = UserRegisterForm() #creates an empty form
	return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user) #instance shows current username and image filled in
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid(): #save info if valid
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user) 
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)
