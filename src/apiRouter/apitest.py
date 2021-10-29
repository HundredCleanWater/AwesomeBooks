from flask import Blueprint, jsonify, request, render_template
import urllib.request

search_page = Blueprint('search', __name__, url_prefix='/')

@search_page.route('/search', methods=['GET'])
def search():
    search_receive = request.args.get('search_give')
    search_result = api_value(search_receive)
    return jsonify({'all_search_results': search_result})

def api_value(query):
    client_id = "FX0D1x996cJpBNHf5huf"
    client_secret = "ZFgUa_ti5y"
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/book_adv.json?d_catg=280&d_titl=" + encText  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)





