from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Member

# Create your views here.

class MemberList(ListView):
    model = Member 
    context_object_name = 'members'
    template_name = 'team/member_list.html'

class MemberCreate(CreateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('members')
    template_name = 'team/member_create.html'
    

class MemberUpdate(UpdateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('members')
    template_name = 'team/member_update.html'

class MemberDelete(DeleteView):
    model = Member
    context_object_name = 'member'
    success_url = reverse_lazy('members')
    template_name = 'team/member_delete.html'