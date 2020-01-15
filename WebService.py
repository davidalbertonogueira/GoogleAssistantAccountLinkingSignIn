#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, request, render_template, flash, redirect
from flask_assistant import Assistant, ask
from flask_assistant import profile, sign_in
from flask_assistant import session_id, user, storage
from flask_assistant import request as assistant_request, context_manager,  event, storage


import json
import uuid

app = Flask(__name__)


with open("private.json", encoding='utf-8') as private_json:
    private_data = json.load(private_json)

app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']
app.config['AOG_CLIENT_ID'] = private_data['AOG_CLIENT_ID'] #CLIENT_ID OBTAINED BY SETTING UP ACCOUNT LINKING IN AOG CONSOLE # https://console.actions.google.com/u/0/ + Selecting the action > Develop > Account Linking


assist = Assistant(app=app, route="/", project_id=private_data['project_id']) #PROJECT ID OBTAINED IN 1) https://dialogflow.cloud.google.com/ > Select Agent > Settings > General > GOOGLE PROJECT > 'Project ID' OR 2) GOOGLE CLOUD CONSOLE: https://console.cloud.google.com/home/dashboard

@assist.action("Default Welcome Intent")
def welcome():
    print("Default Welcome Intent")
    print("Request: ", request)
    print("assistant_request: ", assistant_request)

    if profile:
        print("Profile: ", profile)
    if session_id:
        print("session_id: ",session_id)
    if user:
        print("user: ",user)
    if storage:
        print("storage: ",storage)
    
    output_message = ""

    if profile:
        output_message+=f"Welcome back {profile['name']}. "
    else:
        output_message+="Hi! I'm your Authentication Tester app. It's a pleasure! Remember, if you want to authenticate, please say 'I want to sign in\". "
    
    if user:
        if user.get('userStorage') is None or len(user['userStorage'])==0 :
            output_message += "Looks like you're new here. "
            user['userStorage'] = {}
            uid = uuid.uuid4()
            user['userStorage']['ID'] = str(uid)
            output_message += "I've given you the following ID: " + user['userStorage']['ID'] + " . "
        
        elif user['userStorage'].get('ID') is not None:
            last_seen = user['lastSeen']
            output_message += ("Welcome back " + 
                user['userStorage']['ID'] + 
                " ! Haven't seen you since "+ last_seen + ".")

    return ask(output_message)

@assist.action("Start-Sign-In")
def start_sign_in():
    print("Start-Sign-In")
    print("Request: ", request.data)
    print("assistant_request: ", assistant_request)
    return sign_in("Sure! Let's do it! To learn more about you")

# this intent must have the actions_intent_SIGN_IN event
# and will be invoked once the user has 
@assist.action("Complete-Sign-In")
def complete_sign_in():
    print("Complete-Sign-In")
    print("Request: ", request)
    print("assistant_request: ", assistant_request)
    if profile:
        return ask(f"Welcome aboard {profile['name']}, thanks for signing up!")
    else:
        return ask("Hope you sign up soon! Would love to get to know you!")


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5000, 
            threaded=True,
            debug=True)
