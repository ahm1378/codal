
from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(verbose_name="title", max_length=100)
    symbol = models.CharField(verbose_name="symbol", max_length=100)
    company_name = models.CharField(verbose_name="company_name", max_length=100)
    create_at = models.DateTimeField(verbose_name="Create at", auto_now_add=True)
    publish_date = models.DateTimeField()
    url = models.URLField()
    update_at = models.DateTimeField(verbose_name="Update at", auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "post"

    def __str__(self):
        return self.title


class Page(models.Model):
    post = models.OneToOneField(to=Post, on_delete=models.CASCADE)
    html = models.FileField(
        verbose_name="html", upload_to="crawl/files/")
    create_at = models.DateTimeField(verbose_name="Create at", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Update at", auto_now=True)



# Create your models here.
