"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import index, post_detail, post_create, post_update, post_delete
from users.views import register, user_login, account, account_update
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('post/<int:id>', post_detail, name = "post_detail"),
    path('post/create/', post_create, name = "post_create"),
    path('post/update/<int:id>', post_update, name = "post_update"),
    path('post/delete/<int:id>', post_delete, name = "post_delete"),
    path('register/', register, name = "register"),
    path('login/', user_login, name = "user_login"),
    path('logout/', LogoutView.as_view(next_page = "index"), name = "logout"),
    path('account/<int:id>',account, name = "account"),
    path('account/update/<int:id>', account_update, name = "account_update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)