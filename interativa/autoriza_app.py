# -*- coding: utf-8 -*-
import tweepy

CONSUMER_API_KEY = 'Kv5UHuOhicN0tfL9ZEhizJCE1'
CONSUMER_API_SECRET = 'O5dVob6csLWyTaFepFwMMJb4BUnyqPCXwfgaWONrWwhBwhn0Go'
ACCESS_TOKEN = '3547470323-4YkBZ69Kscem9QLBx0WqV0oZ7bcVkQHD5OQJjIi'
ACCESS_TOKEN_SECRET = '5bPLxwd04H9uDIhL4wSoc0r1BGUuS2u0IwlOonADTdomM'

auth = tweepy.AppAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)

api = tweepy.API(auth)
if not api:
    print('Ocorreu um erro ao tentar conectar!')
