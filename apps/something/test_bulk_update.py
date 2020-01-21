from bulk_update.helper import bulk_update

from apps.something.models import Something


def inbuilt(fields=10, objects=100_000, batch_size=1000):
    list_of_objects = list(Something.objects.all()[:objects])

    Something.objects.bulk_update(
        list_of_objects,
        ["relation1", "date1", "date2", "bool1", "bool2", "bool3", "int1", "int2", "int3", "datetime1"][:fields],
        batch_size=batch_size,
    )


def bulk_update_package(fields=10, objects=100_000, batch_size=1000):
    list_of_objects = list(Something.objects.all()[:objects])

    bulk_update(
        list_of_objects,
        update_fields=["relation1", "date1", "date2", "bool1", "bool2", "bool3", "int1", "int2", "int3", "datetime1"][
            :fields
        ],
        batch_size=batch_size,
    )


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
