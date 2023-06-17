from django.contrib import admin

from proposals.models import Proposal


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'cpf', 'value', 'address', 'status']
    list_filter = ['cpf', 'status']
    search_fields = ['name', 'cpf', 'address']
    list_editable = ['status']
