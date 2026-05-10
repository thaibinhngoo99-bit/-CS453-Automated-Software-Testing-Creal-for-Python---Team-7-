def reset_secuence(table, column_name='id', schema_name='public'):
    table_name = f'{schema_name}.{table.__tablename__}'
    sql = f"SELECT pg_get_serial_sequence('{table_name}', '{column_name}');"
    secuence_name = database.engine.execute(sql).fetchone()[0]
    if secuence_name is not None:
        sql = f'ALTER SEQUENCE {secuence_name} RESTART WITH 1;'
        database.engine.execute(sql)