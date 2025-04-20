from textwrap import shorten

from rest_framework.views import exception_handler


def exception_handler_with_http_code(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data["code"] = response.status_code
    return response


def shorten_text(content, n_chars=20):
    return shorten(text=content, width=n_chars, placeholder="...")
