# BOT TELEGRAM

**Bot_Telegram.py**

This one is just a test, it includes a very simple code to make a simple bot.

**Bot_Telegram_DonTorrent.py**

This one send you automatic notifications about the latest updates on Don Torrent website, and send personalized notification to registered users.
Categories:
  - Movies SD
  - Movies HD
  - Movies 4K
  - TV Series SD
  - TV Series HD
  - Documentaries
    
**Bot_Telegram_DonTorrent_register.py**
    
Manages the registration of users who wants to recieve updates.

***Features***:
  - Scraping Updates: Extract info about new movies,series,documentaries from specific Don Torrent endpoints.
  - User notifications: Send the scraped updates to all registered users.
  - Session management with Tor: Ensure anonymity using Tor for web scraping.
  - Users Registration: Allows users to register or unregister from the notification list.
    
  ***Requirements***:
  - Python 3.x
  - Tor service installed
  - Install required Python libraries:
  - Telethon
  - Beautifulsoup4
  - Requests
  - Python-telegram-bot[socks]

