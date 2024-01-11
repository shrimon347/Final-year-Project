from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.models import User
from .models import Notes
from datetime import date
from .forms import NoteForm
from django.db.models import Q
from django.core.paginator import Paginator
# note shareing views here started

def note(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    users = User.objects.all()
    # pagination 
    Notedata = Notes.objects.filter(status=True and
        Q(subject__icontains=q) |
        Q(branch__icontains=q) |
        Q(description__icontains=q)
    )
    Note_count = Notes.objects.filter(status=True).count()
    
    page = Paginator(Notedata, 5)
    page_number = request.GET.get('page')
    NoteDataFinal = page.get_page(page_number)
    totalpage = NoteDataFinal.paginator.num_pages
    context = {'data':NoteDataFinal, 'note_count':Note_count, 'users':users, 'lastpage':totalpage,'totalpagelist':[n+1 for n in range (totalpage)],'page':page_number}
    return render(request,'note/note.html',context)


@login_required(login_url='/login')
def upload_notes(request):
    error=""
    form = NoteForm()
    if request.method=='POST':
        b = request.POST.get('branch')
        s = request.POST.get('subject')
        n = request.FILES.get('notesfile')
        f = request.POST.get('filetype')
        d = request.POST.get('description')
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,
                                 filetype=f,description=d)
            error="no"
        except:
            error="yes"
    context = {'form':form}
    return render(request,'note/upload_note.html',context)

def my_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user=user)
    print(notes)

    context = {'notes':notes}
    return render(request, 'note/my_notes.html',context)




def delete_mynotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('my_notes')


