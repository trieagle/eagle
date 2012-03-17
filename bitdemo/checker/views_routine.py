from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from checker.models import Routine,Status,Case,Casething
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from bitdemo.checker.myforms import AddRoutineForm,CasethingForm

import datetime

def get_lists(request):
    template_var={}
    if request.user.is_authenticated():
        
        u_id = request.user.id
        routine_list = Routine.objects.filter(owner=u_id).order_by('-start_date')[:100]
        status_list = Status.objects.filter(user=u_id)
        todo_list = []
        done_list = []
        casething_list = []
        
        for rt in routine_list:
            mod = rt.mode
            done = False
            st = status_list.filter(routine=rt.pk).order_by('-date')
            if st:
                d = st[0].date
                cur = datetime.datetime.now()
                if mod == 0:
                    done = True
                elif mod == 1:
                    if d.day>=cur.day:
                        done= True
                elif mod == 2:
                    if d.day>=cur.day-datetime.datetime.weekday(cur)+1:
                        done= True
                elif mod == 3:
                    if d.month>=cur.month:
                        done= True
                else:
                    if d.year>=cur.year:
                        done= True
            if done:
                done_list.append(rt)
            else:
                todo_list.append(rt)
            
        template_var["todo_list"]=todo_list
        template_var["done_list"]=done_list
    return template_var
    
        
def add_routine(request):
    template_var={}
    form = AddRoutineForm()    
    if request.method == 'POST':
        form=AddRoutineForm(request.POST.copy())
        if form.is_valid():
            _add_routine(request,form)
            return HttpResponseRedirect(reverse("main"))
    template_var["form"]=form      
    return render_to_response("checker/addRoutine.html",template_var,context_instance=RequestContext(request))

def _add_routine(request,form):
    '''core func of add op'''
    res = False
    r = Routine()
    r.title = form.cleaned_data["title"]
    r.details = form.cleaned_data["details"]
    r.owner = request.user
    r.start_date = form.cleaned_data["start_date"]
    r.end_date = form.cleaned_data["end_date"]
    r.mode = form.cleaned_data["mode"]
    r.save()
    res = True
    return res

def remove_routine(request,r_id):
    r = get_object_or_404(Routine,pk=r_id)
    if r:
        r.delete()
    else:
        raise HttpResponse('no routine found! remove failed!')
    return HttpResponseRedirect(reverse("main"))

def show_routine(request,r_id):
    r = get_object_or_404(Routine,pk=r_id)
    if request.method == 'POST':
        form=AddRoutineForm(request.POST.copy())
        if form.is_valid():
            r.title = form.cleaned_data["title"]
            r.details = form.cleaned_data["details"]
            r.owner = request.user
            r.start_date = form.cleaned_data["start_date"]
            r.end_date = form.cleaned_data["end_date"]
            r.mode = form.cleaned_data["mode"]
            r.save()
    else:
        form=AddRoutineForm({'title':r.title,
                             'details':r.details,
                             'mode':r.mode,
                             'start_date':r.start_date,
                             'end_date':r.end_date})

    form.title = 'edit fails'
    return render_to_response("checker/showRoutine.html",{'form':form,'r_id':r_id},context_instance=RequestContext(request))

def done_routine(request,r_id):
    u = request.user
    ra = 1
    r = Routine.objects.get(pk=r_id)
    d = datetime.datetime.now()
    status = Status(routine=r,user=u,rate=ra,date=d)
    status.save()
    return HttpResponseRedirect(reverse("main"))

def undone_routine(request,r_id):
    u_id=request.user.id
    st = Status.objects.filter(routine=r_id,user=u_id).latest("date")
    if st:
        st.delete()
    return HttpResponseRedirect(reverse("main"))













