from django import forms
import datetime
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import RadioSelect
from django.forms.extras.widgets import SelectDateWidget


MOD_CHOICES = (('0','not repeat'),('1','repeat every day'),('2','repeat every weak'),('3','repeat every month'),('4','repeat every year'))

class AddRoutineForm(forms.Form):
    title = forms.CharField(label=_(u"routine"),max_length=30,widget=forms.TextInput(attrs={'size':'30'}))
    details = forms.CharField(label=_(u"details"),max_length=666,widget=forms.Textarea,required=False)
    mode = forms.ChoiceField(widget=RadioSelect, choices=MOD_CHOICES)
    start_date = forms.DateField(widget=SelectDateWidget(),initial=datetime.date.today)
    end_date = forms.DateField(widget=SelectDateWidget(),initial=datetime.date.today)
    
    def clean_end_date(self):
        ## below
        '''make sure to_date>from_date'''
        sd = self.cleaned_data["start_date"]
        ed = self.cleaned_data["end_date"]
        return ed

class CasethingForm(forms.Form):
    title = forms.CharField(label=_(u'title'),max_length=30,widget=forms.TextInput(attrs={'size':'30'}),initial='this is initial values',help_text='An abstract, please.',error_messages={'required':'initial value is useless','max_length':'too much words, put some in the detail section'})
    details = forms.CharField(label=_(u"details"),max_length=666,widget=forms.Textarea,required=False)
    case=forms.CharField(label=_(u'case'),max_length=30,widget=forms.TextInput(attrs={'size':'30'}))
    # validation not approvedddd
    setup_date = forms.DateField(initial=datetime.date.today,required=False)
    
    
