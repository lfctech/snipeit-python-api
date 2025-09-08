from snipeit import SnipeIT
import os

api_key_path = os.path.join(os.path.dirname(__file__), 'docker', 'api_key.txt')
with open(api_key_path, 'r') as f:
    # The file contains "API Token: <token>"
    api_key = f.read().replace('API Token: ', '').strip()

client = SnipeIT(url="http:///localhost:8000", token=api_key)

asset = client.assets.list()[0]
print(asset)