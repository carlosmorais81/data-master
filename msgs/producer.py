import json
from datetime import datetime
from kafka import KafkaProducer


class Producers:
    def __init__(self):
        self.broker = 'localhost:9092'
        self.topico = 'twitters'
        self.resp = ""
        self.prod = KafkaProducer(bootstrap_servers=[self.broker],
                                  value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def send_msg(self):
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dados = {"tweet": self.resp, "horario": data_hora}

        self.prod.send(self.topico, value=dados)

