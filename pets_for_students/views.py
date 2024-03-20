from django.shortcuts import render
from pets_for_students.models import Student, Cat

# Create your views here.
def index(request):
    student_list = Student.objects.order_by('lastName')
    cat_list = Cat.objects.order_by('name')

    context_dict = {"student_list" : student_list, "cat_list" : cat_list}

    return render(request, "pets_for_students/index.html", context = context_dict)

def pets(request):
    cat_list = Cat.objects.order_by('name')

    context_dict = {"cat_list" : cat_list}

    return render(request, "pets_for_students/pets.html", context = context_dict)