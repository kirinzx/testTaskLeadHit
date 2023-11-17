from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .formSearcher import FormSearcher

class RetrieveFormView(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        form = request.data
        try:
            searcher = FormSearcher(form)
        except TypeError:
            return Response(data={'error': 'Форма содержит неподдерживаемые типы данных'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=searcher.findMatching())
