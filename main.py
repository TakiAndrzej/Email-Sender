import smtplib
import datetime as dt
from random import choice
import os

my_email = "pythonnzub@gmail.com"
password = os.environ("password")
now = dt.datetime.now()
day = now.weekday()

if day == 1:
    with open('quotes.txt') as file:
        data = file.readlines()
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs='pythonnzub@yahoo.com',
            msg=f"Subject:Motivational quote\n\n{choice(data)}."
        )
