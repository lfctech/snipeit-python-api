from snipeit import SnipeIT
import os
import random

api_key_path = os.path.join(os.path.dirname(__file__), 'docker', 'api_key.txt')
with open(api_key_path, 'r') as f:
    # The file contains only the JWT token
    api_key = f.read().strip()
    
client = SnipeIT(url="http://localhost:8000", token=api_key)
random_index = random.randint(1, 100)
asset = client.assets.list()[random_index]
print(asset)
