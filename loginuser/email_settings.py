# -*- coding: utf-8 -*-

SITE_ADDRESS= '127.0.0.1:8000'

EMAIL_ADDRESS = 'a.szymanski.pb@gmail.com'
EMAIL_PASSWORD = '123Tymczasowe'

EMAIL_SMTP = 'smtp.gmail.com'
EMAIL_SMTP_PORT = 587

EMAIL_SUBJECT = 'Potwierdzenie rejestracji - E-Wybory'
EMAIL_MESSAGE = """\
<html>
  <head></head>
  <body>
    <h2>Potwierdzenie rejestracji</h2>
    Aby potwierdzić swoje konto wejdź na podany link: 
    <a href="http://""" + SITE_ADDRESS + """/auth/register/{0}/{1}">kliknij tutaj</a>.
    <br><br>------------------------------------<br>
    Wiadomość wygenerowana automatycznie, proszę na nią nie odpowiadać.
  </body>
</html>
"""
