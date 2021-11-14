flask를 이용한 웹브라우저입니다.


<img width="718" alt="스크린샷 2021-11-14 오후 8 30 14" src="https://user-images.githubusercontent.com/87803612/141679032-30fff4d1-4053-4082-bec1-19edf9ffd568.png">

[링크](https://okdohyuk.tistory.com/31) 를 참고하여 만들었습니다. (Mac OS 기준)


# Super User (관리자 권한으로 가상환경을 위한 라이브러리 생성)
sudo pip3 install virtualenv

# 가상환경 설치를 위한 경로 이동 및 디렉토리 생성
cd Desktop
mkdir html

# 가상환경 형성
virtualenv myproject

# 가상환경 실행
cd myproject
source bin/activate

# FLASK 설치
pip3 install Flask

# main.py 형성

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask!'

if __name__ == '__main__':
	app.run(debug=True)
  

# Flask 실행

export FLASK_APP = main
flask run


이 과정을 마무리하면 다음과 같은 화면을 출력할 수 있습니다. 

<img width="1440" alt="스크린샷 2021-11-14 오후 8 46 16" src="https://user-images.githubusercontent.com/87803612/141679468-a901045f-1500-4d37-9472-3d180a645d05.png">

