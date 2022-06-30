from cmath import e
from django.shortcuts import render, redirect
from blog.models import BlogPost 

# Create your views here.
def blog_home(request):
    return render(request, "blog/index.html")
def create(request):
    if request.method == "POST":
        
        new_post = BlogPost()
        new_post.title = request.POST.get("title")
        new_post.content = request.POST.get("content")
        new_post.save()

        # print(request.POST.get("title"))
        # print(request.POST.get("content"))

        return redirect("/blog/home/")
    elif request.method == "GET":
        return render(request, "blog/create.html")

def read(request):
    return render(request, "blog/read.html")
def update(request):
    return render(request, "blog/update.html")
def delete(request):
    return render(request, "blog/delete.html")

def temp():
    # 1. create
    new_post = BlogPost()
    new_post.title = "new post title"
    new_post.content = "Lorem Ipsum"
    new_post.save()

    print(BlogPost.objects.all())
    # ORM
    # 조회하는 거 blogpost.objects의 멤버변수와 all() 
    # 대상클래스를 쓰고 
    # 안에 있는 오브젝스 변수를 갖고 온다
    # 함수를 가지고 오면 

    # 2. Read 조회하는 것 아래 코드
    post_list = BlogPost.objects.all()
    for post in post_list:
        print(post.title)
    first_post = BlogPost.objects.get(id=2)
    print(first_post.created_at)
    print(f"title : {first_post.title}")
    print(f"content : {first_post.content}")
    print(f"created : {first_post.created_at}")

    # objets 멤버변수안에..

    # 2. 새로운 레코드를 넣는다. append와 같은 기능.
    new_post = BlogPost()
    new_post.title = "new post title" 
    new_post.content = "Lorem Ipsum"
    new_post.save() # 데이터베이스와 통신하면서 새로운 row를 기록한다.

    # 3. Update 존재하는 row의 값을 업데이트할 때 사용.
    target_post = BlogPost.objects.get(id=1)
    target_post.title = "Blog Title0"
    target_post.content = "updated new content"
    target_post.save()

    # 4. Delete 하나의 row를 가져와서 삭제하기.
    target_post = BlogPost.objects.all().order_by("-pk")[0]
    print(target_post.id)
    # target_post.delete()



