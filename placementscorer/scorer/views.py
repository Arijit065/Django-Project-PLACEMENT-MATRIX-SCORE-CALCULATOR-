from django.shortcuts import render, redirect
from .models import Student

def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        roll_no = request.POST["roll_no"]
        score = int(request.POST["score"])
        placed = True if score >= 60 else False  # Example rule
        Student.objects.create(name=name, roll_no=roll_no, score=score, placed=placed)
        return redirect("home")

    students = Student.objects.all()
    return render(request, "home.html", {"students": students})
