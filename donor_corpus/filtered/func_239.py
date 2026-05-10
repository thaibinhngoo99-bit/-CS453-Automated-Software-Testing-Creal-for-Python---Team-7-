def get_temporary_credentials(session, key_names=BOTO_CRED_KEYS, role_arn=None):
    sts_client = session.client('sts', endpoint_url=get_service_endpoint('sts', session.region_name), region_name=session.region_name)
    if role_arn:
        session_name = 'CloudFormationContractTest-{:%Y%m%d%H%M%S}'.format(datetime.now())
        try:
            response = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=session_name, DurationSeconds=900)
        except ClientError:
            LOG.debug('Getting session token resulted in unknown ClientError. ' + "Could not assume specified role '%s'.", role_arn)
            raise DownstreamError() from Exception("Could not assume specified role '{}'".format(role_arn))
        temp = response['Credentials']
        creds = (temp['AccessKeyId'], temp['SecretAccessKey'], temp['SessionToken'])
    else:
        frozen = session.get_credentials().get_frozen_credentials()
        if frozen.token:
            creds = (frozen.access_key, frozen.secret_key, frozen.token)
        else:
            try:
                response = sts_client.get_session_token(DurationSeconds=900)
            except ClientError as e:
                LOG.debug('Getting session token resulted in unknown ClientError', exc_info=e)
                raise DownstreamError('Could not retrieve session token') from e
            temp = response['Credentials']
            creds = (temp['AccessKeyId'], temp['SecretAccessKey'], temp['SessionToken'])
    return dict(zip(key_names, creds))