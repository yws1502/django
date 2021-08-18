from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Photo

@login_required
def photo_list(request):
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})# object_list가 관례적이다 바꿀 수 있다.

class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    # 작성자 필수 필드
    fields = ['photo', 'text'] # 작성자(author), 작성시간(created) -> auto_now_add 덕분에 알아서 들어감
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 데이터가 올바르다면 처리
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'


"""
서버에 이미지 파일을 업로드하거나 수정하거나 지운다.
장고 웹 앱이 해당 작업을 수행한다.
장고 웹 앱은 특정 서버에 업로드 되어 있다.
* 그럼 해당 기능은 특정 서버 안에서만 영향을 끼칠 수 있다.
-> 실 서비스를 배초하면 서버 컴퓨터는 1대가 아니다.
-> 사용자가 늘어날수록 서버 컴퓨터도 늘어난다.
-> 장고 웹 앱이 업로드 되어있는 서버 컴퓨터가 늘어난다.
-> 이미지 파일이 업로드 되는 컴퓨터의 갯수도 늘어나야 한다.
-> 업로드 받은 후에 다른 서버에도 공유해줘야 한다.
-> 공유해주는데 사용되는 자원(돈이나 시간)이 아깝다..
-> 어떻게하면 공유하는데 들어가는 자원을 절약할 수 있을까?
-> 이미지는 한 곳의 서버에다만 올려놓고, 거기에 접속해서 사용하자.
    -> 이러한 목적으로 클라우드 서비스를 많이 사용한다.
"""