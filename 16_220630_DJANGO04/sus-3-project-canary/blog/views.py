from django.shortcuts import render, redirect

from blog.models import Article


def blog_home(request):
    post_all = Article.objects.all().order_by("-pk")
    context = {
        "post_list": post_all
    }
    return render(
        request,
        "blog-html/index.html",
        context,
    )

    return render(request, "blog-html/index.html")

def blog_post_create(request):
    if request.method == "POST": # POST는 대문자
        # print(request.POST.get("title"))
        # print(request.POST.get("content"))
        # 딕셔너리의 형태로 옴.
        # 딕셔너리여서 키 값을 .get으로 했다.
        # 키 값이 어떻게 정해지는가?
        # input의 name에 들어 가 있는 값과 동일 하다.

        new_post = Article()
        new_post.title = request.POST.get("title")
        new_post.content = request.POST.get("content")
        new_post.save()
        
        return redirect("/blog-url/home/") # 기술적인게 연관되어있는데 일단 이렇게 사용해라. 홈페이지로 돌아가라
        # return render(request, "blog-html/index.html")
    elif request.method == "GET":
        return render(request, "blog-html/post-create.html")

def blog_post_read(request, target_id):
    # 유니폼머시기 파일을. 바꿔줘야함
    target_post = Article.objects.get(id=target_id)
    context = {
        "post":target_post,
    }
    return render(
        request,
        "blog-html/post-read.html",
        context,
    )
    # return render(request, "blog-html/post-read.html")

def blog_post_update(request, target_id):
    target_post = Article.objects.get(id=target_id)
    if request.method == "POST":
        target_post.title = request.POST.get("title")
        target_post.content = request.POST.get("content")
        target_post.save()
        return redirect(f"/blog-url/{target_id}/read/")

    elif request.method == "GET":
        context = {
            "post":target_post,
        }
        return render(
            request, 
            "blog-html/post-update.html",
            context,
        )

def blog_post_delete(request, target_id):
    target_post = Article.objects.get(id=target_id)
    if request.method == "POST":
        print("yes delete")
        target_post.delete()
        return redirect("/blog-url/home/")

    elif request.method == "GET":
        context = {
            "post":target_post
        }
        return render(
            request,
            "blog-html/post-delete.html",
            context
        )

