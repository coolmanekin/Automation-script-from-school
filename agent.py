import hashlib
import time
import os
import requests
import json
import hashlib
import datetime

api_key="1749c1e51a1f28ebf050a036da27cd6a4833c67b4daa95886f6b1273372b1ca7"
url = 'https://www.virustotal.com/vtapi/v2/file/report'
delete_percentage = 5
host="localhost" 
port ="8080"
path =os.getcwd()
scans_for_the_day =0;
curr_date = datetime.datetime.today().strftime('%d-%m-%Y')
baseline_md5 =dict()

for file in os.listdir(path):
    fullpath=os.path.join(path, file)
    if os.path.isfile(fullpath):
        baseline_md5[file]= hashlib.md5(open(fullpath,'rb').read()).hexdigest()
        
#print(baseline_md5)
        
while True:
    time.sleep(300)
    today =  datetime.datetime.today().strftime('%d-%m-%Y')
    if not curr_date.__eq__(today):
        scans_for_the_day = 0
        curr_date = today
        
    if scans_for_the_day <= 500:
        
        for file in os.listdir(path):        
            fullpath=os.path.join(path, file)
        
            if os.path.isfile(fullpath):
                if baseline_md5.get(file) == None:
                    print("New file detected : ", file)
                    md5 = hashlib.md5(open(fullpath,'rb').read()).hexdigest()
                    params = {'apikey': api_key, 'resource': md5}
                    response = requests.get(url, params=params)
                    
                    if response.status_code != 204:
                        res = response.json()
                        #print(res)
            
                    percentage=0
                    if res["response_code"].__eq__(1):
                        total = res["total"]
                        positives = res["positives"]
                        percentage = (positives/total) * 100
        
                    if percentage >= delete_percentage:
                    
                        print("percentage : "+ str(percentage)+ " removing malicious file: " + file )
                        os.remove(fullpath)
                        dictToSend = {'file':file}
                        requests.post("http://"+host+":"+port+"/api/add", json=dictToSend)
        
                    else:
                        baseline_md5[file]= md5          
       
        
        from_server = requests.get("http://"+host+":"+port+"/")
        print('Scan complete. All malicious files found and removed: ',from_server.json())
            
         
    else:
        print("Exceeded daily limit ")


