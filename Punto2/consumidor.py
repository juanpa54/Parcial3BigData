from kafka import KafkaConsumer
import statistics
import boto3
consumer = KafkaConsumer("quickstart-events", bootstrap_servers=['localhost:9092'])
s3 = boto3.client('s3')

suma = 0
cont = 0
max = -999999999
min = 999999999
precios = list()
desv = 0
z =0

for message in consumer:
    cont = cont +1
    precio = int(message[6].decode("utf-8"))
    precios.append(precio)
    suma = suma + precio
    promedio = suma/cont
    if precio > max:
            max = precio
    elif precio < min:
            min = precio
    if len(precios) > 1:
            desv = statistics.stdev(precios)
    else:
            desv = 0
    if desv != 0:
            z = (precio-promedio)/desv
    if z >= 2:
            print('--------------------------------------------------------------------')
            print('    El precio está por encima de las dos desviaciones estandar !!!! ')
            print('--------------------------------------------------------------------')
    elif z <= -2:
            print('--------------------------------------------------------------------')
            print('    El precio está por debajo de las dos desviaciones estandar !!!! ')
            print('--------------------------------------------------------------------')
    txt_data="maximo = "+str(max)+", minimo = "+str(min)+", promedio = "+str(promedio)+", desviación estandar"+str(desv)
    directory_name = 'prices'
    s3.put_object(Body=txt_data, Bucket='bigdatajofre', Key=(directory_name+'/'+'Precios.txt'))
    print('     ------------------------------------------------------ ')
    print('     | T    O    D    A    Y    P    R    I    C    E    S  ')
    print('     ------------------------------------------------------ ')
    print('     | El precio maximo de la acción es :'+str(max)          )
    print('     | El precio minimo de la acción es :'+str(min)          )
    print('     | El precio actual de la acción es :'+str(precio)       )
    print('     | El promedio del precio es :'+str(promedio)            )
    print('     | La desviación estandar de los precios es :'+str(desv) )
    print('     ------------------------------------------------------\n\n')
