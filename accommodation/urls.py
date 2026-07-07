from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Student
    path(
        'student/dashboard/',
        views.student_dashboard,
        name='student_dashboard'
    ),

    # Landlord
    path(
        'landlord/dashboard/',
        views.landlord_dashboard,
        name='landlord_dashboard'
    ),

    path(
        'landlord/add-room/',
        views.add_room,
        name='add_room'
    ),

    path(
        'landlord/my-rooms/',
        views.landlord_rooms,
        name='landlord_rooms'
    ),

    path(
    'landlord/delete-room/<int:pk>/',
    views.delete_room,
    name='delete_room'
    ),

    # Rooms
    path(
        'rooms/',
        views.room_list,
        name='room_list'
    ),

    path(
        'rooms/<int:pk>/',
        views.room_detail,
        name='room_detail'
    ),

    # Contact
    path(
        'rooms/<int:pk>/contact/',
        views.contact_landlord,
        name='contact_landlord'
    ),
]
