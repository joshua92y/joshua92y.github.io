from django.shortcuts import render
from django.db import connection
# Create your views here.
def index(request):
    return render(request, "qslmain.html")

def create_person(name, age):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO myapp_person (name, age) VALUES (%s, %s)", [name, age])

def get_all_people():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, age FROM myapp_person")
        rows = cursor.fetchall()
    return [{'id': r[0], 'name': r[1], 'age': r[2]} for r in rows]

def get_person_by_id(person_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, age FROM myapp_person WHERE id = %s", [person_id])
        row = cursor.fetchone()
    if row:
        return {'id': row[0], 'name': row[1], 'age': row[2]}
    return None

def update_person(person_id, name, age):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE myapp_person SET name = %s, age = %s WHERE id = %s", [name, age, person_id])
        return cursor.rowcount
    
def delete_person(person_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM myapp_person WHERE id = %s", [person_id])
        return cursor.rowcount