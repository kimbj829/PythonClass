'''
GET POST

GET
- URL로 파라미터가 남음
ex) 아래처럼 2페이지로 넘어갈시 ?pageno=2가 추가됨
https://notice.nexon.com/Notice/NoticeList
https://notice.nexon.com/Notice/NoticeList?pageno=2
POST
- URL로 파라미터가 남지 않음


http 상태코드
- 200 : 성공
- 400 : 클라이언트 요청의 형식이나 내용이 잘못전달
- 401 : 인증정보를 누락하거나 잘못 지정한 경우
- 404 : 페이지를 찾을 수 없다 요청 url을 찾을 수 없다
- 500 : 서버의 내부 오류
'''