import os
import urllib.request
import json
import requests

# 1. 보안을 위해 깃허브 설정값에서 아이디와 비밀번호를 가져옵니다.
# (직접 입력하지 않아도 깃허브가 알아서 넣어줄 거예요)
client_id = os.environ.get('isQRmYCuA1s6V6CMFxuQ')
client_secret = os.environ.get('KroQ1W40OX')
bot_token = os.environ.get('8589841222:AAEBDGIQoTHMRXzxSlKCqjyUn1HdHnkzMhM')
chat_id = os.environ.get('7868549264')

# 2. 네이버 뉴스 가져오기
encText = urllib.parse.quote("국내 증시 전망")
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + "&display=5&sort=sim"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode == 200):
    response_body = response.read()
    news_data = json.loads(response_body.decode('utf-8'))
    
    # 3. 텔레그램에 보낼 메시지 꾸미기
    message = "📢 내일 증시 관련 뉴스 목록입니다!\n\n"
    
    print("--- 오늘의 주요 뉴스 목록 ---")
    for item in news_data['items']:
        title = item['title'].replace("<b>", "").replace("</b>", "").replace("&quot;", "")
        link = item['link']
        print(f"제목: {title}")
        
        # 메시지에 제목과 링크 추가
        message += f"✅ {title}\n🔗 {link}\n\n"

    # 4. 텔레그램으로 전송
    send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {'chat_id': chat_id, 'text': message}
    requests.get(send_url, params=params)
    
    print("\n✅ 텔레그램으로 알림을 보냈습니다!")

else:
    print("오류 발생:" + str(rescode))
