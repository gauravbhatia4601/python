from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm
from .models import Users
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Get the username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            
            # Hash the password before saving it
            hashed_password = Users.hash_password(password)
            
            # Create a new user instance with hashed password
            user = Users(username=username, password=hashed_password, email=email)
            user.save()
            
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if username in users:
                # Get the hashed password from the database
                hashed_password = users[password]

                # Verify the provided password against the hashed password
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                    return redirect('login')
                else:
                    return jsonify({'error': 'Invalid password'}), 401
            else:
                return jsonify({'error': 'User not found'}), 404
            # Redirect to dashboard or show error message
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')