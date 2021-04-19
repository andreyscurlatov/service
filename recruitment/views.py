from .forms import TestForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from .models import Sith, Recruit, Question, Answer, HandShadow
from django.urls import reverse_lazy

# Create your views here.

def index(request):

    sith_ids=Sith.objects.values('id')

    sith_list1=[]
    for id_ in sith_ids:
        sith=Sith.objects.get(id=id_['id'])
        numHands=sith.handshadow_set.all().count()
        sith_list1.append((sith, numHands))

    sith_list2=[]
    for i in sith_list1:
        if i[1] > 1:
            sith_list2.append((i[0], i[1]))

    context={'sith_list1': sith_list1, 'sith_list2': sith_list2}
    return render(request,'index.html',context=context)

def hands(request, pk_sith, pk_recruit):

    numHands=HandShadow.objects.filter(sith_id=pk_sith).count()
    if numHands >= 13:
        return redirect(reverse_lazy('sith-notice', args=[pk_sith]))

    h=HandShadow.objects.create(
        recruit=Recruit.objects.get(id=pk_recruit),
        sith=Sith.objects.get(id=pk_sith))
    h.save()
    return render(request,'enrolment_complete.html',context={})

class RecruitCreate(CreateView):

    model = Recruit
    fields = '__all__'
    template_name = 'recruit_form.html'

    def form_valid(self, form):
        recruit=form.save()
        recruit.save()
        return redirect(reverse_lazy('test-create', args=[recruit.id]))

class TestCreate(FormView):

    form_class = TestForm
    success_url = reverse_lazy('test-result')
    template_name = 'test_form.html'

    def form_valid(self, form):

        for questionPk in range(1, Question.objects.count() + 1):
            a=Answer.objects.create(
                recruit=Recruit.objects.get(id=self.kwargs['pk_recruit']),
                question=Question.objects.get(id=questionPk),
                answer=form.cleaned_data['q_%s' % questionPk])
            a.save()
        return redirect(reverse_lazy('test-result'))

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
        return context

class RecruitListView(ListView):
    model = Recruit
    context_object_name = 'recruit_list'
    queryset = Recruit.objects.all()
    template_name = 'recruit_list.html'

class RecruitDetailView(DetailView):
    model = Recruit
    context_object_name = 'recruit'
    template_name = 'recruit_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RecruitDetailView, self).get_context_data(**kwargs)
        answers=Answer.objects.filter(recruit_id=self.kwargs['pk'])
        context['answer_list'] = answers
        return context

