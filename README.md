# django
## 웹 프로그래밍 --> 홈페이지, 웹 서비스 만들기
- Frontend : 화면(웹 브라우저에서 동작하는 코드) -> HTML, CSS, JS
- Backend : 서버(데이터를 입출력하거나, 계산 하는 서버에서 동작하는 코드)
> - 컴퓨터에서 동작하는 언어(Python, Ruby, Java, PHP, JS, C#)
> - GO, Erlangm Perl

## HTTP
- 웹 사이트 동작 방식
> - 웹 브라우저 주소창에 URL 입력
> - URL을 이용해 서버의 IP 접근
> - IP를 이용해서 서버 접속
> - URL에 해당하는 자료 request
> - 웹 어플리케이션이 URL을 해석해서 해당하는 코드 동작
> - 코드의 동작 결과를 response
> - 서버가 웹 브라우저로 데이터를 보내줌
> - 웹 브라우저 응답 받은 데이터를 화면에 표시
> - * JS(AJAX)

- Backend_code : 각각의 URL 패턴마다 소스코드 1개 이상
## Framwork
> - 어떤 일을 할 때 자주 사용되는 기능을 미리 준비해둔것.
- Micro(Flack) : 최소한의 기능만 가지고 있다. + 추가 기능을 원하는 대로 설치해서 사용
- FullStack(Django) : 거의 대부분의 기능을 가지고 있다. + 추가 기능도 설치 가능


## 디자인 패턴
> - 개발 설계상 발생하는 문제를 해결하기 위한 해결책
> - 디자이너, 프론트, 백엔드 역할을 나눔
- MVC : Model(데이터베이스), View(화면 - 프론트), Controller(계산, 처리 - 백엔드)
- MTV : Model(데이터베이스), Template(화면 - 프론트), View(계산, 처리 - 백엔드)

## Django 프로젝트 flow
> 1. 프로젝트 만들기
> 2. 장고 설치
> 3. 장고 프로젝트 만들기
> 4. 설정하기(DB, S3)
> 5. 데이터베이스 초기화
> 6. 관리자 계정 만들기
> 
> 8. 앱(App) 만들기
> 9. 모델 설계(데이터베이스)
> 
> 10. 뷰 만들기(기능, 계산)
> 11. 템플릿 만들기(화면에 표시될 내용, 양식)
> 12. URL 만들기
>   - 대표적인 기능(화면) : CRUD -> Create, Read, Update, Delete

[배우는 프로그래머 강의](https://www.youtube.com/channel/UCoIC6Nj833OCz3J3bZrJGyg)
