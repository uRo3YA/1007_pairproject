from django.shortcuts import render

# Create your views here.
def index(request):
    # 게시글을 가져와서..

    # Template에 전달한다.

    return render(request, "reviews/index.html")
