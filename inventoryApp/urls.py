from django.urls import path

from inventoryApp.views import *

urlpatterns = [
    path('', Home, name = 'home'),
    path('display_laptop/', display_laptops, name = 'display_laptops'),
    path('display_desktop/', display_desktops, name = 'display_desktops'),
    path('display_mobile', display_mobiles, name = 'display_mobiles'),
]
