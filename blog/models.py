from django.db import models

# Create your models here.
class MyPost(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.title