from django.shortcuts import redirect, render
from .models import signup
from django.contrib import messages

# Create your views here.
def HOME_Main_Page(request):
    return render(request, 'main.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def newuser(request):
    if request.method == 'GET':
        return render(request, 'newuser.html')
    
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        signup.objects.create(name=name, email=email, password=password, mobile=mobile, address=address, photo=photo)
        return render(request, 'newuser.html', {'message':name+ ' signup successfully!'})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
          try:
             email = request.POST.get('email')
             password = request.POST.get('password')
             user = signup.objects.get(email=email, password=password)
             request.session['username'] = user.name
             request.session['emailid'] = user.email
             return redirect('dashboard')
          except signup.DoesNotExist:
                     messages.error(request,'Invalid email or password')
                     return render(request,'login.html') 

def Dashboard(request):
    if "username" in request.session and "emailid" in request.session:
        name = request.session["username"]
        email = request.session["emailid"]
        return render(request,'dashboard.html', {'username': name, 'emailid': email})
    else:
         messages.error(request,'Please login to access the dashboard')
    return render(request,'login.html')    

def logout(request):
     request.session.clear()
     messages.error(request,'You have been logged out successfully')
     return redirect('login')

def changepassword(request):
    if "username" in request.session and "emailid" in request.session:
        if request.method == 'GET':
            return render(request, 'changepassword.html')
        else:
            try:
                email = request.POST.get('email')
                current_password = request.POST.get('current_password')
                new_password = request.POST.get('new_password')
                confirm_password = request.POST.get('confirm_password')
                
                # Verify email and current password
                user = signup.objects.get(email=email, password=current_password)
                
                # Check if new passwords match
                if new_password != confirm_password:
                    messages.error(request, 'New passwords do not match!')
                    return render(request, 'changepassword.html')
                
                # Update password
                user.password = new_password
                user.save()
                messages.success(request, 'Password changed successfully!')
                return redirect('dashboard')
            except signup.DoesNotExist:
                messages.error(request, 'Invalid email or current password!')
                return render(request, 'changepassword.html')
    else:
        messages.error(request, 'Please login to change password')
        return redirect('login')