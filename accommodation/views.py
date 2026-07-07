from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile, Room, ContactMessage
from .forms import RegisterForm, LoginForm, RoomForm, ContactForm


# HOME PAGE
def home(request):

    rooms = Room.objects.filter(
        available=True
    ).order_by('-created_at')[:6]

    return render(
        request,
        'home.html',
        {
            'rooms': rooms
        }
    )


# REGISTER
def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password1']
            )

            user.save()

            profile = user.profile

            profile.full_name = form.cleaned_data['full_name']
            profile.phone = form.cleaned_data['phone']
            profile.role = form.cleaned_data['role']

            profile.save()

            messages.success(
                request,
                "Account created successfully"
            )

            return redirect('login')

    else:

        form = RegisterForm()


    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )


# LOGIN
def user_login(request):

    if request.method == "POST":

        form = LoginForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(
                request,
                user
            )

            return redirect('dashboard')

    else:

        form = LoginForm()


    return render(
        request,
        'registration/login.html',
        {
            'form': form
        }
    )


# LOGOUT
def user_logout(request):

    logout(request)

    return redirect('home')


# DASHBOARD ROUTER
@login_required
def dashboard(request):

    if request.user.profile.role == "Student":

        return redirect(
            'student_dashboard'
        )


    else:

        return redirect(
            'landlord_dashboard'
        )


# STUDENT DASHBOARD
@login_required
def student_dashboard(request):

    rooms = Room.objects.filter(
        available=True
    )


    return render(
        request,
        'student_dashboard.html',
        {
            'rooms': rooms
        }
    )


# LANDLORD DASHBOARD
@login_required
def landlord_dashboard(request):

    rooms = Room.objects.filter(
        owner=request.user
    )


    return render(
        request,
        'landlord_dashboard.html',
        {
            'rooms': rooms
        }
    )


# ADD ROOM
@login_required
def add_room(request):

    if request.user.profile.role != "Landlord":

        return redirect('dashboard')


    if request.method == "POST":

        form = RoomForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            room = form.save(commit=False)

            room.owner = request.user

            room.save()


            messages.success(
                request,
                "Room added successfully"
            )


            return redirect(
                'landlord_rooms'
            )

    else:

        form = RoomForm()


    return render(
        request,
        'add_room.html',
        {
            'form': form
        }
    )


# LANDLORD ROOMS
@login_required
def landlord_rooms(request):

    rooms = Room.objects.filter(
        owner=request.user
    )


    return render(
        request,
        'landlord_rooms.html',
        {
            'rooms': rooms
        }
    )


# ALL ROOMS
def room_list(request):

    rooms = Room.objects.filter(
        available=True
    )


    location = request.GET.get('location')

    room_type = request.GET.get('room_type')


    if location:

        rooms = rooms.filter(
            location__icontains=location
        )


    if room_type:

        rooms = rooms.filter(
            room_type=room_type
        )


    return render(
        request,
        'rooms/room_list.html',
        {
            'rooms': rooms
        }
    )


# ROOM DETAIL
def room_detail(request, pk):

    room = get_object_or_404(
        Room,
        id=pk
    )


    return render(
        request,
        'rooms/room_detail.html',
        {
            'room': room
        }
    )


# CONTACT LANDLORD
@login_required
def contact_landlord(request, pk):

    room = get_object_or_404(
        Room,
        id=pk
    )


    if request.method == "POST":

        form = ContactForm(request.POST)


        if form.is_valid():

            message = form.save(
                commit=False
            )

            message.room = room

            message.student = request.user

            message.save()


            messages.success(
                request,
                "Message sent successfully"
            )


            return redirect(
                'room_detail',
                pk=room.id
            )


    else:

        form = ContactForm()


    return render(
        request,
        'rooms/contact_landlord.html',
        {
            'form': form,
            'room': room
        }
    )
@login_required
def delete_room(request, pk):

    room = get_object_or_404(
        Room,
        id=pk,
        owner=request.user
    )

    room.delete()

    messages.success(
        request,
        "Room deleted successfully"
    )

    return redirect(
        'landlord_rooms'
    )
