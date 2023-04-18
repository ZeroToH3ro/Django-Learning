from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyDV9FKEHD2pPIAYrTCqLGfF6XkCAbJ4Ij8",

    'authDomain': "django-firebase-7e6ba.firebaseapp.com",

    'projectId': "django-firebase-7e6ba",

    'storageBucket': "django-firebase-7e6ba.appspot.com",

    'messagingSenderId': "1096115685930",

    'appId': "1:1096115685930:web:66c94ea76a6e695bafd153",

    'measurementId': "G-1C7SZ9KNB7"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def signIn(request):
    return render(request, "signIn.html")

def postSign(request):
    return render(request, "welcome.html")