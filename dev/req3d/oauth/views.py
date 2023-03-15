from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import requests

# Create your views here.

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=1084965843827437688&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify%20email"
next_url = '/'
CLIENT_ID = '1084965843827437688'
CLIENT_SECRET = 'pqU0GJ_nUWc4AnLVwuoZkbt_xeKVNkJr'
redirect_url = "http://127.0.0.1:8000/oauth2/login/redirect"

# def home(request: HttpRequest) -> JsonResponse:
#   return JsonResponse({ "msg": "Hello World" })

@login_required(login_url='/oauth2/login')
def get_authenticated_user(request: HttpRequest):
  print(request.user)
  user = request.user
  return JsonResponse({
    "id": user.id,
    "discord_tag": user.discord_tag,
    "avatar": user.avatar,
    "public_flags": user.public_flags,
    "flags": user.flags,
    "locale": user.locale,
    "mfa_enabled": user.mfa_enabled
  })

def discord_login(request: HttpRequest):
  global next_url
  try:
    next_url = request.GET['next']
    print(next_url)
  except Exception:
    print('No next param')
  return redirect(auth_url_discord)

def discord_login_redirect(request: HttpRequest):
  code = request.GET.get('code')
  print(code)
  user = exchange_code(code)
  discord_user = authenticate(request, user=user)
  try:
      discord_user = list(discord_user).pop()
  except TypeError:
      print(discord_user)

  print(discord_user)
  login(request, discord_user)
  return redirect(next_url)

def exchange_code(code: str):
  data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_url,
    "scope": "identify email"
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
  print(response)
  credentials = response.json()
  access_token = credentials['access_token']
  response = requests.get("https://discord.com/api/v6/users/@me", headers={
    'Authorization': 'Bearer %s' % access_token
  })
  print(response)
  user = response.json()
  print(user)
  return user