import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "EUPDVJWFG0NU7R59"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "6a11a8d0c65e47f2bbc82d9c8a6039d9"

account_sid = "AC9b290ef413b50fac2a355b47cdd26d47"
auth_token = "49325dc076a4f88e558b24b7cb399367"



    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

news_response = requests.get(STOCK_ENDPOINT, params=stock_params)
news_response.raise_for_status()
stock_data= news_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
#print(yesterday_closing_price)

'''
the reason we wanted to do a list comprehension is because for this program to work we need the program to be
dynamic. we will reference the index position instead of the key name to make this happen.
initially i forgot to specify the index ["Time Series (Daily)"] on line 22. I kept getting a keyError on line 25
because ["4. close"] was not listed under the initial tree meta data.
the items() gives not just the item but the key, value pairs in dictionary
'''

#Get the day before yesterday's closing stock price
day_before_data = stock_data_list[1]
day_before_closing_price = float(day_before_data["4. close"])
#print(day_before_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yesterday_closing_price - day_before_closing_price)
#print(difference)
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_change = difference / yesterday_closing_price *100
#print(percent_change)


#. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_change > 5:

    news_params={
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    #print(articles)
    three_articles = articles[:3]
    #print(three_articles)

    #. - Create a new list of the first 3 article's headline and description using list comprehension.
    #[new_item for item in list]
    formatted_articles = [f"Healine: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
# - Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_="+12562902565",
            to="18035421156",
        )
    print(message.status)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

