import time

from django.core.management.base import BaseCommand
from tqdm import tqdm, trange

from apps.experiments.models import Experiment
from apps.something.test_bulk_update import get_all_combos, inbuilt, bulk_update_package


class Command(BaseCommand):
    def handle(self, *args, **options):
        batch_size = 1000

        all_combos = list(get_all_combos())

        for size in tqdm([1_000, 2_500, 5_000, 10_000, 25_000, 50_000]):
            for _ in trange(5, leave=False):
                for field_types in tqdm(all_combos, leave=False):
                    field_types_str = ",".join(field_types)

                    start = time.time()
                    fields = inbuilt(types=field_types, objects=size, batch_size=batch_size)
                    inbuilt_duration = time.time() - start
                    Experiment.objects.create(
                        method=Experiment.INBUILT,
                        field_types=field_types_str,
                        fields=fields,
                        count=size,
                        batch_size=batch_size,
                        time=inbuilt_duration,
                    )

                    start = time.time()
                    bulk_update_package(types=field_types, objects=size, batch_size=batch_size)
                    package_duration = time.time() - start
                    Experiment.objects.create(
                        method=Experiment.PACKAGE,
                        field_types=field_types_str,
                        fields=fields,
                        count=size,
                        batch_size=batch_size,
                        time=package_duration,
                    )
