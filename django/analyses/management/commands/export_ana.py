from django.core.management import BaseCommand
from ...views import export

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('Report Name', nargs='+', type=str)

    def handle(self, *args, **options):
        for ana_file in options['Report Name']:
            data = export("Dark_Matter_Test")
            f = open(str(ana_file) + ".ana","w+")
            i = 0;
            for line in data.split("\n"):
                if len(line) > 5 and i > 0:
                    f.write("insert Rivet:Analyses 0 " + line + "\n")
                i += 1
            f.close()
