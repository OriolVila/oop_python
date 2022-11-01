import yagmail
import pandas as pd
import datetime
import time

from news import NewsFeed


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         to_date=today,
                         from_date=yesterday)
    email = yagmail.SMTP(user="YOUR_EMAIL@gmail.com",
                         password="YOUR_PASSWORD")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']}!  \n \
                        See what's on about {row['interest']} today. \n\n \
                        {news_feed.get()} \
                        \n Oriol",
               attachments="design.txt"
               )


while True:
    if datetime.datetime.now().hour == 22 and datetime.datetime.now().minute == 29:
        df = pd.read_excel('people.xlsx')
        df = df.iloc[:3, :4]

        for index, row in df.iterrows():
            send_email()
    time.sleep(60)


