async def asyncio_detailed(output_format: FileConversionOutputFormat, src_format: FileConversionSourceFormat, body: bytes, *, client: Client) -> Response[Union[Any, FileConversionWithOutput, Error]]:
    kwargs = _get_kwargs(output_format=output_format, src_format=src_format, body=body, client=client)
    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)
    return _build_response(response=response)