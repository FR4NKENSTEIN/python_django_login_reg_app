from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

# render my forms
def log_reg(request):
    return render(request, 'login_registration_app/log_reg_form.html')

def success(request):
    try:
        user_id = int(request.session['userid'])
        context = {
            'user_in_session' : User.objects.get(id=user_id)
        }
        print('##############################   SUCCESS!   ##############################')
        return render(request, 'other_app/.html', context)
    except:
        return redirect('/')

def register(request):
    print('##############################   ABOUT TO REGISTER A USER...   ##############################')
    #Ask the validator to find any errors with client input
    errors = User.objects.registerValidator(request.POST)
    #If there are any errors, serve them to the template
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print('##############################   REGISTRATION FAILED   ##############################')
        return redirect('/')
    #Else there are no errors, create the new user
    else:
        password = request.POST['password_reg']
        hashword = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        new_user = User.objects.create(
            first_name = request.POST['first_name_reg'],
            last_name = request.POST['last_name_reg'],
            email = request.POST['email_reg'],
            pw_hash = hashword
            )
        request.session['userid'] = new_user.id
        print('##############################   REGISTERED A NEW USER   ##############################')
        print(f'user {new_user.id} is in session.')
        return redirect('/another_app')

def login(request):
    print('##############################   LOGGING IN...   ##############################')
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print('##############################   LOGIN FAILED   ##############################')
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email_log'])
        request.session['userid'] = user.id
        print('##############################   A USER LOGGED IN   ##############################')
        print(f'user {user.id} is in session.')
        return redirect('/another_app')

def logout(request):
    request.session.clear()
    print('##############################   LOGGED OUT   ##############################')
    return redirect('/')
