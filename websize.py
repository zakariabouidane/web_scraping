import webbrowser
#from selenium import webdriver

url = input('Enter site name : ')
ws = webbrowser.open('https://www.google.com/search?q=site '+url)