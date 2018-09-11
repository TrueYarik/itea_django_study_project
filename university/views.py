from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import StudentForm, TeacherForm, ClassForm
from .models import Student, Teacher, Class
from django.views import View
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


class IndexView(View):
    template_name = 'university/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def first_html_page(request):
    return render(request, 'university/my_first_template_page.html', )


class AddStudent(View):
    form_class = StudentForm
    template_name = 'university/add_student.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']

            # LOGGING
            logger.debug(
                "Student's form submitted: {first_name} {last_name} |"
                " {phone_number}, {email} |"
                .format(
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    email=email,
                ))

            # Committing new Student into database
            student_send = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
            )
            messages.add_message(request, messages.INFO,
                                 'Student {name} {lastname} has been added'.format(
                                     name=form.cleaned_data['first_name'], lastname=form.cleaned_data['last_name']))
            student_send.save()

            return render(request, self.template_name, {"form": self.form_class})

        # Logging mistake in Student's form submit
        logger.warning(
            "MISTAKES in Student's form: {first_name} {last_name} |"
            " {phone_number}, {email} |"
            .format(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                phone_number=request.POST['phone_number'],
                email=request.POST['email'],
            ))
        return render(request, self.template_name, context={"form": form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})


class AddTeacher(View):
    form_class = TeacherForm
    template_name = 'university/add_teacher.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']

            logger.debug(
                "Teacher's form submitted: {first_name} {last_name} |"
                " {phone_number}, {email} |"
                " {subject} |"
                .format(
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    email=email,
                    subject=subject
                ))

            teacher_send = Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                subject=subject
            )
            messages.add_message(request, messages.INFO,
                                 'Teacher {name} {lastname} has been added'.format(
                                     name=form.cleaned_data['first_name'], lastname=form.cleaned_data['last_name']))
            teacher_send.save()

            return render(request, self.template_name, {"form": self.form_class})
        logger.warning(
            "MISTAKES in Teacher's form: {first_name} {last_name} |"
            " {phone_number}, {email} |"
            " {subject} |"
            .format(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                phone_number=request.POST['phone_number'],
                email=request.POST['email'],
                subject=request.POST['subject']
            ))
        return render(request, self.template_name, context={"form": form})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})


def add_class(request):
    form = ClassForm()
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.phone_valid()
            return render(request, 'university/add_student.html', context={"form": ClassForm, "success": True})

    return render(request, 'university/add_student.html', context={"form": form})