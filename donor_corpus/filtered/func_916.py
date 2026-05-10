def _test():
    import os
    import doctest
    import tempfile
    from pyspark.context import SparkContext
    from pyspark.sql import Row, SQLContext
    import pyspark.sql.context
    os.chdir(os.environ['SPARK_HOME'])
    globs = pyspark.sql.context.__dict__.copy()
    sc = SparkContext('local[4]', 'PythonTest')
    globs['tempfile'] = tempfile
    globs['os'] = os
    globs['sc'] = sc
    globs['sqlContext'] = SQLContext(sc)
    globs['rdd'] = rdd = sc.parallelize([Row(field1=1, field2='row1'), Row(field1=2, field2='row2'), Row(field1=3, field2='row3')])
    globs['df'] = rdd.toDF()
    jsonStrings = ['{"field1": 1, "field2": "row1", "field3":{"field4":11}}', '{"field1" : 2, "field3":{"field4":22, "field5": [10, 11]},"field6":[{"field7": "row2"}]}', '{"field1" : null, "field2": "row3", "field3":{"field4":33, "field5": []}}']
    globs['jsonStrings'] = jsonStrings
    globs['json'] = sc.parallelize(jsonStrings)
    failure_count, test_count = doctest.testmod(pyspark.sql.context, globs=globs, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
    globs['sc'].stop()
    if failure_count:
        exit(-1)