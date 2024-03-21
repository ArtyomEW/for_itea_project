from django.db import models


# Create your models here.
class Course(models.Model):
    name_course = models.CharField(max_length=20)
    quantiity_watch = models.IntegerField(null=True)
    price = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'Наименование курса: {self.name_course} Количество часов: {self.quantiity_watch} Цена курса: {self.price}'


class Mentors(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20, null=True)
    image = models.FileField(null=True)
    year_of_birth = models.DateField(null=True)
    qualification = models.CharField(max_length=30)
    additional_information = models.TextField(null=True)

    class Meta:
        verbose_name = 'Менторы'
        verbose_name_plural = 'Менторы'

    def __str__(self):
        return f'Данные о менторе {self.name} ,{self.surname}, {self.father_name}, Фото: {self.image} ' \
               f'Год_рожд: {self.year_of_birth} Квалификация: {self.qualification} Доп_инфор:{self.additional_information}'


class Listeners(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20, null=True)
    year_of_birth = models.DateField(null=True)
    image = models.ImageField(null=True)
    phone = models.CharField(max_length=12,null=True)
    сompleted_courses = models.TextField(null=True)

    class Meta:
        verbose_name = 'Слушатели'
        verbose_name_plural = 'Слушатели'

    def __str__(self):
        return f'Имя:{self.name} Фамилия:{self.surname} Отчество: {self.father_name} Фото: {self.image} ' \
               f'Год_рожд: {self.year_of_birth} Номер телефона: {self.phone} Пройденные курсы:{self.сompleted_courses}'


class Application(models.Model):
    name_listeners = models.ForeignKey(Listeners, on_delete=models.CASCADE,null=True)
    name_of_course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    desired_week = models.CharField(max_length=100, null=True)
    desired_time = models.TimeField(null=True)

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f' {self.name_listeners}  {self.name_of_course} Желаемое время обучение: ' \
               f'{self.desired_time} Желаемые дни недели: {self.desired_week}'


class Groups(models.Model):
    name_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name_mentor = models.ForeignKey(Mentors, on_delete=models.CASCADE)
    name_listen = models.ForeignKey(Application, on_delete=models.CASCADE)
    desired_time = models.DateField(null=True)
    desired_date = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'{self.name_course}  {self.name_mentor}  ' \
               f'{self.name_listen} {self.desired_date} {self.desired_time}'
