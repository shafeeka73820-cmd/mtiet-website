from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'students/index.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = self.object_list.count()
        context['dept_count'] = Student.objects.values('branch').distinct().count()
        context['title'] = 'Student Portal'
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'
    slug_field = 'roll'
    slug_url_kwarg = 'roll'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Student'
        return context

    def get_success_url(self):
        return reverse_lazy('students:detail', kwargs={'roll': self.object.roll})


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    slug_field = 'roll'
    slug_url_kwarg = 'roll'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Student'
        return context

    def get_success_url(self):
        return reverse_lazy('students:detail', kwargs={'roll': self.object.roll})


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    slug_field = 'roll'
    slug_url_kwarg = 'roll'
    success_url = reverse_lazy('students:index')
