from rest_framework.generics import RetrieveAPIView, CreateAPIView

from proposals.serializers import ProposalSerializer
from proposals.models import Proposal
from proposals.tasks import update_proposal_status


class ProposalCreateView(CreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def perform_create(self, serializer):
        proposal = serializer.save()
        update_proposal_status.delay(proposal.id)


class ProposalDetailView(RetrieveAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
