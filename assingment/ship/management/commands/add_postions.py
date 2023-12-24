from django.core.management.base import BaseCommand
import csv
from ship.models import Ship, ShipPosition


class Command(BaseCommand):
    """
    Management utility to add ship position data.
    """
    help = 'Used to add default ship positions for the app.'

    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **options):

        file_name = options["file_name"]
        with open(file_name) as f:
            for data in csv.reader(f):
                try:
                    ship, _ = Ship.objects.get_or_create(imo_number=data[0])
                    ShipPosition.objects.create(
                        ship=ship, timestamp=data[1],
                        latitude=data[2], longitude=data[3])
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"{ship} - Ship position data saved successfully"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(e))
