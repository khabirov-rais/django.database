import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)
            # Phone.objects.all().delete()

            for line in phone_reader:
                Phone.objects.create(
                    id=line[0],
                    name=line[1],
                    price=line[3],
                    image=line[2],
                    release_date=line[4],
                    lte_exists=line[5],
                    slug='-'.join(line[1].split(' '))
                )
