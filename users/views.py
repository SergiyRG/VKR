from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.forms import profileUpdateForm, userUpdateForm
from users.models import Profile as Pro
from users.models import  Teacher
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage

@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Ваша учетная запись была успешно обновлена!')
            return redirect('users:profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context= {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'profile/profile.html',context)


def teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('e-mail')
        num_tel = request.POST.get('phone')
        prof = request.user.profile
        teacher = Teacher(profil=prof, name=name, email=email, num_tel=num_tel)
        teacher.save()
        prof_id = prof.id
        Pro.objects.filter(id=prof_id).update(is_teacher=False)
        
        message = 'Здравствуйте! Ваш запрос на учетную запись преподавателя на рассмотрении!  Ждите ответ от Администратора платформы! После одобрения учётной записи Преподавателя, Вы сможете вернуться и загружать курсы, лекции, практику и много чего ещё!'
        send_mail(
            'Запрос на рассмотрении.',
            message,
            'online-learning@no-reply.com',
            [email],
            fail_silently=False,
        )
        send_mail(
            'Online Learning',
            'Кто-то запросил учетную запись учителя. С информацией: ' + name + ' , ' + email + ' , ' + num_tel + ' , ' + str(prof) + '.',
            'online-learning@no-reply.com',
            ['serejenbkasteam@gmail.com'],
            fail_silently=False,
        )
        messages.info(request, f'Запрос был успещно отправлен, вы получите уведомление по электронной почте.')
        return redirect('courses:home')