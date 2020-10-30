#coding utf-8

import cgi
import http.cookies
import os
import sys
import codecs

#permet de mettre les accents par exemple
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())




#import http.cookies
import datetime

expiration = datetime.datetime.now() + datetime.timedelta(days = 365)
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")




my_cookie = http.cookies.SimpleCookie()

my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["httponly"] = True
my_cookie["pref_lang"]["expires"] = expiration

print(my_cookie.output())



print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Cookies avec Python </h1>
</body>
    <p>Il était une fois...</p>
</hmtl>
"""
print(html)

try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print("La langue choisie par l'utilisateur est :", user_lang["pref_lang"].value)

except(http.cookies.CookieError, KeyError):
    print("Non trouvé")