from utils.utils import validate_parameters

get_news_query_schema = {
    "from": {
        "type": "integer",
        'coerce': int,
        "min": 0,
        "max": 10000,
        "required": False,
        "default": 0
    },
    "limit": {
        "type": "integer",
        'coerce': int,
        "min": 0,
        "max": 10000,
        "required": False,
        "default": 0
    },
    "category": {
        "type": "string",
        "required": False
    }
}

class GetNewsValidator:

    def __call__(self, request):
        body_validation_errors = validate_parameters(request.args.copy(), get_news_query_schema)
        return body_validation_errors