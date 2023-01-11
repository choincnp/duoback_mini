from flask import Flask, session, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.1sichzk.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta
app = Flask(__name__)
app.secret_key = "Mykey"

sessionId = "kkk12"

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
    # session.pop('id', None)
    if 'id' in session:
        # sessionId = session['id']
        # print(session['id'])
        global sessionId
        print(sessionId)
        return render_template('index.html')
    else:
        print(sessionId)
        return render_template('/auth/login.html')
# session 오류 해결하려고 입력
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/search', methods=['GET'])
def search_get():
   query = request.args.get('query')
   HTMLData = getHTMLData(query)
   resData = list(HTMLData)[1];
   return jsonify({ 'data': str(resData)})

#PlayList
@app.route('/playlist', methods=['POST'])
def list_post():
    # list data
    global sessionId
    title = request.form['title']
    thumbnail = request.form['thumbnail']
    owner = request.form['owner']
    musicId = request.form['id']
    duration = request.form['duration']
    musicInfo = {
        'title' :title,
        'thumbnail' : thumbnail,
        'owner' : owner,
        'musicId' : musicId,
        'duration' : duration
    }
    # 선택한 플레이리스트 몽고db에 저장
    user = db.users.find_one({'id': sessionId},{"_id": False})['playlist']
    user.append(musicInfo)
    db.users.update_one({'id': sessionId}, {'$set': {'playlist': user}})

    # 몽고db에서 플레이리스트 꺼내기
    allPlaylist = db.users.find_one({'id':sessionId})['playlist']

    return jsonify({"msg": allPlaylist})

@app.route('/playlist', methods=['GET'])
def list_get():
    #DB에서 정보를 가져옴
    playlist = db.users.find_one({'id': 'test1'})['list']
    return jsonify({'playlist' : playlist})

#Auth
@app.route('/auth/login')
def login():
   return render_template('auth/login.html')

#####Auth#####

#LogIn
@app.route('/auth/login', methods=['GET'])
def getlogIn():
   return render_template('auth/login.html')

@app.route('/auth/login', methods=['POST'])
def logIn():
    user_id = request.form['inputId']
    user_pw = request.form['inputPw']
    error = True
    playlist = 0

    # 유효성 검사 (빈문자열, 4자리 미만, ID 존재여부 -> 존재하면 PW 일치 확인)
    if (len(user_id.strip()) == 0):
        msg = "ID를 입력해 주세요."
    elif (len(user_pw.strip()) == 0):
        msg = "PW를 입력해 주세요."
    elif (len(user_id) < 4 or len(user_pw) < 4):
        msg = "ID와 PW의 길이는 4자가 넘어야 합니다."
    elif (db.users.find_one({'id': user_id}) == None):  # 등록되지 않은 ID
        msg = "등록되지 않은 ID입니다. 회원가입 하세요."
    elif (db.users.find_one({'id': user_id})['pw'] != user_pw):  # ID, PW 일치 확인
        msg = "ID와 PW가 일치하지 않습니다. 다시 확인해보세요."
    else:
        msg = "로그인 성공"
        error = False  # 로그인 가능
        session['id'] = user_id
        global sessionId
        sessionId = user_id

    return jsonify({'message': msg, 'error': error})

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


    return jsonify({'message': msg, 'error': error})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5003,debug=True)

