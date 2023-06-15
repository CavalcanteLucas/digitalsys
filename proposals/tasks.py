from celery import shared_task

from proposals.models import Proposal


@shared_task
def update_proposal_status(proposal_id):
    try:
        proposal = Proposal.objects.get(id=proposal_id)
        proposal.status = 'approved'
        proposal.save()
        return proposal.id
    except Proposal.DoesNotExist:
        pass
