"""quizlet.py
Purpose: Use the Quizlet API to create a new card deck from User's input.

Authors: Riley Rettig
Date created: January 17, 2018
Date last edited: April 30 2017
"""

import os
from sys import exit
import json
import webbrowser
import codecs

import jinja2
import requests
from requests.auth import HTTPBasicAuth

from VocabList import *

BASE_URL_AUTH = "https://quizlet.com/authorize"
BASE_URL_TOKEN = "https://api.quizlet.com/oauth/token"
CLIENT_ID = "sNtZu7YJaJ"
REDIRECT_URI = "https://rileyrettig.wordpress.com/"
SECRET_KEY = "2Y8pMwHKvuBAAUtzdFWRNS"
TERM_LANGUAGE = "en"
DEF_LANGUAGE = "en"


def ask_auth():
    params = {
        "scope": "write_set",
        "client_id": CLIENT_ID,
        "response_type": "code",
        "state": "RANDOM_STRING"
        }
    url = requests.get(BASE_URL_AUTH, params=params).url
    # Open URL page to ask for permission
    webbrowser.open(url)


def get_auth(redirected_url):
    split_url = redirected_url.split("code=")

    # If the authorization is denied the program will exit
    if len(split_url) != 2:
        auth_code = none
        print("Error: Access Denied")
        exit()
    else:
        auth_code = split_url[1][:-1]
    return auth_code


def get_token(code):
    params = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        }
    r = requests.post(
        BASE_URL_TOKEN,
        auth=HTTPBasicAuth(CLIENT_ID, SECRET_KEY),
        params=params
        )
    # Convert given JSON string to a dictionary
    results_dict = json.loads(r.content)
    # returns the access token
    return results_dict['access_token']

        
def create_set(access_token, title, terms, definitions):
    """Returns true if set creation is successful and false if not"""
    url = "https://api.quizlet.com/2.0/sets"
    params = {
        "title": title,
        "terms[]": terms,
        "definitions[]": definitions,
        "lang_terms": TERM_LANGUAGE,
        "lang_definitions": DEF_LANGUAGE
        }
    headers = {"Authorization": 'Bearer {}'.format(access_token)}
    http_resp = requests.post(url, params=params, headers=headers)
    if http_resp.status_code == 201:
        print("Set was created!\n")
        return True
    else:
        print(http_resp.status_code, http_resp.reason, http_resp.text)
        return False

        
def main():
    ask_auth()

    """Get the  authorization code from the returned URL, include a space or
    other decoy character so that a web page is not opened
    """
    response = input("Redirected URL +1 decoy character?\n")
    auth_code = get_auth(response)
    token = get_token(auth_code)
    title = input("Title of set?\n")

    """Use a VocabList Object to hold terms and definitions."""
    vocab = VocabList()
    terms = vocab.terms
    definitions = vocab.defs

    create_set(token, title, terms, definitions)

    
if __name__ == '__main__':
    main()