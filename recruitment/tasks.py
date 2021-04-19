import service.settings
from django.core.mail import send_mail
from . import models
from service.celery import app

@app.task
def sendMail(idd):

    ob=models.HandShadow.objects.select_for_update().get(id=idd)

    sith_name = ob.sith.name
    recruit_email = ob.recruit.email

    if not ob.isWelcomeMailSent:

        send_mail('Уведомление о зачислении Рукой Тени в Орден Ситхов',
            'Вы зачислены в Орден Ситхов к ситху %s' % sith_name,
            service.settings.EMAIL_HOST_USER,
            ['ana_vinogradova@mail.ru'], fail_silently=False)

        ob.isWelcomeMailSent = True
        ob.save()

@app.task
def sendPeriodicMail():

    send_mail('Уведомление о зачислении Рукой Тени в Орден Ситхов',
       'Вы получили это письмо потому, что подписаны на наш сервис',
        service.settings.EMAIL_HOST_USER,
        ['ana_vinogradova@mail.ru'], fail_silently=False)

