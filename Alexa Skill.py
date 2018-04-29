from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/webEditor")


def get_input():
    pass


@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like to edit your website'
    return question(welcome_message)


@ask.intent("YesIntent")
def yes():
    return statement("Ok, editing your website")


@ask.intent("NoIntent")
def no():
    return statement("I do not know why you called me")


@ask.intent('addIntent')
def add(text, idNumber):
    return question("ok adding {} to id tag {}".format(text, idNumber))


if __name__ == "__main__":
    app.run(debug=True)

