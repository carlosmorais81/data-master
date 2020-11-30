# -*- coding: utf-8 -*-
from interativa.autoriza_app import api
import tweepy
import msgs.producer

consulta = '#Santander'

numMaxTweets = 50
contadorTweets = 0

prod = msgs.producer.Producers()

for tweet in tweepy.Cursor(api.search, q=consulta).items(numMaxTweets):
    prod.resp = tweet._json
    prod.send_msg()
    contadorTweets += 1

print("Foram coletados " + str(contadorTweets) + " tweets.")


