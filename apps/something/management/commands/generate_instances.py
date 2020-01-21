from django.core.management.base import BaseCommand

from apps.something.factories import SomethingElseFactory, SomethingFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(100):
            something_else = SomethingElseFactory()

            SomethingFactory.fast_create_batch(10_000, relation1=something_else)
            print(i)
