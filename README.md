
## Overview

This is a tutorial/sample project that demostrates how to create a webserver for a Google Assistant action with Account Linking via Google Sign in.


## Installation

### Requirements
The required libraries are listed in `requirements.txt`.

### Setting up a virtual environment
Linux  | Windows
------------- | -------------
pip install virtualenv  | pip install virtualenv
virtualenv --python /usr/bin/python3.6 venv	  | virtualenv venv
source venv/bin/activate  | venv\Scripts\activate.bat
pip install -r requirements.txt  | pip install -r requirements.txt 



## Configuration before running
Please edit the file private.json, with your "AOG_CLIENT_ID" and "project_id".

The "AOG_CLIENT_ID" is the "CLIENT_ID" that can be obtained by setting up Account Linking in the AOG Console: 
https://console.actions.google.com/u/0/ + Selecting the action > Develop > Account Linking"


The "project_id" can be obtained: 
1) in the Dialogflow platform (https://dialogflow.cloud.google.com/) going to > Select Agent > Settings > General > GOOGLE PROJECT > 'Project ID' or 
2) in the Google Cloud Console : https://console.cloud.google.com/home/dashboard


## Running
To run, just do:

```
python WebService.py


``` 

