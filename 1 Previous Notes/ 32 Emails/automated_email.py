##################### Normal Starting Project ######################
import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = "cambrightjosh@gmail.com"
PASSWORD = "Nolee123"

today = datetime.now()
today_tuple = (today.month, today.day)

quote = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in quote.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    print("match")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"subject: Happy Birthday\n\n {contents}")
else:
    print("match not found")

