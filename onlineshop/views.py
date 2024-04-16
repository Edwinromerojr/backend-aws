from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializers

# Create your views here.

class OrderView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializers(orders, many=True)
            return Response({
                'date': serializer.orders,
                'message': "Orders Data fetched successfully"
            }, status = status.HTTP_200_OK)
        except:
            return Response({
                'date': {},
                'message': "Something went wrong while fetching the data"
            }, status = status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            serializer = OrderSerializers(data=data)

            if not serializer.is_valid():
                return Response({
                    'date': serializer.errors,
                    'message': "Something went wrong"
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({
                'date': serializer.data,
                'message': "New order is created"
            }, status = status.HTTP_201_CREATED)
        except:
            return Response({
                'date': {},
                'message': "Something went wrong in creation of order"
            }, status = status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id=data.get('id'))

            if not order.exists():
                return Response({
                    'date': {},
                    'message': "Order is not found with this ID"
                }, status = status.HTTP_404_NOT_FOUND)

            serializer = OrderSerializers(order[0], data=data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'date': serializer.errors,
                    'message': "Something went wrong"
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'date': serializer.data,
                'message': "Order is updated successfully"
            }, status = status.HTTP_200_OK)

        except:
            return Response({
                'date': {},
                'message': "Something went wrong in creation of order"
            }, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id=data.get('id'))

            if not order.exists():
                return Response({
                    'date': {},
                    'message': "Order is not found with this ID"
                }, status = status.HTTP_404_NOT_FOUND)

            order[0].delete()
            return Response({
                'date': {},
                'message': "Order is Deleted"
            }, status = status.HTTP_200_OK)
        except:
            return Response({
                'date': {},
                'message': "Something went wrong in deleting the order"
            }, status = status.HTTP_400_BAD_REQUEST)
