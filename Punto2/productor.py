from kafka import KafkaProducer
import pandas as pd
import time
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
df = pd.read_csv('https://raw.githubusercontent.com/juanpa54/Parcial3BigData/main/SPY_TICK_TRADE.csv')

for i in range(len(df['PRICE'])):
        precio = str(df['PRICE'][i])
        precio = str.encode(precio)
        producer.send('quickstart-events',precio)
        producer.flush()
        time.sleep(4)
