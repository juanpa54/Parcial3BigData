# Parcial Final Big Data
# Por: Jofre Eduardo Oliveros y Juan Pablo Blanco
# Universidad Sergio Arboleda

El presente proyecto tiene como objetivo desarrollar funciones en python que por medio de herramientas como aws glue, permitan extraer información precisa de sitios web para posteriormente escribir los resultados en distintos servicios de Amazon Web Services como lo son Athena y S3.


### 1. Workflow aws glue que realiza scrapping a eltiempo.com y a publimetro.com📰 

[job1](Punto1/job1.py) cada dia descargará la página principal de El Tiempo y Publímetro.

La información quedará en S3 con la estructura:

• s3://bucket/headlines/raw/periodico=xxx/year=xxx/month=xxx/day=xxx

Una vez llegado el archivo a la carpeta raw, se activará a [job2](Punto1/job2.py) el cual leerá los datos que llegaron utilizando Beautifulsoup. Este proceso va a extraer la categoría, el titular y el enlace para cada noticia. Estos datos se deben guardar en un csv en la
siguiente ruta:

• s3://bucket/headlines/final/periodico=xxx/year=xxx/month=xxx/day=xxx

Este archivo dispara a [job3](Punto1/job3.py) que descarga la noticia y lo guarda en:

• s3://bucket/news/raw/periodico=xxx/year=xxx/month=xxx/day=xxx

### 2. Aplicación en spark-streaming-kafka que permita determinar la variación del precio de las acciones en tiempo real. 💲💲💲💲💲

[productor.py](Punto2/productor.py) se encargará de leer enl dataset y extraer los precios de él, cada 4 segundos se enviará un nuevo precio hacia el consumidor.

[consumidor.py](Punto2/consumidor.py) se encargará de  mostrar el promedio hasta el momento, el máximo y mínimo hasta el momento en cada instante. Además mostrará una alerta cuando el precio está por encima o por debajo de 2 desviaciones estándar de la media. Por último este programa escribirpá la información en un bucket de S3.



### ...Esperamos que disfrutes el proyecto, cualquier comentario escribir a [juan.blanco01@correo.usa.edu.co] o a [jofre.oliveros01@correo.usa.edu.co] 😊
