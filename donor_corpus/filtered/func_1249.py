def load_database_url_from_vcap_services(name: str, service: str, env: Environ=os.environ) -> str:
    """
    Sets os.environ[DATABASE_URL] from a service entry in VCAP_SERVICES.
    """
    if not is_on_cloudfoundry(env):
        return
    vcap = json.loads(env['VCAP_SERVICES'])
    env['DATABASE_URL'] = vcap[service][0]['credentials']['uri']