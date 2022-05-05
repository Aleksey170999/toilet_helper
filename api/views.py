from django.forms import model_to_dict
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from api.serializers import ToiletSerializer
from toilet_posts.models import Toilet
from rest_framework.response import Response


class ToiletListViewPersonolized(ListAPIView):
    serializer_class = ToiletSerializer

    def get_queryset(self):
        """
        Получение отфильтрованного списка записей,
        tg_id передается в представление через kwargs
        """
        return Toilet.objects.filter(user_tg_id=self.kwargs["tg_id"])


class ToiletListView(ListAPIView):
    model = Toilet
    serializer_class = ToiletSerializer
    queryset = Toilet.objects.filter(confirmed__exact=True)


class ToiletCreateView(APIView):

    def post(self, request):
        new_post = Toilet.objects.create(
            author=request.data['author'],
            address=request.data["address_from_geo"],
            description=request.data['description'],
            rating=request.data['rating'],
            location=request.data['location'],
            user_tg_id=request.data['user_tg_id'],
            confirmed=False,

        )
        return Response({'post': model_to_dict(new_post)})
