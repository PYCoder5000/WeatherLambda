import requests
import boto3
import time
def handler(event, context):
    city = "Milpitas"
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ec1e9852707e1ebb802ad2b06b2ad5dc")
    if data.status_code == 200:
        data = data.json()
        weather_main = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('WebStacklambdaStack294303EF-Weather812728CF-U3726M1L0A53')
        table.put_item(
            Item={
                'location': city,
                'timestamp': str(time.time()),
                'weather_main': weather_main,
                'temp': str(temperature),
            }
        )
        return {
            'statusCode': 200,
            'body': 'YARRRRRR!'
        }
    else:
        print("OH NO THE THING BLEW UP! PLEASE CONTACT ME AND I WILL RESPOUND IN...4 HUNDRED YEARS.")
if __name__ == "__main__":
    handler("Yup", "SAYYY WHAT")