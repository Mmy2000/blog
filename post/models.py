from django.utils import timezone
from django.db import models

CATEGORY_CHIOSES = (
    ('WB','Web Development'),
    ('DB','Desktop Development'),
     ('DS','Data Science'),
)

class Post(models.Model):
    title = models.CharField(max_length=50,unique=True)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    views_count = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY_CHIOSES,max_length=20)




    def __str__(self) :
        return self.title