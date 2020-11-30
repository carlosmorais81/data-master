from kafka import KafkaConsumer


class Consumer:
    def __init__(self):
        self.broker = 'localhost:9092'
        self.topico = 'twitters'

    def get_msg(self):
        consumers = KafkaConsumer(self.topico, group_id='gp1', bootstrap_servers=self.broker)

        try:
            return consumers

        except Exception as e:
            print(e)
