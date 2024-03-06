import requests
import re




url = 'http://10.12.0.30/'
filePaths = []

with open("directories.txt", "r") as content:
    for line in content:
        filePaths.append(line.strip())

successfulLinks = []

for path in filePaths:
    response = requests.get(url+path+ "/flag.txt")
    if response.status_code == 200:
        successfulLinks.append(url+ path+ "/flag.txt")

print( "Sucessful links:")
for link in successfulLinks:
    print(link)
       


#response = requests.get(url + "/s3cr3t/users.txt", auth = (username, password))
#content = response.text


#print(re.findall('natas4:(.*)', content)[0])
