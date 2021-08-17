from django.shortcuts import render
from http.server import BaseHTTPRequestHandler
from datetime import datetime

def home(request):
    return render(request, 'home/home.html')

