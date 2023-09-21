import datetime

def log(text):
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-2]+ "Z"
    print(f"{timestamp} {text}")
