## 시연 화면

### 1. 메인 페이지

<img src="assets/fd3c14ad3fb0ced535e1d860c9de4819a3252e4b.JPG" title="" alt="Screenshot 2022-10-07 at 17.06.13.JPG" width="481">

### 2. 리뷰 리스트 페이지

<img src="assets/6cb746b414c1f972b9a2ce11c9f0ef958e48d8bc.JPG" title="" alt="Screenshot 2022-10-07 at 17.06.28.JPG" width="480">

### 3. 리뷰 상세 페이지

<img src="assets/16a7dbd55df2f21a1a97327e765960a4d266509b.JPG" title="" alt="detail.JPG" width="477">

### 4. 리뷰 수정 페이지

<img title="" src="assets/ed8ecd2d060a3879445dae740ae6c65bb04d3d66.JPG" alt="Screenshot 2022-10-07 at 17.05.54.JPG" width="468">

### 5. 반응형 Navbar

<img src="assets/54e0d4c45d47a1eaabf2d3beb329f956967f310b.JPG" title="" alt="Screenshot 2022-10-07 at 17.06.39.JPG" width="474">

## 목표

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- ModelForm 활용 CRUD 구현
- Staticfiles 활용 서비스 로고 표시

## 요구 사항

### 모델 Model

모델은 아래 조건을 만족해야합니다.

적절한 필드와 속성을 부여하세요.

- 모델 이름 : Review

- 모델 필드
  
  | 이름         | 역할      | 필드       | 속성                |
  | ---------- | ------- | -------- | ----------------- |
  | title      | 리뷰 제목   |          |                   |
  | content    | 리뷰 내용   |          |                   |
  | movie_name | 영화 이름   |          |                   |
  | grade      | 영화 평점   |          |                   |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now = True   |

### 기능(View), 화면(Template)

**네비게이션바, Bootstrap <nav>**

- 서비스 로고
  
  - Django Staticfiles 활용
  - 클릭 시 메인 페이지로 이동

- 리뷰 목록 버튼
  
  - 클릭 시 목록 페이지로 이동

- 리뷰 작성 버튼
  
  - 클릭 시 작성 페이지로 이동

```html
<!--base.html-->
<nav class="navbar navbar-expand-lg bg-dark navbar-dark p-0 sticky-top">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'reviews:main' %}"><img src="https://cdn-icons-png.flaticon.com/512/3223/3223092.png" alt=""
                    width="30px"></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link btn btn-dark" href="{% url 'reviews:index' %}">목록</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link btn btn-dark" href="{% url 'reviews:create' %}">추가</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
```

**메인 페이지**

- `GET` http://127.0.0.1:8000/reviews/
- 자유 디자인
- ```html
  <!--reviews/main.html-->
  {% extends 'base.html' %}
  {% load static %}
  {% block body %}
  <div class="bg-dark d-flex justify-content-center">
  <div id="carouselExampleControls" class="carousel slide w-50" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="{% static 'images/movie1.jpg' %}" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="{% static 'images/movie2.jpg' %}" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="{% static 'images/movie3.jpg' %}" class="d-block w-100" alt="...">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  </div>
  {% endblock body %}
  ```

**목록 페이지**

- `GET` http://127.0.0.1:8000/reviews/index/

- 리뷰 목록 출력
  
  - 리뷰 제목
  - 영화 이름

- 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

- ```html
  <!--reviews/index.html-->
  {% extends 'base.html' %}
  {% load static %}
  {% load django_bootstrap5 %}
  
  {% block css %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
  {% endblock %}
  
  {% block body %}
    <div class="bg-black d-flex justify-content-center mb-3">
      <img class="" src="{% static 'images/netflix.png' %}" alt="img">
    </div>
    <h1 class="text text-center">리뷰 목록</h1>
    <table class="table text-center align-middle">
      <thead>
        <th>ID</th>
        <th>제목</th>
        <th>영화 제목</th>
        <th>영화 평점</th>
        <th>시간</th>
      </thead>
      <tbody>
        {% for review in reviews %}
          <tr>
            <td>{{review.pk}}</td>
            <td>
              <a href="{% url 'reviews:detail' review.pk %}">{{ review.title }}</td>
              <td>
                {{ review.movie_name }}
              </td>
              <td>
                {{ review.grade }}
              </td>
              <td>
                {{ review.runnug_time }}분
              </td>
            </tr>
          {% endfor %}
  
        </tbody>
      </table>
    {% endblock %}
  ```

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/int:pk/
- 해당 리뷰 정보 출력
- 수정 / 삭제 버튼데이터 목록 조회
- ```html
  <!--reviews/detail.html-->
  {% extends 'base.html' %}
  
  {% block body %}
    <div class="top d-flex justify-content-between mb-3">
      <h1 class="">{{ review.title }}</h1>
    </div>
    <div>
      <p class="text-muted">평점:
        {{ review.grade }}</p>
    </div>
    <div class="text">
      <p class="text-muted mt-5 border border-3 p-3">{{ review.content | linebreaksbr }}</p>
    </div>
    <div class="detail-btn text-end">
      <a href="{% url 'reviews:index' %}" class="btn btn-outline-info">목록</a>
      <a href="{% url 'reviews:update' review.pk %}" class="btn btn-outline-success">수정</a>
      <a href="{% url 'reviews:delete' review.pk %}" class="btn btn-outline-danger">삭제</a>
  
    </div>
  {% endblock body %}
  ```

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼
- ```html
  <!--reviews/create.html-->
  {% extends 'base.html' %}
  {% load django_bootstrap5 %}
  
  {% block body %}
  <h1>글쓰기</h1>
  
  <!-- form : 사용자에게 양식을 제공하고 
    값을 받아서(input : name, value) 
    서버에 전송(form : action, method)-->
  <form action="" method="POST">
      {% csrf_token %}
  
      {% bootstrap_form review_form %}
      {# review_form.as_p #}
      <!-- <label for="title">제목 : </label>
    <input type="text" name="title" id="title" required>
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10" required></textarea> -->
      {% bootstrap_button button_type="submit" content="OK" %}
      {% bootstrap_button button_type="reset" content="Cancel" %}
  </form>
  {% endblock %}
  ```

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/int:pk/update/
- 리뷰 수정 폼
- ```html
  {% extends 'base.html' %}
  {% load django_bootstrap5 %}
  
  {% block body %}
  <h1>글 수정하기</h1>
  
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form review_form %}
      {% bootstrap_button button_type="submit" content="OK" %}
      {% bootstrap_button button_type="reset" content="cancel" %}
  </form>
  {% endblock %}
  ```






