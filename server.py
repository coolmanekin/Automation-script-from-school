from flask import Flask, request

app = Flask(__name__)
files = list()
port =8080

@app.route("/api/add",methods=["POST"])
def api_add():
    content = request.json  
    file = content['file']
    files.append(file)
    return content

@app.route("/")
def root():    
    print('returning :', files)
    return files

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=port)




