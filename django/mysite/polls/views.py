from django.shortcuts import render
import pyrebase

config = {
  "apiKey": "AIzaSyCby-voeyDPj5CaaH33OJFdRjCMZF45jKs",
  "authDomain": "django-fb531.firebaseapp.com",
  "projectId": "django-fb531",
  "storageBucket": "django-fb531.firebasestorage.app",
  "messagingSenderId": "5279372713",
  "appId": "1:5279372713:web:2de9975b2423ef0c7b20b8"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
def home(request):
    return render(request, "polls/home.html")
def login(request):
    return render(request, "polls/login.html")

def verify_login(request):
    account = request.POST.get('account', '')
    password = request.POST.get('password', '')
    ischecked = request.POST.get('ischecked', '')
    print('***', account, password, ischecked)
    try:
        user = auth.sign_in_with_email_and_password(account, password)
        print('user', user)
        return render(request, "polls/home.html")
    except:
        print('*** login failed')
        return render(request, "polls/login.html", {'error': 'Login failed. Please check your credentials.'})

# Create your views here.
