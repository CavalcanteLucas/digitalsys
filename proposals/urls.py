from django.urls import path

from proposals.views import ProposalCreateView


urlpatterns = [
    path('', ProposalCreateView.as_view(), name='proposal-create'),
]
