from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from consultants.models import Filing

from .serializers import PublicFilingSerializer
from .models import Favorite
from consultants.models import Filing

# Create your views here.

class PublicFilingViewSet(viewsets.ModelViewSet):
    queryset = Filing.objects.filter(is_published=True).select_related("district", "consultant")
    serializer_class = PublicFilingSerializer
    permission_classes = [AllowAny]  


class ToggleFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, filing_id):
        filing = get_object_or_404(Filing, pk=filing_id)

        is_favorited = Favorite.objects.filter(user=request.user, filing=filing).exists()

        if is_favorited:
            Favorite.objects.filter(user=request.user, filing=filing).delete()

            return Response({"status": "removed"})
        else:
            favorite = Favorite(user=request.user, filing=filing)
            favorite.save()

            return Response({"status": "added"})


class ListFavoriteView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PublicFilingSerializer

    def get_queryset(self):
        return Filing.objects.filter(favorite__user=self.request.user)
            
        
