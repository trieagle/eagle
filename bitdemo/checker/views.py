from django.template import Context, loader, RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from checker.models import Routine,Status,Case,Casething
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from bitdemo.checker.myforms import AddRoutineForm,CasethingForm
from bitdemo.checker.views_routine import get_lists
import datetime

def main(request):
    template_var={"w":_(u"Hello: tourist!")}
    if request.user.is_authenticated():
        u_name = request.user.username
        template_var["w"]=_(u"Hello: %s!")%u_name
        routine_var = get_lists(request)
        ##do not know merge func
        for k,v in routine_var.items():
            template_var[k]=v
##        template_var["casething_list"] = Casething.objects.all()
        template_var["case_list"] = Case.objects.all()
        return render_to_response('checker/main.html', template_var, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse("login"))













