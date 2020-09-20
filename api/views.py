import json

from rest_framework.response import Response
from rest_framework.views import APIView

from .errors import USER_ALREADY_EXISTS
from .models import User
from .serializers import UserSerializer
from .utils import make_response_payload


class Register(APIView):
    def post(self, request):
        if request.META["CONTENT_TYPE"] != "application/json":
            return

        body = json.loads(request.body)

        if User.objects.filter(email=body["email"]).exists():
            return Response(make_response_payload(is_success=False, message=USER_ALREADY_EXISTS), status=409)

        user = User.objects.create_user(email=body["email"], realname=body["realname"],
                                        username=body["username"],
                                        password=body["password"])

        result = UserSerializer(user).data

        return Response(make_response_payload(result))
