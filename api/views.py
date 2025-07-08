from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response (
            {
                "Status": "OK"
            }

        )

health_view = HealthView.as_view()


#
# Book Resources
# /api/books
#

class BookView(APIView):
    def get(self, request, *args, **kwargs):
        return Response (
            {
                "hello": "django"
            }

        )

book_view = BookView.as_view()