import requests

def test_fetch_groups():
    url = "https://chatbot.jastipin.id/group/fetchAllGroups/gurindamlian"
    headers = {"apikey": "8832A7D1C700-4DE4-AGY0CD-96E481A95DF1"}
    params = {"getParticipants": "false"}
    
    print("Making API request with:")
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    print(f"Params: {params}")
    
    try:
        response = requests.request("GET", url, headers=headers, params=params, timeout=10)
        print(f"\nResponse Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Content: {response.text[:1000]}")  # First 1000 chars
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nParsed JSON data type: {type(data)}")
            print(f"Data preview: {data[:2] if isinstance(data, list) else data}")
        
    except Exception as e:
        print(f"\nError occurred: {str(e)}")

if __name__ == "__main__":
    test_fetch_groups()
