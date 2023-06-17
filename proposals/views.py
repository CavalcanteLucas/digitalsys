from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from proposals.serializers import ProposalSerializer
from proposals.tasks import update_proposal_status


class ProposalCreateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'proposal_create.html'

    def get(self, request):
        serializer = ProposalSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = ProposalSerializer(data=request.data)
        if serializer.is_valid():
            proposal = serializer.save()
            update_proposal_status.delay(proposal.id)
            return Response({'success': True})
        return Response({'serializer': serializer})
