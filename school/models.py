from django.db import models
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
class Classroom(models.Model):
   # Рік початку навчання (наприклад 2021)
   start_year = models.IntegerField()
   # Літера класу (А, Б, В...)
   letter = models.CharField(max_length=1)
   # класний керівник
   class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='classes')

   def __str__(self):
       return f"{self.start_year}-{self.letter}"
class Student(models.Model):
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   # Дата народження
   birth_date = models.DateField()
   # прив’язуємо клас
   classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='students')

   def __str__(self):
       return f"{self.last_name} {self.first_name}"
# Create your models here.
