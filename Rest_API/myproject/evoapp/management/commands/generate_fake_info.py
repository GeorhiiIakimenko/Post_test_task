from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = 'Generates fake data for the database'

    def handle(self, *args, **options):
        fake = Faker()


