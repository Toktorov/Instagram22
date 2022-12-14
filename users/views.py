import re
from django.shortcuts import redirect, render
from users.models import User, UserFollow
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
    follow_status = UserFollow.objects.filter(from_user=request.user, to_user=user).exists()
    if request.method == "POST":
        if 'follow' in request.POST:
            user = User.objects.get(id = id)
            try:
                user = UserFollow.objects.get(from_user=request.user, to_user = user)
                user.delete()
                user = User.objects.get(id = id)
                return redirect('account', user.id)
            except:
                
                UserFollow.objects.create(from_user=request.user, to_user = user)
                return redirect('account', user.id)
        
    context = {
        'user' : user,
        'follow_status' : follow_status
    }
    return render(request, 'my_account.html', context)

def account_update(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        profile_image = request.FILES.get('profile_image')
        user = User.objects.get(id = id)
        user.username = username 
        user.last_name = last_name 
        user.first_name = first_name 
        user.email = email 
        user.phone = tel 
        user.profile_image = profile_image
        user.save() 
        return redirect('account', user.id)
    context = {
        'user' : user
    }
    return render(request, 'account_update.html', context)

def account_delete(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        user = User.objects.get(id = id)
        user.delete()
        return redirect('index')
    context = {
        'user' : user
    }
    return render(request, 'account_delete.html', context)

def account_followers(request, id):
    user = User.objects.get(id = id)
    context = {
        'user' : user
    }
    return render(request, 'user_followers.html', context)

def account_following(request, id):
    user = User.objects.get(id = id)
    context = {
        'user' : user
    }
    return render(request, 'user_following.html', context)