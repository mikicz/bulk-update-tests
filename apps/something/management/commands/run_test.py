from django.core.management.base import BaseCommand

from apps.something.test_bulk_update import inbuilt, bulk_update_package


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("way")

    def handle(self, *args, **options):
        way = options.get("way")
        if way == "inbuilt":
            inbuilt()
        else:
            bulk_update_package()
