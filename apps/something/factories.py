import factory
from django.utils import timezone

from apps.something.models import SomethingElse, Something


class SomethingElseFactory(factory.django.DjangoModelFactory):

    char1 = factory.Faker("pystr")

    class Meta:
        model = SomethingElse


class SomethingFactory(factory.django.DjangoModelFactory):
    date1 = factory.Faker("date_object")
    date2 = factory.Faker("date_object")
    bool1 = factory.Faker("pybool")
    bool2 = factory.Faker("pybool")
    bool3 = factory.Faker("pybool")
    int1 = factory.Faker("pyint")
    int2 = factory.Faker("pyint")
    int3 = factory.Faker("pyint")
    datetime1 = factory.LazyAttribute(lambda obj: timezone.now())

    class Meta:
        model = Something

    @classmethod
    def fast_create_batch(cls, size, **kwargs):
        Something.objects.bulk_create([cls.build(**kwargs) for _ in range(size)])
