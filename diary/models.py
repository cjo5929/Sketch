from django.db import models
from Login.models import User
# Create your models here.
class Diary(models.Model):
    
    title = models.CharField(max_length=60)
    content = models.TextField()
    dt_created = models.DateField()
    
    TF_PUBLIC = [
        (True, '공개'),
        (False, '비공개'),
    ]
    
    TF_COMMENT = [
        (True, '허용'),
        (False, '비허용'),
    ]
    
    public_TF = models.BooleanField(choices=TF_PUBLIC, default=True)
    comment_TF = models.BooleanField(choices=TF_COMMENT, default=True)
    image = models.ImageField(blank=True, default = "img_making.png", upload_to ='diary_img/')
    emotion = models.CharField(max_length=20)
    vector = models.CharField(max_length=65535)
    music_no = models.IntegerField()
    emotion_value = models.TextField()
    rate = models.BooleanField(default=False)

    # User 모델 접근
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 관리자 페이지에서 title로 보이게 하기 위해
    def __str__(self):
        return self.title

class Music(models.Model):
    title = models.TextField()
    artist = models.TextField()
    lyric = models.TextField()
    genre = models.TextField()
    release_date = models.TextField()
    vector = models.TextField()
    sentiment = models.TextField()
    url = models.TextField()
    rate = models.FloatField(default=0)
    rate_cnt = models.IntegerField(default=0)

class Comment(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField()
    dt_created = models.DateField()