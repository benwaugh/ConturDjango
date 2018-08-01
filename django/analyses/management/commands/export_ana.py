from django.core.management import BaseCommand
from ...views import export

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('Report Name', nargs='+', type=str)


