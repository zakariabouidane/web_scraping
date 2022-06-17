import whois

url = input('Enter site name : ')
info = whois.whois(url)
print(info)