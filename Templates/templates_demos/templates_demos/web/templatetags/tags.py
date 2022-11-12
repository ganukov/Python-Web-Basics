from django.template import Library

from templates_demos.web.views import Student

register = Library()


@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hello, I am {student.name} and I am {student.age}--years old'


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args,
    }
    return context
