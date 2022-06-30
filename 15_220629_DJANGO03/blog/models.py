from django.db import models

# Create your models here.
class BlogPost(models.Model): # 클레스 이름은 대문자로 파스탈,, ? 앞에 대문자 두번째도 대문자 클래스의 네이밍 컨베션.
    title = models.CharField(max_length=128) # CharField에는 맥스랭스가 반드시 들어가야함
    # 스네이크 케이스 createdAt -> created_at namming combestion? 을 지키자!
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 생성 수정
    update_at = models.DateTimeField(auto_now=True) # 업데이트만?