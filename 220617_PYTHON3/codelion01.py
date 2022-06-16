import requests

# print(requests.get)

# put, get post delete, 요청하면 응답. 예)배가고파져서 주문이요. 햄버거 , 주문받았습니다. 요리해서 햄버거 돌려줌.
# server 응답 / client 요청하면 /
url = 'https://lifena.netlify.app/'
response = requests.get(url)

# print(response.text)

# print(response.url)

# print(response.content)

# print(response.encoding)

# print(response.headers)

# print(response.json)

# print(response.links)

# print(response.ok)

# print(response.status_code)

#server return : requests.response