import requests
import json

def track_phone_number(phone_number, api_key):

    url = f"https://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    
   
    response = requests.get(url)
    
   
    if response.status_code == 200:
        data = response.json() 
        return data
    else:
        return {"error": "Failed to retrieve data", "status_code": response.status_code}

def main():
    phone_number = input("Enter the phone number (with country code): ")
    api_key = "Give your API key" #replace with your own API key otherwise it will fail or show the error

    
    data = track_phone_number(phone_number, api_key)

    
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()