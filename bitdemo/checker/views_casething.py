from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from checker.models import Routine,Status,Case,Casething
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from bitdemo.checker.myforms import CasethingForm
import datetime

  
def add_casething(request):
    template_var={}
    form = CasethingForm()    
    if request.method == 'POST':
        form=CasethingForm(request.POST.copy())
        if form.is_valid():
            _add_casething(request,form)
            return HttpResponseRedirect(reverse("main"))
        else:
            return HttpResponse("CasethingForm is not valid")
    template_var["form"]=form      
    return render_to_response("checker/addCasething.html",template_var,context_instance=RequestContext(request))

def _add_casething(request,form):
    '''core func of add op'''
    res = False
    r = Casething()
    r.title = form.cleaned_data["title"]
    r.details = form.cleaned_data["details"]
    r.owner = request.user
    r.setup_date = form.cleaned_data["setup_date"]
    case_name = form.cleaned_data["case"]
    r.case = add_case(request,case_name)
    r.save()
    res = True
    return res

def add_case(request,case_name):
    ##some thing wrong may because name is not unique?
    ##case,created = Case.objects.get_or_create(name=case_name)
    try:
        case = Case.objects.get(name=case_name,user=request.user)
    except Case.DoesNotExist:
        case = Case(name=case_name,user=request.user,setup_date = datetime.datetime.now())
        case.save()
    return case

def remove_casething(request,c_id):
    c = get_object_or_404(Casething,pk=c_id)
    if c:
        c.delete()
    else:
        raise HttpResponse('no casething found! remove failed!')
    return HttpResponseRedirect(reverse("main"))

def show_casething(request,c_id):
    c = get_object_or_404(Casething,pk=c_id)
    if request.method == 'POST':
        form=CasethingForm(request.POST.copy())
        if form.is_valid():
            c.title = form.cleaned_data["title"]
            c.details = form.cleaned_data["details"]
            c.owner = request.user
            c.setup_date = form.cleaned_data["setup_date"]
            c.save()
    else:
        form=CasethingForm({'title':c.title,
                             'details':c.details,
                             'case':c.case,
                             'setup_date':c.setup_date})
    return render_to_response("checker/showCasething.html",{'form':form,'c_id':c_id},context_instance=RequestContext(request))







