from .forms import TestForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from .models import Sith, Recruit, Question, Answer, HandShadow
from django.core.mail import send_mail
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import service.settings

# Create your views here.

def index(request):

    sith_ids=Sith.objects.values('id')

    sith_list1=[]
    for id_ in sith_ids:
        sith=Sith.objects.get(id=id_['id'])
        numHands=HandShadow.objects.filter(sith_id=id_['id']).count()
        sith_list1.append((sith, numHands))

    sith_list2=[]
    for i in sith_list1:
        if i[1] > 1:
            sith_list2.append((i[0], i[1]))

    context={'sith_list1': sith_list1, 'sith_list2': sith_list2}
    return render(request,'index.html',context=context)

def sendMail(idd):

    ob=HandShadow.objects.get(id=idd)

    sith_name = ob.sith.name
    recruit_email = ob.recruit.email

    send_mail('Уведомление о зачислении Рукой Тени в Орден Ситхов',
        'Вы зачислены в Орден Ситхов к ситху %s' % sith_name,
        service.settings.EMAIL_HOST,
        [recruit_email], fail_silently=False)

def hands(request, pk):

    numHands=HandShadow.objects.filter(sith_id=request.session['sith_identificator']).count()
    if numHands >= 3:
        return HttpResponseRedirect(reverse_lazy('sith-notice', args=[pk]))

    h=HandShadow.objects.create(
        recruit=Recruit.objects.get(id=pk),
        sith=Sith.objects.get(id=request.session['sith_identificator']))
    h.save()
    sendMail(h.id)
    context={}
    return render(request,'enrolment_complete.html',context=context)

class RecruitCreate(CreateView):

    model = Recruit
    fields = ['name', 'planet', 'age', 'email']
    template_name = 'recruit_form.html'

    def form_valid(self, form):
        recruit=form.save()
        recruit.save()
        return HttpResponseRedirect(reverse_lazy('test-create', args=[recruit.id]))

class TestCreate(FormView):
    form_class = TestForm
    success_url = '/recruitment/test/result'
    template_name = 'test_form.html'

    def form_valid(self, form):
        return super(TestCreate, self).form_valid(form)

    def post(self, request, pk):

        for questionPk in range(1, Question.objects.count() + 1):
            a=Answer.objects.create(
                uid=111,
                recruit=Recruit.objects.get(id=pk),
                question=Question.objects.get(id=questionPk),
                answer=self.request.POST['q_%s' % questionPk])
            a.save()
        return super(TestCreate, self).post(request)

class SithListView(ListView):
    model = Sith
    context_object_name = 'sith_list'
    queryset = Sith.objects.all()
    template_name = 'sith_list.html'

class SithDetailView(DetailView):
    model = Sith
    context_object_name = 'sith'
    queryset = Sith.objects.all()
    template_name = 'sith_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SithDetailView, self).get_context_data(**kwargs)
        recruits=HandShadow.objects.values('recruit')
        result=Recruit.objects.exclude(id__in=recruits)
        context['recruit_list'] = result
        self.request.session['sith_identificator']=self.kwargs['pk']
        return context

class RecruitListView(ListView):
    model = Recruit
    context_object_name = 'recruit_list'
    queryset = Recruit.objects.all()
    template_name = 'recruit_list.html'

class RecruitDetailView(DetailView):
    model = Recruit
    context_object_name = 'recruit'
    queryset = Recruit.objects.all()
    template_name = 'recruit_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RecruitDetailView, self).get_context_data(**kwargs)
        answers=Answer.objects.filter(recruit_id=self.kwargs['pk'])
        context['answer_list'] = answers
        return context


