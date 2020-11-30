import json
import os
from datetime import datetime

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster

import msgs.consumer


class Dados:
    def __init__(self):
        self.horario = ""
        self.created_at = ""
        self.desc_text = ""
        self.hashtg = ""
        self.id_usr = ""
        self.screen_name = ""
        self.location = ""
        self.followers_count = ""
        self.friends_count = ""
        self.listed_count = ""
        self.created_at_usr = ""
        self.favourites_count = ""
        self.statuses_count = ""
        self.retweet_count = ""
        self.favorite_count = ""
        self.lang = ""
        self.dt_proc = ""
        self.insert = ""

    def insert_tweeter(self):
        qry = 'insert into twitters.twitt("horario", "created_at", "desc_text", "hashtg", "id_usr", "screen_name", ' \
              '"location", "followers_count", "friends_count", "listed_count", "created_at_usr", "favourites_count", ' \
              '"statuses_count", "retweet_count", "favorite_count", "lang", "dt_proc") values '

        return qry + "('" + self.horario + "','" + self.created_at + "','" + self.desc_text + "','" + \
               self.hashtg + "','" + self.id_usr + "','" + self.screen_name + "','" + self.location + "','" + \
               self.followers_count + "','" + self.friends_count + "','" + self.listed_count + "','" + \
               self.created_at_usr + "','" + self.favourites_count + "','" + self.statuses_count + "','" + \
               self.retweet_count + "','" + self.favorite_count + "','" + self.lang + "','" + self.dt_proc + "')"

    def grava_scylla(self):
        cluster = Cluster(contact_points=["scylla-node1", "scylla-node2", "scylla-node3"])
        session = cluster.connect(keyspace="twitters")
        session.default_consistency_level = ConsistencyLevel.QUORUM
        session.execute(self.insert)


consumers = msgs.consumer.Consumer()
dado = Dados()
res = []

for messagem in consumers.get_msg():
    texto = json.loads(messagem.value.decode('utf-8'))
    hashtg = "#".join(map(str, [r['text'] for r in texto['tweet']['entities']['hashtags']]))
    dado.horario = str(texto['horario'])
    dado.created_at = str(texto['tweet']['created_at'])
    dado.desc_text = str(texto['tweet']['text']).rstrip().rstrip(os.linesep).replace('\n', '').\
        replace('\r', '').replace(',', '').replace("'",'')
    dado.hashtg = str(hashtg)
    dado.id_usr = str(texto['tweet']['user']['id'])
    dado.screen_name = str(texto['tweet']['user']['screen_name'])
    dado.location = str(texto['tweet']['user']['location'])
    dado.followers_count = str(texto['tweet']['user']['followers_count'])
    dado.friends_count = str(texto['tweet']['user']['friends_count'])
    dado.listed_count = str(texto['tweet']['user']['listed_count'])
    dado.created_at_usr = str(texto['tweet']['user']['created_at'])
    dado.favourites_count = str(texto['tweet']['user']['favourites_count'])
    dado.statuses_count = str(texto['tweet']['user']['statuses_count'])
    dado.retweet_count = str(texto['tweet']['retweet_count'])
    dado.favorite_count = str(texto['tweet']['favorite_count'])
    dado.lang = str(texto['tweet']['lang'])
    dado.dt_proc = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dado.insert = dado.insert_tweeter()
    print(dado.insert_tweeter())
    # dado.grava_scylla()
    res.append(dado.insert_tweeter())

contadorTweets = 0

for tw in res:
    print(tw)

with open('tweets.json', 'w') as f:
    for tweet in res:
        f.write(tweet + '\n')
        contadorTweets += 1

    print("Foram coletados " + str(contadorTweets) + " tweets.")
