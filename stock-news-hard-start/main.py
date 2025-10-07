import requests
import datetime as dt
import env
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": env.STOCK_API_KEY,
    "outputsize": "compact"
    
}

def send_email(message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=env.SENDER_EMAIL, password=env.EMAIL_PASSWORD)
        
        # Create properly formatted email message
        msg = MIMEMultipart()
        msg['From'] = env.SENDER_EMAIL
        msg['To'] = env.SENDER_EMAIL
        msg['Subject'] = "Stock Alert!"
        
        # Add message body
        msg.attach(MIMEText(message, 'plain', 'utf-8'))
        
        # Send email
        connection.send_message(msg)


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 


res = requests.get(STOCK_ENDPOINT  , params=params)
res.raise_for_status()
daily_data =res.json()["Time Series (Daily)"]   
data_list = [value for (key, value) in daily_data.items()]
yesterday_data = data_list[0]
yesterday_data_closing_price = yesterday_data["4. close"]
print(yesterday_data_closing_price)
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
if yesterday_data_closing_price > day_before_yesterday_closing_price:
    difference = float(yesterday_data_closing_price) - float(day_before_yesterday_closing_price)
    up_down = "🔺"
else:
    difference = float(day_before_yesterday_closing_price) - float(yesterday_data_closing_price)
    up_down = "🔻"

diff_percent = (difference / float(yesterday_data_closing_price)) * 100
print(f"Price change: {diff_percent:.2f}%")
    



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if diff_percent > 5:  # Temporarily lowered for testing
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": env.NEWS_API_KEY,
    }
    news_res = requests.get(NEWS_ENDPOINT, params=news_params)
    news_res.raise_for_status()
    articles = news_res.json()["articles"]
    three_articles = articles[:3]


## STEP 3: use Email to send a message with the percentage change and each article's title and description to your own email address and then send yourself a separate email for each article.
#HINT 1: Use the format below to send the message.
    formatted_articles = [f'{STOCK}: {up_down}{round(diff_percent)}%\nHeadline: {article["title"]}. \nBrief: {article["description"]}' for article in three_articles]
    print(formatted_articles)
    for article in formatted_articles:
        print(article)
        send_email(article)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

