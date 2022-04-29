from django.forms import model_to_dict
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from api.serializers import ToiletLocationSerializer, ToiletSerializer
from toilet_posts.models import Toilet, Author
from rest_framework.response import Response


class ToiletListView(ListAPIView):
    model = Toilet
    serializer_class = ToiletSerializer
    queryset = Toilet.objects.filter(confirmed__exact=True)


class ToiletCreateView(APIView):

    def post(self, request):
        new_post = Toilet.objects.create(
            author=request.data['user_name'],
            description=request.data['description'],
            rating=request.data['rating'],
            address=request.data['address'],
            location=request.data['location'],
            user_tg_id=request.data['user_tg_id']
        )

        return Response({'post': model_to_dict(new_post)})
