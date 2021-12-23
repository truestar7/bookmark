from django.db import models
from django.urls import reverse

# Create your models here.
# 모델 : 데이터베이스를 SQL없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루겠다.
# 모델 = 테이블
# 모델의 필드  = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 펄드의 값(인스턴스의 필드 값) = 레코드의 컬럼 데이터값

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    
    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url
    
    def get_absolute_url(self):
        return reverse('detail', args=[self.id])