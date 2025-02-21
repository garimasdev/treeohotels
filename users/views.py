import traceback
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from .models import User, UserRole
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        role_id = request.POST.get('role')
        role = UserRole.objects.get(user_type=role_id)
        try:
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                messages.error(request, "Passwords do not match!")
                return redirect('signup')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect(f'login')

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




def user_login(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.filter(email=email).first()
            # Check if password matches
            if user.check_password(password):
                # user ID in session
                request.session['user_id'] = user.id

                if user.role.user_type == 3:
                    return redirect('dashboard:db-dashboard')
                else: 
                    return redirect('dashboard:db-vendor-dashboard') 
        except:
            traceback.print_exc()
    return render(request, 'login.html')


    # if request.method == 'POST':
    #     try:
    #         email = request.POST.get('username')
    #         password = request.POST.get('password')
    #         print(email,password)
    #         user = authenticate(request, username=email, password=password)
    #         print(user)
    #         if user is None:
    #             print("Authentication failed! User not found.")
    #             return render(request, 'login.html')
    #         login(request, user)
    #         messages.success(request, "Logged in successfully!")
    #         if user.role.user_type == 3:  # Customer
    #             return redirect('index.html')
    #         else:  # Agent or Vendor
    #             return redirect('db-vendor-dashboard')
    #     except:
    #         traceback.print_exc()
    # return render(request, 'login.html')



def logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')


