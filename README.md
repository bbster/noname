Scrapy + API
===
- 어떤거 할지 아직 안정함
- Use Stack
```text
Python 3.8.1
Django 4.0.6
Postgresql
Scrapy
Docker
GCP(사용해볼 예정)
```
---
### APIView, GenericView/Viewset
- 간단하고 빠르게 구현할것이라면 GenericView/ViewSet
- 조금더 커스텀 하게 사용하고자 한다면 APIView
---
### 쿼리 연습 사이트
- https://inpa.tistory.com/entry/DB-%F0%9F%93%9A-SQL-%EC%97%B0%EC%8A%B5-%EC%98%A8%EB%9D%BC%EC%9D%B8-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%AA%A8%EC%9D%8C
- https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all
- http://sqlfiddle.com/#!17/9eecb
---
### MongoDB
- not yet
---
### Scrapy
- pip install scrapy
---
### Conventional
- feat : 새로운 기능 추가
- fix : 버그 수정
- docs : 문서 수정
- style : 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우
- refactor : 코드 리펙토링
- test : 테스트 코드, 리펙토링 테스트 코드 추가
- chore : 빌드 업무 수정, 패키지 매니저 수정
```text
Feat: "회원 가입 기능 구현"

SMS, 이메일 중복확인 API 개발

Resolves: #123
Ref: #456
Related to: #48, #45
```
---