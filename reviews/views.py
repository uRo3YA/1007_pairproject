from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    # 게시글을 가져와서..
    reviews = Review.objects.order_by("-pk")
    # Template에 전달한다.
    context = {"reviews": reviews}
    return render(request, "reviews/index.html", context)


def detail(request, pk):
    # 특정 글을 가져온다.
    review = Review.objects.get(pk=pk)
    # template에 객체 전달
    context = {"review": review}
    return render(request, "reviews/detail.html", context)


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
    context = {"review_form": review_form}
    return render(request, "reviews/create.html", context=context)


def update(request, pk):
    movie = Review.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        review_form = ReviewForm(request.POST, instance=movie)
        if review_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            review_form.save()
            return redirect("reviews:detail", movie.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 review_form 랜더링
    else:
        # GET : Form을 제공
        review_form = ReviewForm(instance=movie)
    context = {"review_form": review_form}
    return render(request, "reviews/update.html", context)


def delete(request, pk):

    review = Review.objects.get(pk=pk)
    review.delete()

    return redirect("reviews:index")

def main(request):
    return render(request, "reviews/main.html")
