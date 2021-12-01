from datetime import datetime
import requests 
import json
import boto3


def handler(event, context):
	# Escritura de la página El Tiempo
	r= requests.get('https://www.eltiempo.com/')
	r.status_code
	r.headers['content-type']
	r.encoding
	s3 = boto3.client('s3')
	txt_data = r.text
	bucket = ''
	year = datetime.today().strftime('%Y')
	month = datetime.today().strftime('%m')
	day = datetime.today().strftime('%d')
	directory_name = 'headlines/raw/periodico=eltiempo/year='+year+'/month='+month+'/day='+day 
	s3.put_object(Body=txt_data, Bucket='', Key=(directory_name+'/'+'El_tiempo.txt'))

	#Escritura de la página publimetro
	r= requests.get('https://www.publimetro.co/')
	r.status_code
	r.headers['content-type']
	r.encoding
	txt_data = r.text
	directory_name = 'headlines/raw/periodico=publimetro/year='+year+'/month='+month+'/day='+day 
	s3.put_object(Body=txt_data, Bucket='', Key=(directory_name+'/'+'Publimetro.txt'))

	return {
        	'statusCode': 200,
        	'body': json.dumps('Hello from Lambda!')
    	}