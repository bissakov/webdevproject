import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwNDU3MzE5LCJqdGkiOiI2NmEwMzk4MzBiYTg0YmFhYjBkNjM1N2VlZDU3ZGU3MyIsInVzZXJfaWQiOjF9.ZkW8T3_jDblSYYqFk2dQEYVT46V2p9fnGRh33BiDn9E'

r = requests.get('http://127.0.0.1:8000/api/product-list', headers=headers)

print(r.text)