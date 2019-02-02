import json
from django.conf import settings
from rest_framework import serializers
import requests

def email_deliverable(email):
    verifier_url = 'https://api.hunter.io/v2/email-verifier'
    payload = {'api_key': settings.HUNTER_IO_SECRET_KEY, 'email': email} 
    response = requests.get(verifier_url, params=payload)
    response_object = response.json()
    if response_object['data']['result'] == 'undeliverable':
        raise serializers.ValidationError('Email provided is undeliverable!')