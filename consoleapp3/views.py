import re
import requests
from django.shortcuts import render
from urllib.request import urlopen
import json

def start(request):
    return render(request, 'console_main.html')

def about(request):
    return render(request, 'console_about.html')