from django.urls import path

from inventoryApp.views import *

urlpatterns = [
    path('', Home, name = 'home'),

    path('display_laptop/', display_laptops, name = 'display_laptops'),
    path('display_desktop/', display_desktops, name = 'display_desktops'),
    path('display_mobile/', display_mobiles, name = 'display_mobiles'),

    path('add_laptop/', add_laptops, name = 'add_laptops'),
    path('add_desktop/', add_desktops, name = 'add_desktops'),
    path('add_mobile/', add_mobiles, name = 'add_mobiles'),

    path('edit_laptop/<int:pk>', edit_laptops, name = 'edit_laptops'),
    path('edit_desktop/<int:pk>', edit_desktops, name = 'edit_desktops'),
    path('edit_mobile/<int:pk>', edit_mobiles, name = 'edit_mobiles'),

    path('delete_laptop/<int:pk>', delete_laptops, name = 'delete_laptops'),
    path('delete_desktop/<int:pk>', delete_desktops, name = 'delete_desktops'),
    path('delete_mobile/<int:pk>', delete_mobiles, name = 'delete_mobiles'),
]
