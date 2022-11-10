from urllib.request import urlopen

from django.core.management import BaseCommand
from crawl.models import Post,Page
from django.core.files import File as DjangoFile


class Command(BaseCommand):
    help = 'Create random users'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        i = 0
        for post in posts:
            req_url = 'https://www.codal.ir' + post.url
            with urlopen(req_url) as response:
                body = response.read()
            mystr = body.decode("utf8")
            file_name = "crawl/files/{}.html".format(i)
            with open(file_name, 'w+', encoding='utf-8') as file:
                file.write(str(mystr))
            file_obj1 = DjangoFile(open(file_name, mode='rb'), name=file_name)
            Page.objects.create(post=post, html=file_obj1)
            i += 1
