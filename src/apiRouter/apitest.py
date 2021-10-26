import json
import urllib.request
import re
pattern = re.compile(u'<\/?\w+\s*[^>]*?\/?>')


client_id = "FX0D1x996cJpBNHf5huf"
client_secret = "ZFgUa_ti5y"
encText = urllib.parse.quote("자바")
url = "https://openapi.naver.com/v1/search/book_adv.json?d_catg=280&d_titl=" + encText  # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if (rescode == 200):
    response_body = response.read()
    result = response_body.decode('utf-8')
    qq = json.loads(result)
    a = qq['items'][0]['title']
    a1 = str(a)
    print(pattern.sub(u"", a1))

else:
    print("Error Code:" + rescode)


