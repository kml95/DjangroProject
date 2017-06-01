# -*- coding: utf-8 -*-

SITE_ADDRESS= '127.0.0.1:8000'

EMAIL_ADDRESS = 'kamil.tymczasowe@gmail.com'
EMAIL_PASSWORD = 'Haslo123'

EMAIL_SMTP = 'smtp.gmail.com'
EMAIL_SMTP_PORT = 587

EMAIL_SUBJECT = 'Potwierdzenie rejestracji - Fitlife'
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
