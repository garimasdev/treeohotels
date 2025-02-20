import traceback
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, UserRole


def register(request):
    role_id = request.GET.get('role')
    role = UserRole.objects.get(user_type=role_id)
    if request.method == 'POST':
        try:
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                messages.error(request, "Passwords do not match!")
                return redirect('signup')

            try:
                role = UserRole.objects.get(user_type=role_id)
            except UserRole.DoesNotExist:
                messages.error(request, "Invalid user role selected.")
                return redirect('signup')

            User.objects.create_user(
                email=email,
                first_name=full_name,
                phone=phone,
                password=password,
                role=role
            )

            messages.success(request, "Account created! Please log in.")
            return redirect('login')
        except:
            traceback.print_exc()

    return render(request, 'signup.html')




def login(request):
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     user = authenticate(request, email=email, password=password)

    #     if user:
    #         login(request, user)
    #         messages.success(request, "Logged in successfully!")
    #         return redirect('db-dashboard')
    #     else:
    #         messages.error(request, "Invalid email or password.")

    return render(request, 'login.html')



def logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')


