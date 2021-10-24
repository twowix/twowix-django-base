from rest_framework.views import exception_handler
from rest_framework import exceptions
from rest_framework.response import Response
from config.common.library import *
from rest_framework import status


def cus_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, exceptions.ParseError):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.AuthenticationFailed):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.NotAuthenticated):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.PermissionDenied):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.NotFound):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.MethodNotAllowed):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.NotAcceptable):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.UnsupportedMediaType):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.Throttled):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.ValidationError):
            code = response.status_code
            msg = exc.detail
        elif isinstance(exc, exceptions.APIException):
            code = int(exc.detail)
            msg = code_to_message(code)
        else:
            code = response.status_code
            msg = "unknown error"

        response.data['code'] = code
        response.data['message'] = msg
        response.data['data'] = None
        del response.data['detail']
        return response

    else:
        print("ER|%s| %s" % (exc, context))
        return Response(common_serializer(STATUS_RSP_INTERNAL_ERROR), status=status.HTTP_500_INTERNAL_SERVER_ERROR)