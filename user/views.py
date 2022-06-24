from django.http import HttpResponse
from rest_framework import status as httpStatus
from rest_framework.decorators import api_view
from rest_framework.response import Response


users = [
    {
        "userId": 1,
        "userName": 'ashutosh',
    },
    {
        "userId": 2,
        "userName": 'gary',
    },
]


# Create your views here.
@api_view(['GET'])
def index(request):
    return HttpResponse('<center><h1>Welcome to AWS-Test :)</h1></center>')


@api_view(["GET"])
def get_user_list(request):
    try:
        if len(users) > 0:
            result = {"data": users}
            return Response(result, status=httpStatus.HTTP_200_OK)
        else:
            return Response({'message': "No user found"}, status=httpStatus.HTTP_404_NOT_FOUND)
    except Exception as e:
        print('.....verify_referral exception.....\n', str(e))
        return Response({'error': "Something went wrong"}, status=httpStatus.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def add_user(request):
    try:
        if request.data.get("userId") and request.data.get("userName"):
            users.append({
                "userId": request.data.get("userId"),
                "userName": request.data.get("userName")
            })
            result = {"message": "User Added"}
            return Response(result, status=httpStatus.HTTP_200_OK)
        else:
            return Response({'message': "Request invalid"}, status=httpStatus.HTTP_404_NOT_FOUND)
    except Exception as e:
        print('.....verify_referral exception.....\n', str(e))
        return Response({'error': "Something went wrong"}, status=httpStatus.HTTP_500_INTERNAL_SERVER_ERROR)
