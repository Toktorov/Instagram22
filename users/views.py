from django.shortcuts import redirect, render
from users.models import User
from django.contrib.auth import login, authenticate
from posts.models import Post

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            user = User.objects.create(username = username, first_name = first_name, last_name = last_name, email = email, phone = phone, profile_image = profile_image)
            user.set_password(password)
            user.save()
            return redirect('user_login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('index')
    return render(request, 'login.html')

def account(request, id):
    user = User.objects.get(id = id)
    context = {
        'user' : user,
    }
    return render(request, 'my_account.html', context)