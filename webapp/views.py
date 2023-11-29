from django.shortcuts import render
from .models import WifiData  # Import your model
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WifiData
from .serializers import WifiDataSerializer


# Create your views here.

def landing_page(request):
    return render(request, 'webapp/landing.html')

def db_view(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'

    if query:
        # If there is a search query, filter the queryset based on the query
        wifi_data = WifiData.objects.filter(
            ssid__icontains=query) | WifiData.objects.filter(
            bssid__icontains=query)
    else:
        # If no search query, fetch all WifiData objects from the database
        wifi_data = WifiData.objects.all()

    return render(request, 'webapp/db.html', {'wifi_data': wifi_data, 'query': query})

class WifiDataCreateView(APIView):
    def get(self, request):
        network = WifiData.objects.all()
        serializer = WifiDataSerializer(network, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WifiDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
