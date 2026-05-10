def get_presigned_url(session, bucket_name, object_name, region_name, expire_seconds, user_id, method='GET'):
    timez = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    datez = timez[:8]
    hostname = '{0}.s3{1}.amazonaws.com'.format(bucket_name, '.' + region_name if region_name != 'us-east-1' else '')
    cred = session['Credentials']['AccessKeyId']
    secret = session['Credentials']['SecretAccessKey']
    token = session['Credentials']['SessionToken']
    aws4_request = '/'.join([datez, region_name, 's3', 'aws4_request'])
    cred_string = '{0}/{1}'.format(cred, aws4_request)
    parts = ['A-userid={0}'.format(user_id), 'X-Amz-Algorithm=AWS4-HMAC-SHA256', 'X-Amz-Credential=' + urllib.parse.quote_plus(cred_string), 'X-Amz-Date=' + timez, 'X-Amz-Expires={0}'.format(expire_seconds), 'X-Amz-Security-Token=' + urllib.parse.quote_plus(token), 'X-Amz-SignedHeaders=host']
    can_query_string = '&'.join(parts)
    can_req = method + '\n/' + object_name + '\n' + can_query_string + '\nhost:' + hostname + '\n\nhost\nUNSIGNED-PAYLOAD'
    can_req_hash = sha256(can_req.encode('utf-8')).hexdigest()
    stringtosign = '\n'.join(['AWS4-HMAC-SHA256', timez, aws4_request, can_req_hash])
    StepOne = hmacsha256('AWS4{0}'.format(secret).encode('utf-8'), datez).digest()
    StepTwo = hmacsha256(StepOne, region_name).digest()
    StepThree = hmacsha256(StepTwo, 's3').digest()
    SigningKey = hmacsha256(StepThree, 'aws4_request').digest()
    Signature = hmacsha256(SigningKey, stringtosign).hexdigest()
    url = 'https://' + hostname + '/' + object_name + '?' + can_query_string + '&X-Amz-Signature=' + Signature
    return url