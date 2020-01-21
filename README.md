# Bulk Update Tests

For comparison of performance of bulk update using the new inbuilt Django method and the package django-bulk-update.

Basic comparison using PostgreSQL 11.5 on this example project.

```
In [1]: Something.objects.count()                                                                                                                                                                                                             
Out[1]: 1008895

In [2]: from apps.something.test_bulk_update import *                                                                                                                                                                                         

In [3]: %time inbuilt()                                                                                                                                                                                                                       
CPU times: user 2min 9s, sys: 653 ms, total: 2min 10s
Wall time: 2min 24s

In [4]: %time bulk_update_package()                                                                                                                                                                                                           
CPU times: user 11.2 s, sys: 41.6 ms, total: 11.3 s
Wall time: 24.2 s
```

PyInstrument profiling available in folder `pyinstrument`.
