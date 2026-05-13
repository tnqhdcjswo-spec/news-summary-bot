import urllib.request
import json
import requests

# 1. 네이버 정보 (알려주신 것을 직접 넣었어요)
client_id = "KroQ1W40OX"
client_secret = "isQRmYCuA1s6V6CMFxuQ"

# 2. 텔레그램 정보 (여기에 직접 복사해서 넣어주세요!)
bot_token = "8589841222:AAEBDGIQoTHMRXzxSlKCqjyUn1HdHnkzMhM"
chat_id = "7868549264"

# 네이버 뉴스 가져오기
encText = urllib.parse.quote("국내 증시 전망")
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + "&display=5"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

try:
    response = urllib.request.urlopen(request)
    news_data = json.loads(response.read().decode('utf-8'))
    
    # 메시지 만들기
    message = "📢 오늘의 증시 뉴스입니다!\n\n"
    for item in news_data['items']:
        title = item['title'].replace("<b>", "").replace("</b>", "").replace("&quot;", "")
        message += f"✅ {title}\n"

    # 텔레그램 보내기
    send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.get(send_url, params={'chat_id': chat_id, 'text': message})
    print("성공! 텔레그램을 확인하세요.")

except Exception as e:
    print(f"에러가 났어요: {e}")
