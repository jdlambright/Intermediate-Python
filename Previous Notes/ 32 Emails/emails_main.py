import smtplib
import datetime as dt
import random


now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()
print(year) #year is an int
print(type(now)) #its listed as a class datetime.datetime not number or string

date_of_birth = dt.datetime(year=1995 , month=12 , day=15, hour=4)

if weekday == 0:
    with open("quotes.txt") as quote_file:
        quote_list= quote_file.readlines()
        weekly_quote= random.choice(quote_list)
        print(weekly_quote)


    #this is your email
    my_email = "cambrightjosh@gmail.com"
    password = "Nolee123" #for yahoo app password is  "cczy fkqr qifu rjev"

    #this tells it what server to use and opens and closes it
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:        #yahoo  may need a port   "smtp.mail.yahoo.com"
        #this makes your connection secure
        connection.starttls()
        #this logs in
        connection.login(user=my_email, password=password)
        #this sends the smail.   the 2 \n\n is required to separate subject and content
        connection.sendmail(
            from_addr=my_email,
            to_addrs="cambrightjosh@yahoo.com",
            msg=f"subject: Weekly Quote\n\n {weekly_quote}")


















