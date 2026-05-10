def dag_write_string_to_s3(string, prefix, **kwargs):
    """Push a string in memory to s3 with a defined prefix"""
    access_id = kwargs.get('access_id')
    access_secret = kwargs.get('access_secret')
    bucket_name = kwargs.get('bucket_name')
    logging.info('Writing to S3 Bucket %s', bucket_name)
    our_hash = hashlib.md5(string.encode('utf-8')).hexdigest()
    filename = '{}/{}'.format(prefix, our_hash)
    process.generate_s3_object(string, bucket_name, filename, access_id, access_secret)