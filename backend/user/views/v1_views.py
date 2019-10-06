from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework_jwt.settings import api_settings
from config.common.common_library import *

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class SignIn(APIView):
    # permission_classes = ()
    # authentication_classes = ()

    def get(self, request):
        try:
            return Response(common_serializer(STATUS_RSP_SUCCESS))

        except APIException as e:
            raise APIException(e)

    def post(self, request):
        try:
            data = {'user': 'test', 'login_token': '1234'}
            return Response(common_serializer(STATUS_RSP_SUCCESS))

        except APIException as e:
            raise APIException(e)
