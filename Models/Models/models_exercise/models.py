from django.db import models
from django.template.defaulttags import url
from django.urls import reverse
from django.utils.datetime_safe import date


class AuditInfo(models.Model):
    class Meta:
        # No table will be created in the DB
        # Can be inherited in other models
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    # This will be automatically set on each 'save/update'
    updated_on = models.DateTimeField(
        auto_now=True,
    )


# Model field == Class attributes in Model Classes
# Relation example with class Department
class Department(AuditInfo, models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(
        unique=True,
        null=True
    )

    def get_absolute_url(self):
        reverse('details department',kwargs={
            'pk':self.pk,
        })
        return url

class Project(AuditInfo, models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=10, unique=True)
    deadline = models.DateField()


class Employee(AuditInfo, models.Model):

    first_name = models.CharField(max_length=30, )  ## Creates a column type VarChar with length = 30 (MODEL_FIELD)
    last_name = models.CharField(max_length=50, )
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    # This will be automatically set on creation
    # Text with unlimited length
    review = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    # This will be automatically set on each 'save/update'
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )
    projects = models.ManyToManyField(Project, related_name='employees')

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        # self.id == self.pk
        return f'Id: {self.pk}; Name {self.fullname}'

    @property
    def year_of_employment(self):
        return date.today() - self.created_on


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, primary_key=True
    )


# Employee.objects.raw('Select *')
# Employee.objects.all() # Select *
# Employee.objects.create() # Insert
# Employee.objects.filter() # Select + Where
# Employee.objects.update() # Update

'''
Django ORM (Object - relational mapping)
'''

# class NullBlankDemo(models.Model):
#     # blank = models.IntegerField(
#     #     blank=True,
#     #     null=False,
#     # )
#     #
#     # null = models.IntegerField(
#     #     blank=False,
#     #     null=True,
#     # )
#
#     blank_null = models.IntegerField(
#         blank=True,
#         null=True,
#     )  # Form validation
#
#     default = models.IntegerField(
#         blank=False,
#         null=False,
#     )
