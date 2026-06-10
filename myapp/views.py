from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
import logging

from .serializers import SensorReadingSerializer, UserSerializer, NoteSerializer, UploadedImageSerializer
from .models import Note, UploadedImage, SensorReading, StockMarketReading

logger = logging.getLogger(__name__)


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            logger.error(f"NoteListCreate validation errors: {serializer.errors}")
            raise serializers.ValidationError(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ChartDataView2(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            readings = StockMarketReading.objects.all().order_by('timestamp')
            x = [r.timestamp.strftime('%Y-%m-%d %H:%M:%S') for r in readings]
            y = [r.value1 for r in readings]
            chart_data = {
                "data": [
                    {
                        "x": x,
                        "y": y,
                        "type": "scatter",
                        "mode": "lines+markers",
                        "name": "Stock Market Data",
                    }
                ],
                "layout": {
                    "title": "Stock Market Data",
                    "xaxis": {"title": "Time"},
                    "yaxis": {"title": "Value"},
                }
            }
            return Response(chart_data)
        except Exception as e:
            logger.error(f"ChartDataView2 error: {str(e)}")
            return Response({"error": str(e)}, status=400)


class ChartDataView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            readings = SensorReading.objects.all().order_by('timestamp')
            x = [r.timestamp.strftime('%Y-%m-%d %H:%M:%S') for r in readings]
            y = [r.value for r in readings]

            chart_data = {
                "data": [
                    {
                        "x": x,
                        "y": y,
                        "type": "scatter",
                        "mode": "lines+markers",
                        "name": "Sensor Data",
                    }
                ],
                "layout": {
                    "title": "Sensor Data",
                    "xaxis": {"title": "Time"},
                    "yaxis": {"title": "Value"},
                }
            }
            return Response(chart_data)
        except Exception as e:
            logger.error(f"ChartDataView error: {str(e)}")
            return Response({"error": str(e)}, status=400)


class ImageListView(generics.ListAPIView):
    queryset = UploadedImage.objects.all().order_by('-uploaded_at')
    serializer_class = UploadedImageSerializer
    permission_classes = [AllowAny]


class ImageUploadView(generics.CreateAPIView):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny]
