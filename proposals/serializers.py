from rest_framework import serializers

from proposals.models import Proposal


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'name', 'value', 'status']
