from analytics import data, telegrambot

if __name__ == '__main__':
    data = data.Data()
    app = telegrambot.Telegram()
    app.main()