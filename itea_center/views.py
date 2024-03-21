from django.shortcuts import render
from .models import Course, Application, Groups, Mentors, Listeners
from django.http import HttpResponse


def home_itea(request):
    return render(request, 'work_in_center.html')


def add_course(request):
    try:
        if request.method == 'POST':
            Course.objects.create(id=request.POST.get('id'), name_course=request.POST.get('name_course'),
                                  quantiity_watch=request.POST.get('quantity'),
                                  price=request.POST.get('price'))
        return render(request, 'work_with_base/add.html')
    except:
         return HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')


def read_course(request):
    course = Course.objects.all()
    return render(request, 'work_with_base/read.html', context={'course': course})


def delete(request):
    course = Course.objects.all()
    if request.method == 'POST':
        id = request.POST.get('id_delete')
        course_del = Course.objects.get(id=int(id))
        course_del.delete()
    return render(request, 'work_with_base/delete.html', context={'course': course})


def edit(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id_edit')
            course = Course.objects.get(id=int(id))
            course.name_course = request.POST.get('name_course')
            course.quantity_watch = request.POST.get('quantity')
            course.price = float(request.POST.get('price'))
            course.save()
    except:
        return HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
    course_read = Course.objects.all()
    return render(request, 'work_with_base/edit.html', context={'course': course_read})


# Менторы
def add_mentors(request):
    try:
        if request.method == 'POST':
            Mentors.objects.create(id=request.POST.get('id'), name=request.POST.get('name'),
                                   surname=request.POST.get('surname'),
                                   father_name=request.POST.get('father_name'),
                                   image=request.POST.get('image'),
                                   year_of_birth=request.POST.get('year_of_birth'),
                                   qualification=request.POST.get('qualification'),
                                   additional_information=request.POST.get('additional_information'))
        return render(request, 'work_with_mentors/add_mentor.html')
    except:
        return HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')


def delete_mentor(request):
    try:
        course = Mentors.objects.all()
        if request.method == 'POST':
            id = request.POST.get('id_delete')
            course_del = Mentors.objects.get(id=int(id))
        course_del.delete()
    except:
        HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
        return render(request, 'work_with_mentors/delete.html', context={'course': course})


def edit_mentor(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            course = Mentors.objects.get(id=int(id))
            course.name = request.POST.get('name')
            course.surname = request.POST.get('surname')
            course.father_name = request.POST.get('father_name')
            course.image = request.POST.get('image')
            course.year_of_birth = request.POST.get('year_of_birth')
            course.qualification = request.POST.get('qualification')
            course.additional_information = request.POST.get('additional_information')
            course.save()
    except:
        return HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
    course_read = Mentors.objects.all()
    return render(request, 'work_with_mentors/edit.html', context={'course': course_read})


# Слушатели
def add_listeners(request):
    try:
        if request.method == 'POST':
            Listeners.objects.create(id=request.POST.get('id'), name=request.POST.get('name'),
                                     surname=request.POST.get('surname'),
                                     father_name=request.POST.get('father_name'),
                                     year_of_birth=request.POST.get('year_of_birth'),
                                     image=request.POST.get('image'),
                                     phone=request.POST.get('phone'),
                                     сompleted_courses=request.POST.get('сompleted_courses'))
        return render(request, 'work_listeners/add.html')
    except:
        return HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')


def delete_listen(request):
    try:
        course = Listeners.objects.all()
        if request.method == 'POST':
            id = request.POST.get('id')
            course_del = Listeners.objects.get(id=int(id))
            course_del.delete()
    except:
        HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
    return render(request, 'work_listeners/delete.html', context={'course': course})


def edit_listen(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            course = Listeners.objects.get(id=int(id))
            course.name = request.POST.get('name')
            course.surname = request.POST.get('surname')
            course.father_name = request.POST.get('father_name')
            course.year_of_birth = request.POST.get('year_of_birth')
            course.image = request.POST.get('image')
            course.phone = request.POST.get('phone')
            course.сompleted_courses = request.POST.get('сompleted_courses')
            course.save()
    except:
        return HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
    course_read = Listeners.objects.all()
    return render(request, 'work_listeners/edit.html', context={'course': course_read})


# Application

def add_aplication(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            week = request.POST.get('week')
            time = request.POST.get('time')
            listen_id = request.POST.get('listeners')
            listeners = Listeners.objects.get(id=listen_id)
            course_id = request.POST.get('course')
            course = Course.objects.get(id=course_id)
            Application.objects.create(id=id,
                                       name_listeners=listeners,
                                       name_of_course=course,
                                       desired_week=week,
                                       desired_time=time)
    except:
        HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
    return render(request, 'work_app/add.html',
                      context={'course': Course.objects.all(), 'listeners': Listeners.objects.all()})


def delete_aplication(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            course_del = Application.objects.get(id=int(id))
            course_del.delete()
        return render(request, 'work_app/delete.html', context={'course': Application.objects.all()})
    except:
        HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')


def edit_aplication(request):
    try:
        if request.method == 'POST':
            week = request.POST.get('week')
            time = request.POST.get('time')
            listen_id = request.POST.get('listeners')
            listeners = Listeners.objects.get(id=listen_id)
            course_id = request.POST.get('course')
            course = Course.objects.get(id=course_id)
            id = request.POST.get('id')
            app = Application.objects.get(id=int(id))
            app.desired_week = week
            app.desired_time = time
            app.name_listeners = listeners
            app.name_of_course = course
            app.save()
    except:
        return HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
    return render(request, 'work_app/edit.html',
                  context={'course': Course.objects.all(), 'listeners': Listeners.objects.all(),
                           'app': Application.objects.all()})


def add_group(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            date = request.POST.get('date')
            text = request.POST.get('text')
            mentor_id = request.POST.get('mentor')
            mentors = Mentors.objects.get(id=mentor_id)
            course_id = request.POST.get('course')
            course = Course.objects.get(id=course_id)
            app_id = request.POST.get('app')
            app = Application.objects.get(id=app_id)
            Groups.objects.create(id=id,
                                  name_course=course,
                                  name_mentor=mentors,
                                  name_listen=app,
                                  desired_time=date,
                                  desired_date=text)
    except:
        HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
    return render(request, 'work_groups/add.html',
                  context={'course': Course.objects.all(), 'mentors': Mentors.objects.all(),
                           'app': Application.objects.all()})


def edit_group(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            date = request.POST.get('date')
            text = request.POST.get('text')
            mentor_id = request.POST.get('mentor')
            mentors = Mentors.objects.get(id=mentor_id)
            course_id = request.POST.get('course')
            course = Course.objects.get(id=course_id)
            app_id = request.POST.get('app')
            app = Application.objects.get(id=app_id)
            Groups.objects.create(id=id,
                                  name_course=course,
                                  name_mentor=mentors,
                                  name_listen=app,
                                  desired_time=date,
                                  desired_date=text)
    except:
        HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
    return render(request, 'work_groups/add.html',
                  context={'course': Course.objects.all(), 'mentors': Mentors.objects.all(),
                           'app': Application.objects.all()})


def delete_group(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            course_del = Groups.objects.get(id=int(id))
            course_del.delete()
        return render(request, 'work_groups/delete.html', context={'course': Groups.objects.all()})
    except:
        HttpResponse('Что то пошло не так или вы прописали существующий уникальный ключ')
