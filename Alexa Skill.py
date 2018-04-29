from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/webEditor")


def get_input():
    pass


@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like the news?'
    return question(welcome_message)


@ask.intent("colorIntent")
def color():
    return statement("Changed color to red")


if __name__ == "__main__":
    app.run(debug=True)

