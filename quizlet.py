# Purpose: Use the Quizlet API to return info about card sets, based on the
# user request.
# Authors: Riley Rettig
# Date: January 17, 2018

import requests
import json
import jinja2, webbrowser, os
import codecs
from requests.auth import HTTPBasicAuth
from sys import exit
from VocabList import *

def askAuth():
    baseURL = "https://quizlet.com/authorize"
    params = {
    "scope":"write_set",
    "client_id":"sNtZu7YJaJ",
    "response_type":"code",
    "state":"RANDOM_STRING"
    }
    URL = requests.get(baseURL, params=params).url
    #Open URL page to ask for permission
    webbrowser.open(URL)


def getAuth(redirectedURL):
    splitURL = redirectedURL.split("code=")
    
    #if the authorization is denied the program will exit
    if len(splitURL)!=2:
        print ("Error: Access Denied")
        exit()
    else:
        authCode = splitURL[1][:-1]
    return authCode


def requestToken(code):
    baseURL = "https://api.quizlet.com/oauth/token"
    params = {
    "grant_type": "authorization_code",
    "code" : code,
    "redirect_uri":"https://rileyrettig.wordpress.com/",
    }
    r = requests.post(baseURL, auth=HTTPBasicAuth('sNtZu7YJaJ', '2Y8pMwHKvuBAAUtzdFWRNS'), params=params)
    # Convert given JSON string to a dictionary
    resultsDict = json.loads(r.content)
    print (resultsDict.keys())
    # returns the access token
    return resultsDict['access_token']
    

def requestSet(setNum):
    """Prepares the request for the Web API and checks the returned response.
    If the response status code is 200, prints 'We got a response from the 
    API!' and returns the content part of the response as a string. 
    Otherwise, prints the status code, reason, and text of the response, 
    returning None. 
    """
    baseURL = "https://api.quizlet.com/2.0/sets/" + setNum + "?client_id=sNtZu7YJaJ&whitespace=1"

    httpResp = requests.get(baseURL)

    # Print the URL, in case you want to copy it
    # to run in the browser and explore the results there
    print ('API URL Requested: ' + httpResp.url + '\n')

    # Pass
    if httpResp.status_code == 200:
        print ("We got a response from the API!\n")
        return httpResp.content
    # Fail
    else:
        print (httpResp.status_code, httpResp.reason, httpResp.text)
        
def writeJSONforExploration(jsonData, filename):
    """Write results as JSON to explore them."""
    with open(filename, 'w') as fw:
        json.dump(jsonData, fw, sort_keys= True, indent=2)
        
def createSet(accessToken, title, terms, defs): #returns true is successful and false if not
    url = "https://api.quizlet.com/2.0/sets"
    params = {
	"title": title,
	"terms[]": terms,
	"definitions[]": defs,
	"lang_terms" : "en",
	"lang_definitions" : "en"}
	
    headers = {
    "Authorization" : 'Bearer {}'.format(accessToken)
    
    }
    httpResp = requests.post(url,params=params, headers=headers)
    if httpResp.status_code == 201:
        print ("Set was created!\n")
        return True
        #return httpResp.content
    # Fail
    else:
        print (httpResp.status_code, httpResp.reason, httpResp.text)
        return False

        
def main():
    #Get Authorization code
    askAuth()
    #get the  authorization code from URL
    response = input("Redirected URL +1 decoy character?\n") #manually input the URL (figure out how to include on website later)
    authCode = getAuth(response)
    print(authCode)
    
    #Get access token to be used in all user-authenticated calls
    token = requestToken(authCode)
    # print(token)
    
    #Access token for Tuesday April 17 (use for testing)
    #token = "XjwuryxHy4zrvwd7hpFj8JzcRHed9mkBkbztBYBp"
    
    title = input("Title of set?\n")
    vocab = VocabList()
    terms = vocab.terms
    defs = vocab.defs

    createSet(token, title, terms, defs)
    
    
    
if __name__ == '__main__':
    main()