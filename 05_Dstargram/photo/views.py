from django.shortcuts import render

# Create your views here.
from .models import Photo

def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})# object_list가 관례적이다 바꿀 수 있다.