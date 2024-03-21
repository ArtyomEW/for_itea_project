from django.contrib import admin
from django.urls import path
from itea import views as vs
from itea_center import views as vs2

urlpatterns = [
    path('', vs2.home_itea, name='home_itea'),
    path('admin/', admin.site.urls),
    path('sign_in/', vs.loginpage, name='loginpage'),
    path('register/', vs.registerPage, name='register'),
    path('add_course/', vs2.add_course, name='add_course'),
    path('delete_course/', vs2.delete, name='delete_course'),
    path('edit_course/', vs2.edit, name='edit_course'),
    # Менторы
    path('add_mentors/', vs2.add_mentors, name='add_mentors'),
    path('delete_mentors/', vs2.delete_mentor, name='delete_mentors'),
    path('edit_mentors/', vs2.edit_mentor, name='edit_mentors'),
    # Слушатели
    path('add_listen/', vs2.add_listeners, name='add_listen'),
    path('delete_listen/', vs2.delete_listen, name='delete_listen'),
    path('edit_listen/', vs2.edit_listen, name='edit_listen'),
    # Заявки
    path('add_app/', vs2.add_aplication, name='add_app'),
    path('delete_app/', vs2.delete_aplication, name='delete_app'),
    path('edit_app/', vs2.edit_aplication, name='edit_app'),
    # Группы
    path('add_group/', vs2.add_group, name='add_group'),
    path('delete_group/', vs2.delete_group, name='delete_group'),
    path('edit_group/', vs2.edit_group, name='edit_group'),
    path('center/', vs.center, name='center'),
]
