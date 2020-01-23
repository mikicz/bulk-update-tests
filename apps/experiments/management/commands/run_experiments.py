import time

from django.core.management.base import BaseCommand
from tqdm import tqdm, trange

from apps.experiments.models import Experiment
from apps.something.test_bulk_update import get_all_combos, inbuilt, bulk_update_package


class Command(BaseCommand):
    def handle(self, *args, **options):
        batch_size = 1000

        for size in tqdm([1_000, 2_500, 5_000, 10_000, 25_000, 50_000, 75_000]):
            for field_types in tqdm(["relationship", "date", "bool", "int", "datetime"], leave=False):
                field_types = set([field_types])
                field_types_str = ",".join(field_types)

                count = (
                    5
                    - Experiment.objects.filter(
                        method=Experiment.INBUILT,
                        field_types=field_types_str,
                        fields=1,
                        count=size,
                        batch_size=batch_size,
                    ).count()
                )
                count = max(count, 0)

                for _ in trange(count, leave=False):
                    start = time.time()
                    inbuilt(types=field_types, objects=size, batch_size=batch_size, single=True)
                    inbuilt_duration = time.time() - start
                    Experiment.objects.create(
                        method=Experiment.INBUILT,
                        field_types=field_types_str,
                        fields=1,
                        count=size,
                        batch_size=batch_size,
                        time=inbuilt_duration,
                    )

                count = (
                    5
                    - Experiment.objects.filter(
                        method=Experiment.PACKAGE,
                        field_types=field_types_str,
                        fields=1,
                        count=size,
                        batch_size=batch_size,
                    ).count()
                )
                count = max(count, 0)

                for _ in trange(count, leave=False):
                    start = time.time()
                    bulk_update_package(types=field_types, objects=size, batch_size=batch_size, single=True)
                    package_duration = time.time() - start
                    Experiment.objects.create(
                        method=Experiment.PACKAGE,
                        field_types=field_types_str,
                        fields=1,
                        count=size,
                        batch_size=batch_size,
                        time=package_duration,
                    )
