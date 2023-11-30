from django.shortcuts import render, redirect
from . models import Profile

import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.


# def cv_maker(request):
#     if request.method == 'POST':
#         name = request.POST.get("name")


def cv_maker(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('work', '')
        skills = request.POST.get('skills', '')
        profile = Profile(name=name, email=email,
                          phone=phone,
                          summary=summary,
                          degree=degree,
                          school=school,
                          university=university,
                          previous_work=previous_work,
                          skills=skills
                          )
        profile.save()
        return redirect('list')
    return render(request, 'mycv/cv_generator.html')


def resume(request, pk):
    user_profile = Profile.objects.get(id=pk)
    template = loader.get_template('mycv/resume.html')
    html = template.render({'user_profile': user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    context = {'user_profile': user_profile}

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response

    # return render(request, 'mycv/resume.html', context)


def list(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'mycv/list.html', context)
