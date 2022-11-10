import json
from datetime import datetime
from urllib.request import urlopen

from django.core.management.base import BaseCommand

from crawl.models import Post
from crawl.taghvim import jalali_to_gregorian


class Command(BaseCommand):
    help = 'get posts from codal'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            url = "https://search.codal.ir/api/search/v2/q?&Audited=true&AuditorRef=-1&Category=-1&Childs=true&CompanyState=-1&CompanyType=-1&Consolidatable=true&IsNotAudited=false&Length=-1&LetterType=-1&Mains=true&NotAudited=true&NotConsolidatable=true&PageNumber={}&Publisher=false&TracingNo=-1&search=false".format(
                i+1)
            with urlopen(url) as response:
                body = response.read()

            todo_item = json.loads(body)
            for item in todo_item['Letters']:
                year = int(item['PublishDateTime'].split('/')[0])
                month = int(item['PublishDateTime'].split('/')[1])
                day = int(item['PublishDateTime'].split('/')[2].split()[0])
                publish_date = jalali_to_gregorian(jy=year, jm=month, jd=day)
                dates = datetime(year=publish_date[0], month=publish_date[1], day=publish_date[2])
                Post.objects.create(url=item['Url'], title=item['Title'], company_name=item['CompanyName'],
                                    symbol=item['Symbol'], publish_date=dates)
