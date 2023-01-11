from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests

# API
# CONSTANT 
REQ = {
    'KEY': 'User-Agent',
    'VALUE': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

#Modules
def getHTMLData(query):
    data = requests.get(f'https://www.youtube.com/results?search_query={query}', headers={REQ['KEY']: REQ['VALUE']})
    soup = BeautifulSoup(data.text, 'html.parser')
    return soup

def parseData():
  result = [];

#Server
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_get():
   query = request.args.get('query')
   HTMLData = getHTMLData(query)
   resData = list(HTMLData)[1];
   return jsonify({ 'data': str(resData)})
   

#####Auth#####

#LogIn
@app.route('/auth/login', methods=['GET'])
def getlogIn():
   return render_template('auth/login.html')

@app.route('/auth/login', methods=['POST'])
def logIn():
  #코드 구현하시면 됩니다.
   return jsonify({ 'data': 'test'})

#SignIn
@app.route('/auth/signIn', methods=['GET'])
def getSignIn():
   return render_template('auth/signIn.html')

@app.route('/auth/signIn', methods=['POST'])
def signIn():
    inputId = request.form['inputId']
    inputPw = request.form['inputPw']
    error = True

    # 유효성 검사 (빈문자열, 4자리 미만, ID중복 여부)
    if (len(inputId.strip()) == 0):
        msg = "ID를 입력해 주세요."
    elif (len(inputPw.strip()) == 0):
        msg = "PW를 입력해 주세요."
    elif (len(inputId) < 4 or len(inputPw) < 4):
        msg = "ID와 PW의 길이는 4자가 넘어야 합니다."
    elif (db.users.find_one({'id': inputId}) != None):  # 이미 등록된 ID
        msg = "이미 등록된 ID입니다."
    else:
        msg = "회원가입 완료!"
        error = False
        db.users.insert_one({'id': inputId, 'pw': inputPw, 'playlist': []})

    return jsonify({'errorMessage': msg, 'error': error})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)