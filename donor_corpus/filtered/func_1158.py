def _get_kwargs(output_format: FileConversionOutputFormat, src_format: FileConversionSourceFormat, body: bytes, *, client: Client) -> Dict[str, Any]:
    url = '{}/file/conversion/{src_format}/{output_format}'.format(client.base_url, output_format=output_format, src_format=src_format)
    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()
    return {'url': url, 'headers': headers, 'cookies': cookies, 'timeout': client.get_timeout(), 'content': body}