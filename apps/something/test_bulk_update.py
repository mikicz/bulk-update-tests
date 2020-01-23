import itertools

from bulk_update.helper import bulk_update

from apps.something.models import Something

db_fields = {
    "relation1": "relationship",
    "date1": "date",
    "date2": "date",
    "bool1": "bool",
    "bool2": "bool",
    "bool3": "bool",
    "int1": "int",
    "int2": "int",
    "int3": "int",
    "datetime1": "datetime",
}


def get_all_combos():
    types = list(set(db_fields.values()))
    for x in itertools.chain(
        itertools.combinations(types, 1),
        itertools.combinations(types, 2),
        itertools.combinations(types, 3),
        itertools.combinations(types, 4),
        itertools.combinations(types, 5),
    ):
        yield set(x)


def get_fields(types):
    if not types:
        return list(db_fields.keys())

    return [k for k, v in db_fields.items() if v in types]


def inbuilt(types=None, single=False, objects=100_000, batch_size=1000):
    list_of_objects = list(Something.objects.all()[:objects])

    fields = get_fields(types)

    if len(types) == 1 and single:
        fields = fields[:1]

    Something.objects.bulk_update(list_of_objects, fields, batch_size=batch_size)

    return len(fields)


def bulk_update_package(types=None, single=False, objects=100_000, batch_size=1000):
    list_of_objects = list(Something.objects.all()[:objects])

    fields = get_fields(types)

    if len(types) == 1 and single:
        fields = fields[:1]

    bulk_update(list_of_objects, update_fields=fields, batch_size=batch_size)

    return len(fields)


"""
In [1]: Something.objects.count()                                                                                                                                                                                                             
Out[1]: 1008895

In [2]: from apps.something.test_bulk_update import *                                                                                                                                                                                         

In [3]: %time                                                                                                                                                                                                                                 
CPU times: user 2 µs, sys: 0 ns, total: 2 µs
Wall time: 3.58 µs

In [4]: %time inbuilt()                                                                                                                                                                                                                       
CPU times: user 2min 9s, sys: 653 ms, total: 2min 10s
Wall time: 2min 24s

In [5]: %time bulk_update_package()                                                                                                                                                                                                           
CPU times: user 11.2 s, sys: 41.6 ms, total: 11.3 s
Wall time: 24.2 s
"""
