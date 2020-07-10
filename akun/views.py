from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfileInfo

def is_recruiter(self):
    if str(self.name) == 'Recruiter':
        return True
    else:
        return False
    
rec_login_required = user_passes_test(lambda u: True if u.is_recruiter else False, login_url='/')

def recruiter_login_required(view_func):
    decorated_view_func = login_required(rec_login_required(view_func), login_url='/')
    return decorated_view_func

def index(request):
    if request.user.is_authenticated:
        print("login")
        dt = UserProfileInfo.objects.filter(user=request.user.id).first()
        data = {
            'bio': dt
        }
        return render(request,'akun/index.html',data)
    # print(dt.foto_profil)
    return render(request,'akun/index.html')

@recruiter_login_required
def special(request):
    print(user_type)
    return HttpResponse("You are logged in !")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'foto_profil' in request.FILES:
                print('found it')
                profile.foto_profil = request.FILES['foto_profil']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'akun/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'akun/login.html', {})
# Create your views here.
