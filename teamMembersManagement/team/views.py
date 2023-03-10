from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Member
from .forms import MemberForm

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
    



def ListTeam(request):
    members = Member.objects.all()
    form = MemberForm()

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'members': members, 'form': form}
    return render(request, 'team/list.html', context)

def updateMember(request, pk):
    member = Member.objects.get(id = pk)
    form = MemberForm(instance = member)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    # elif request.method == 'DELETE':
    #     print("HELLO WORLD")
    #     member.delete()
    #     return redirect('/')


    context = {'form': form}
    return render(request, 'team/update_member.html', context)