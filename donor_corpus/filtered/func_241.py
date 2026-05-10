def get_account(session, temporary_credentials):
    sts_client = session.client('sts', endpoint_url=get_service_endpoint('sts', session.region_name), region_name=session.region_name, aws_access_key_id=temporary_credentials['accessKeyId'], aws_secret_access_key=temporary_credentials['secretAccessKey'], aws_session_token=temporary_credentials['sessionToken'])
    response = sts_client.get_caller_identity()
    return response.get('Account')