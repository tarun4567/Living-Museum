"""
URL configuration for Museum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static
from LMuseum import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='WelcomPage'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('extending/',views.ExtendingPage,name='ExtendingPage'),
    path('bengaltiger/',views.BengalTiger,name='BengalTiger'),
    path('elephant/',views.IndianElephant,name='IndianElephant'),
    path('leopard/',views.SnowLeopard,name='SnowLepord'),
    path('lion/',views.AsiaticLion,name='AsiaticLion'),
    path('panda/',views.RedPanda,name='RedPanda'),


    path('extinct/',views.ExtinctPage,name='ExtinctPage'),
    path('auroch/',views.IndianAuroch,name='IndianAuroch'),
    path('rhinoceros/',views.IndianRhinoceros,name='IndianRhinoceros'),
    path('quail/',views.HimalayanQuail,name='HimalayanQuail'),
    path('civet/',views.MalabarCivet,name='MalabarCivet'),
    path('duck/',views.PinkHeadedDuck,name='PinkHeadedDuck'),
    

    path('donation/',views.DonationPage,name='DonationPage'),
    path('list/',views.RegisteredListPage,name='RegisteredListPage'),

    path('feed/', views.feedback_view, name='Feedback'),

        ]


urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




