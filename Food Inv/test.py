

import requests

url = 'https://www.law.cornell.edu/uscode/text/19'

r = requests.get(url)

print(r.content)