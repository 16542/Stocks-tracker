# Stock News Alert System 📈📧

A Python application that monitors Tesla (TSLA) stock price changes and automatically sends email alerts when the price fluctuates by more than 5% between consecutive trading days, along with the latest news articles about the company.

## Features

- 🔍 **Real-time Stock Monitoring**: Fetches daily stock data using Alpha Vantage API
- 📊 **Price Change Detection**: Calculates percentage change between consecutive trading days
- 📧 **Email Notifications**: Sends formatted email alerts when price changes exceed threshold
- 📰 **News Integration**: Fetches and includes latest company news from NewsAPI
- 🔺🔻 **Visual Indicators**: Uses emoji indicators for price direction (up/down)

## How It Works

1. **Stock Data Retrieval**: The application fetches Tesla's daily stock data from Alpha Vantage API
2. **Price Analysis**: Compares yesterday's closing price with the day before yesterday
3. **Threshold Check**: If the price change exceeds 5%, it triggers the alert system
4. **News Fetching**: Retrieves the top 3 latest news articles about Tesla from NewsAPI
5. **Email Alert**: Sends separate emails for each news article with stock performance and news details

## Prerequisites

Before running this application, you need:

- Python 3.7+
- Gmail account with App Password enabled
- Alpha Vantage API key (free at [alphavantage.co](https://www.alphavantage.co/support/#api-key))
- NewsAPI key (free at [newsapi.org](https://newsapi.org/register))

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd stock-news-hard-start
   ```

2. **Install required packages**:
   ```bash
   pip install requests
   ```

3. **Create environment file**:
   Create a file named `env.py` in the project directory with the following content:
   ```python
   STOCK_API_KEY = "your_alpha_vantage_api_key"
   NEWS_API_KEY = "your_newsapi_key"
   EMAIL_PASSWORD = "your_gmail_app_password"
   SENDER_EMAIL = "your_email@gmail.com"
   ```

## Gmail Setup

To send emails, you need to set up Gmail App Passwords:

1. Enable 2-Factor Authentication on your Gmail account
2. Go to Google Account settings → Security → App passwords
3. Generate a new app password for "Mail"
4. Use this app password in the `EMAIL_PASSWORD` field in `env.py`

## Configuration

You can customize the following settings in `main.py`:

- **Stock Symbol**: Change `STOCK = "TSLA"` to monitor different stocks
- **Company Name**: Update `COMPANY_NAME = "Tesla Inc"` for news search
- **Price Threshold**: Modify the percentage threshold in the condition `if diff_percent > 5:`
- **Email Recipients**: Update recipient email in the `send_email()` function

## Usage

Run the application:

```bash
python main.py
```

The application will:
1. Display the current and previous day's closing prices
2. Calculate and show the percentage change
3. If the change exceeds 5%, fetch news and send email alerts
4. Print confirmation messages for each email sent

## Email Format

Each email alert includes:
- Stock symbol and percentage change with direction indicator
- News headline
- Brief description of the article

Example:
```
TSLA: 🔻6%
Headline: Tesla Reports Strong Q3 Earnings
Brief: Tesla Inc reported better-than-expected earnings for the third quarter...
```

## API Limits

- **Alpha Vantage**: 5 API requests per minute, 500 per day (free tier)
- **NewsAPI**: 1,000 requests per month (free tier)

## Project Structure

```
stock-news-hard-start/
├── main.py          # Main application file
├── env.py           # Environment variables (not tracked by git)
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## Error Handling

The application includes error handling for:
- API request failures
- Invalid JSON responses
- SMTP connection issues
- Email encoding problems

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Security Notes

- Never commit the `env.py` file to version control
- Use environment variables or secure secret management in production
- Regularly rotate your API keys and app passwords

## Future Enhancements

Potential improvements:
- Support for multiple stocks
- Database storage for historical tracking
- Web dashboard for monitoring
- Slack/Discord integration
- Technical analysis indicators
- SMS notifications

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This application is for educational purposes only. It should not be used as the sole basis for investment decisions. Always consult with financial advisors before making investment choices.

---

**Made with ❤️ and Python**
