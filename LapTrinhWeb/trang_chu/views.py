from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless=new")
webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
webdriver.get("https://github.com/Majestymo/IDM-Activation-Script-Coporton")
html_code = webdriver.page_source

def index(request):
    return render(request, (html_code))
