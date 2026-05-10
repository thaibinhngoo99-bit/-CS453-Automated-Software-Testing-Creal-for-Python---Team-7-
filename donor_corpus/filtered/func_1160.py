def sync_detailed(output_format: FileConversionOutputFormat, src_format: FileConversionSourceFormat, body: bytes, *, client: Client) -> Response[Union[Any, FileConversionWithOutput, Error]]:
    kwargs = _get_kwargs(output_format=output_format, src_format=src_format, body=body, client=client)
    response = httpx.post(verify=client.verify_ssl, **kwargs)
    return _build_response(response=response)