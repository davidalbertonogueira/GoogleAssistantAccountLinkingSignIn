#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_assistant import Assistant, ask, profile, sign_in
import json


app = Flask(__name__)


with open("private.json", encoding='utf-8') as private_json:
    private_data = json.load(private_json)

app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']
app.config['AOG_CLIENT_ID'] = private_data['AOG_CLIENT_ID'] #CLIENT_ID OBTAINED BY SETTING UP ACCOUNT LINKING IN AOG CONSOLE # https://console.actions.google.com/u/0/ + Develop + Account Linking


assist = Assistant(app=app, route="/", project_id=private_data['project_id']) #PROJECT ID OBTAINED IN 1) https://dialogflow.cloud.google.com/ > Select Agent > Settings > General > GOOGLE PROJECT > 'Project ID' OR 2) GOOGLE CLOUD CONSOLE: https://console.cloud.google.com/home/dashboard

@assist.action("Default Welcome Intent")
def welcome():
    if profile:
        return ask(f"Welcome back {profile['name']}")
    return ask("Hi! I'm your Auth test App. It's a pleasure. Remember, if you want to authenticate, please say 'I want to sign in\".")

@assist.action("Start-Sign-In")
def start_sign_in():
    return sign_in("Sure! Let's do it! To learn more about you")

# this intent must have the actions_intent_SIGN_IN event
# and will be invoked once the user has 
@assist.action("Complete-Sign-In")
def complete_sign_in():
    if profile:
        return ask(f"Welcome aboard {profile['name']}, thanks for signing up!")
    else:
        return ask("Hope you sign up soon! Would love to get to know you!")


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000, 
            threaded=True,
            debug=True)
