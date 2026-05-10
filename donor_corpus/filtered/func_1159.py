def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FileConversionWithOutput, Error]]:
    if response.status_code == 201:
        response_201 = FileConversionWithOutput.from_dict(response.json())
        return response_201
    if response.status_code == 400:
        response_4XX = Error.from_dict(response.json())
        return response_4XX
    if response.status_code == 500:
        response_5XX = Error.from_dict(response.json())
        return response_5XX
    return None