from django.shortcuts import render

# Create your views here.
from .models import User
from .signup_form import UserForm

def index(request):
    return render(request, 'userapp/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    my_dict = {'users': user_list}
    return render(request, 'userapp/users.html', context=my_dict)

def user_signup(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
           form.save(commit=True)
           return users(request)
        else:
            print('Form is invalid')

    return render(request, 'userapp/user_signup.html', {'form': form})
