from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice", "course": "Computer Science"},
    {"id": 2, "name": "Bob", "course": "Data Science"}
]

def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


@app.get('/')
def home():
    return render_template("home.html")

@app.get("/students")
def student_list():
    return render_template("students.html", students=students)


@app.get("/students/new")
def new_student_form():
    return render_template("new_student.html")


@app.post("/students")
def create_student():
    name = request.form.get("name")
    course = request.form.get("course")

    if not name or not course:
        return "Name and course are required", 400

    new_id = max(student["id"] for student in students) + 1 if students else 1

    new_student = {
        "id": new_id,
        "name": name,
        "course": course
    }

    students.append(new_student)

    return redirect(url_for("student_list"))


@app.get("/students/edit/<int:student_id>")
def edit_student_form(student_id):
    student = find_student(student_id)

    if student is None:
        return "Student not found", 404

    return render_template("edit_student.html", student=student)


@app.post("/students/edit/<int:student_id>")
def update_student(student_id):
    student = find_student(student_id)

    if student is None:
        return "Student not found", 404

    name = request.form.get("name")
    course = request.form.get("course")

    if not name or not course:
        return "Name and course are required", 400

    student["name"] = name
    student["course"] = course

    return redirect(url_for("student_list"))


@app.post("/students/delete/<int:student_id>")
def delete_student(student_id):
    student = find_student(student_id)

    if student is None:
        return "Student not found", 404

    students.remove(student)

    return redirect(url_for("student_list"))


if __name__ == "__main__":
    app.run(debug=True)