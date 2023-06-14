# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProposalSerializer

class ProposalCreateView(APIView):
    def post(self, request, format=None):
        serializer = ProposalSerializer(data=request.data)
        if serializer.is_valid():
            proposal = serializer.save()
            return Response({'id': proposal.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
