# customizing admin

## src
- models.py
```python
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# ForeignKey
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # makemigrations -> migrate
    class Meta:
        ordering = ['-updated', ] # 정렬 기준

    def __str__(self):
        return self.author.username + ' ' + self.created.strftime('%Y-%m-%d %H:%M:%S')

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])
```
- admin.py
```python
from django.contrib import admin
from .models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created',  'updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created', 'author__username']
    ordering = ['-updated', '-created']

admin.site.register(Photo, PhotoAdmin) # 모델 등록
```
- 각 app에 admin.py에서 작업
- `admin.ModelAdmin`을 상속 받아 customizing

## `list_display`
-------------------------
- 관리자 페이지에서 테이블의 저장된 속성들을 기준으로 컬럼이 생신다.
- 보고 싶은 대로, 입맛대로 바꿀 수 있음
- 커스터마이징 전보다 뭔가 있어 보임
- 내가 보고 싶은 속성만 깔끔하게 정리 되서 보인다.

> ![image](https://user-images.githubusercontent.com/77317312/129652008-372d3b11-91df-40aa-92a8-24c48cad2d45.png)
> ## 이렇게 바뀜 👇🔻👇
> ![image](https://user-images.githubusercontent.com/77317312/129652072-ce6fc5e4-3c7d-4a57-a2d7-44a0ef788dce.png)

## `raw_id_fields`
-------------------------
- 커스텀하기 전에는 사진을 저장하는 곳에서 user를 고루기위해선 리스트로 찾았지만 커스터마이징 후 검색으로 바뀜.
- 사용자가 많아지면 찾기 힘들어지니까...
- 커스터마이징 후 돋보기를 누르면 별도의 select user 창이 뜨거 user를 고를 수 있음

> ![image](https://user-images.githubusercontent.com/77317312/129652697-62a6747c-22f4-4b5e-9828-f435e50042d6.png)
> ## 이렇게 바뀜 👇🔻👇 -> 이건 별도 창
> ![image](https://user-images.githubusercontent.com/77317312/129653233-97a876cb-c092-47b6-9779-3aa63befe51b.png)

## `list_filter`
----------------------
- 관리자 페이지에서 테이블의 리스트를 지정한 속성들을 통해 필터링 할 수 있다.

> ![image](https://user-images.githubusercontent.com/77317312/129653651-5a92f85a-e62d-4940-804a-bb6d0eeefe85.png)
> ## 이렇게 바뀜 👇🔻👇
> ![image](https://user-images.githubusercontent.com/77317312/129653733-68ef5c28-4b65-417f-91ea-addc87e4ca17.png)

## `search_fields`
-----------------------
- 커스터 마이징 후 지정한 fields로 조회 할수 있는 search 칸이 생김

> ![image](https://user-images.githubusercontent.com/77317312/129654830-da009822-c886-4fab-aca4-f2cb922a8bc7.png)
> ## 이렇게 바뀜 👇🔻👇
> ![image](https://user-images.githubusercontent.com/77317312/129655044-1644125e-93fb-4f1a-b2fb-9583ac621f24.png)

## `ordering`
--------------------
- 지정한 속성대로 정렬
- 앞에 `-`를 붙이면 최근 순으로 정령!!
