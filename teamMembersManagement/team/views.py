from django.shortcuts import render, redirect

from .models import Member
from .forms import MemberForm

# Create your views here.

def index(request):
    members = Member.objects.all()
    form = MemberForm()

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'members': members, 'form': form}
    return render(request, 'team/list.html', context)
