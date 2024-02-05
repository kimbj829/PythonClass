import urllib.request   #url을 열기 위한 확장 라이브러리
from urllib.parse import quote
import json

search = quote(input("검색할 던어를 입력해 주세요 >> "));
start = quote(input("시작 위치 번호를 입력해 주세요 >> "));
client_id = "zgmespOgzVRZF0hJTIei";     #네이버로 부터 받은 아이디 입력
client_secret = "H4LKK3JvzX";           #네이버로 부터 받은 비번 입력
'''
Query String
- 퀴리스트링이란 URL 뒤에 입력 데이터를 함께 제공하는 가장
  단순한 데이터 전달 방법(파라메타)
- 웹 개발에서 데이터를 요청하는 방식 중 GET, POST방식이 있는데
  주로 GET방식에서 사용
- URL 주소 되에 물음표 ex) key1 =value&key2=value
  방식으로 데이터 요청
'''
API_URL = "https://openapi.naver.com/v1/search/book.json?query=" + search + "&start=" + start;
request = urllib.request.Request(API_URL);
request.add_header("X-Naver-Client-Id", client_id);         #제공된 아이디를 Clinet_ID에 대입
request.add_header("X-Naver-Client-Secret", client_secret); #제공된 비번를 Clinet_Secret에 대입
response = urllib.request.urlopen(request);
rescode = response.getcode(); #Http 상태코드를 얻음 ex02에 관련 오류 번호있음

if rescode == 200:      #rescode가 200이면 성공적으로 값을 보냄
    response_body = response.read();
    json_str = response_body.decode('utf-8');
    print(json_str);
    data = json.loads(json_str);
    data_parse = data['items'];
    for i in data_parse:
        print("================");
        print("제목 :", i['title']);
        print("출판사 :", i['publisher']);
        print("저자 :", i['author']);
        print("================");
else :
    print("Error Code : ", rescode);
