from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from urllib.parse import quote
import requests

import logging
logger = logging.getLogger(__name__)

# Keycloak auth configuration: 
# working link: https://profile.miem.hse.ru/auth/realms/MIEM/protocol/openid-connect/auth?response_type=code&client_id=3D-print&scope=openid%20email&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2F

KEYCLOAK_URL = "https://profile.miem.hse.ru/auth/"
REALM = "MIEM"
PROTOCOL = "openid-connect"
CODE_ACQUIRING_ENDPOINT = "auth" # This endpoint is used for getting authentication code from MIEM Keycloak instance
CODE_EXCHANGE_ENDPOINT = "token" # This endpoint is used for acquiring access, refresh tokens
USERINFO_ENDPOINT = "userinfo" # This endpoint is used for acquiring userinfo
END_SESSION_ENDPOINT = "logout" # This endpoint is used for logging out
NEXT_URL = '/' # Needed for redirecting to the specific page
CLIENT_ID = "3D-print" # ID given by MIEM Keycloak instance admins
CLIENT_SECRET = "15df4b08-7f55-438c-89a1-9bea709b69f2" # Secret given by MIEM Keycloak instance
REDIRECT_URI = "http://127.0.0.1:8000/oauth2/login/redirect" # Code will be sent to this uri
RESPONSE_TYPE = "code" 
SCOPES = "openid offline_access profile"
GRANT_TYPE = "authorization_code" # Standart auth flow 

LINK_TEMPLATE = KEYCLOAK_URL + 'realms/' + REALM + '/protocol/' + PROTOCOL + '/'

# def home(request: HttpRequest) -> JsonResponse:
#     return JsonResponse({ "msg": "Hello World" })

# @login_required(login_url='/oauth2/login')
# def get_authenticated_user(request: HttpRequest):
#     print(request.user)
#     user = request.user
#     return JsonResponse({
#       "id": user.id,
#       "discord_tag": user.discord_tag,
#       "avatar": user.avatar,
#       "public_flags": user.public_flags,
#       "flags": user.flags,
#       "locale": user.locale,
#       "mfa_enabled": user.mfa_enabled
#     })

def keycloak_login(request: HttpRequest):
    global next_url # TODO: Глупая вещь, переделать 
    try:
        next_url = request.GET['next']
        print(next_url)
    except Exception:
        print('No next parameter, rederecting to the main page...')
        next_url = '/'
    query = 'response_type=' + RESPONSE_TYPE + '&' + 'client_id=' + CLIENT_ID + '&' + 'scope=' + quote(SCOPES) + '&' + 'redirect_uri=' + quote(REDIRECT_URI) # Building query for auth endpoint
    link_auth = LINK_TEMPLATE + CODE_ACQUIRING_ENDPOINT + '?' + query # Building auth endpoint url
    logger.debug("Current user auth endpoint url: " + link_auth)
    return redirect(link_auth)

@login_required
def keycloak_logout(request: HttpRequest): # TODO: реализовать revoke токена при логауте
    print('Logging out...')
    logout(request)
    print('Redirecting to the main page...')
    return redirect('/')


def keycloak_login_redirect(request: HttpRequest):
    code = request.GET.get('code') # Getting code from MIEM Keycloak instance response
    logger.debug("Current user auth code: " + code)
    
    # Getting user info via access token 
    user = exchange_code(code)

    # Validating user (TODO: нужна модернизация)
    if user != None:
        miem_user = authenticate(request, user=user)
    else: 
        print('invalid_request, redirecting to the main page...')
        return redirect('/?error=access_denied') # Для реализации всплывающего алерта с просьбой залогиниться еще раз
        
    try:
        miem_user = list(miem_user).pop()
    except TypeError:
        print(miem_user)

    login(request, miem_user)

    return redirect(next_url)

def exchange_code(code: str):
    # Building payload for POST request
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": GRANT_TYPE,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    # Adding headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    link = LINK_TEMPLATE + CODE_EXCHANGE_ENDPOINT # Building url for token endpoint
    response = requests.post(url=link, data=data, headers=headers) # Getting desired tokens
    print(response.json())

    try:
        # Getting user info with acquired tokens from Keycloak
        credentials = response.json()
        access_token = credentials['access_token']
        response = requests.get(LINK_TEMPLATE + USERINFO_ENDPOINT, headers={
          'Authorization': 'Bearer %s' % access_token
        })

        user = response.json()
        print(user)

        return user 
    
    except Exception: # Error response.json()['error'] == 'invalid_request'
        return None