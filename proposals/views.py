# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from .serializers import ProposalSerializer
from proposals.models import Proposal

class ProposalCreateView(CreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        proposal = response.data
        return Response({'id': proposal['id']}, status=status.HTTP_201_CREATED)

class ProposalDetailView(RetrieveAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
