# 2024-Herethon-10
2024 여기톤 : HERETHON 10조 - 팀명: 20%

## 프로젝트 소개 :  📊 기로프 📊

### [해커톤 금상 수상 기사 링크]
https://n.news.naver.com/article/092/0002337413?sid=105  <br><br>

### 1. 서비스 소개

<b><매일이 치열한 성장인 여대에서 조별과제, 잡무를 팀원들과 공평하게 분배하기 어렵나요?></b><br><br>
조별과제, 모임, MT! 여대에 다니는 우리는 항상 같은 딜레마에 빠지게 됩니다. <br>지금 우리가 하고 있는 일이 공평하게 분배되고 있나… 하는 식의 고민이죠.<br>
이런 사소한 것까지 내가 해야하나 싶고, 한 사람이 너무 많은 걸 책임지고 있는 건 아닌가 싶은 그런 때. <br>
<기로프>를 사용하여 일을 공평하게 분배해보세요! <br><br>

<img width="100%" src="https://github.com/hyjang14/2024-Herethon-backend/assets/126192446/8d965e7b-b3cb-44a0-81b7-d9901896f22b"/> 
<br><br>


### 2. 기술 스택

  프론트엔드: <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"><br><br>
  백엔드: <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"><br><br>
  기획·디자인: <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">
<br><br>
  ### 3. 팀원 소개
  
  |송은지|강주은|정새영|이정은|장하연|
  |:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
  |<img width="80%" src="https://github.com/hyjang14/2024-Herethon-backend/assets/126192446/0c61cce5-7534-43a9-877e-bf7febd1e030"/>|<img width="80%" src="https://github.com/hyjang14/2024-Herethon-backend/assets/126192446/f43656f4-1f4a-4c25-80ff-8eee7405f2be"/>|<img width="80%" src="https://github.com/hyjang14/2024-Herethon-backend/assets/126192446/3cee2c61-982f-45cf-9259-5f965c2d127e"/>|<img width="80%" src="https://github.com/hyjang14/2024-Herethon-backend/assets/126192446/1a93cd52-26aa-4f6a-9acb-109920458dbd"/>|<img width="80%" src="https://github.com/hyjang14/2024-Herethon-backend/assets/126192446/d56f17ef-3f14-4bb9-adad-be25d4f17f6b"/>|
  |<b>기획·디자인|<b>프론트엔드|<b>프론트엔드|<b>백엔드|<b>백엔드|
  |서비스 디자인|회원가입·로그인 퍼블리싱|팀 퍼블리싱|할일 CRUD 구현|계정관리·비번 재설정 구현|
  |PPT 디자인|약관동의 퍼블리싱|그래프 퍼블리싱|그래프 기능 구현|팀 CRUD 구현|

<br>

### 4. 폴더 구조

```
📂 HERETHON-TEAM-10
└─ myvenv
└─ taskmanageProject
 ├─ taskmanageProject/
 │  ├─ __init__.py
 │  ├─ asgi.py
 │  ├─ settings.py
 │  ├─ urls.py
 │  └─ wsgi.py
 ├─ accounts/
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ forms.py
 │  ├─ models.py
 │  ├─ tests.py
 │  ├─ urls.py
 │  ├─ views.py
 │  ├─ templates
 ├─ teams/
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ forms.py
 │  ├─ models.py
 │  ├─ tests.py
 │  ├─ urls.py
 │  ├─ views.py
 │  ├─ templates
 └─ manage.py
```
<br>

### 5. 개발환경에서의 실행 방법

```
$ source myvenv/Scripts/activate
$ cd taskmanageProject
$ python manage.py runserver
```
