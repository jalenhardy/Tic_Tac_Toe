
from bs4 import BeautifulSoup
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import paramiko
import sys
import os
import re

app = Flask(__name__)
ask = Ask(app, "/webEditor")
id = 0
text = ""

def connect_to_website(url):
    os.system("cd Docments/umbcHack/resume-April-24-2018")

def get_input():
    pass


@ask.launch
def start_skill():
    welcome_message = 'Hello there, would you like to edit your website'
    return question(welcome_message)


@ask.intent("AMAZON.YesIntent")
def yes():
    return statement("Ok, editing your website")


@ask.intent("AMAZON.NoIntent")
def no():
    return statement("I do not know why you called me")


@ask.intent('AddIDIntent', mapping={'idNumber': 'idTag'})
def addId(idNumber):
    id = idNumber
    edit_html(text, id)
    return statement("Ok")

@ask.intent('AddTextIntent', mapping={'textValue': 'text'})
def addText(textvalue):
    text = textvalue
    print(text)
    return question("What id would you like to append?")


@ask.intent('updateIntent')
def connectserver():
    SSH_ADDRESS = 'address for server'
    SSH_ADDRESS = "username to server here"
    SSH_PASSWORD = "password to server here"
    SSH_COMMAND = "mkdir test"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_stdin = ssh_stdout = ssh_stderr = None
    try:
        ssh.connect(SSH_ADDRESS, username=SSH_USERNAME, password=SSH_PASSWORD)
    except Exception as e:
        sys.stderr.write("SSH Connection error: {0}".format(e))
    if ssh_stdout:
        sys.stdout.write(ssh_stdout.read())
    if ssh_stderr:
        sys.stderr.write(ssh_stderr.read())              
    return statment("Update Complete")

def edit_html(text, idNumber):
    with open('index.html', 'r+') as file:
        file = file.read()
        soup = BeautifulSoup(file, "html5lib")  
    tag = soup.find(id=idNumber)
    print(tag)
    print(text)
    tag.append(text)
    print(tag)
       
if __name__ == "__main__":
    app.run()
