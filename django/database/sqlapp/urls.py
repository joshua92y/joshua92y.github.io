# sqlapp/urls.py
from django.urls import path
from . import views
from django.http import JsonResponse
urlpatterns = [
    path("", views.index, name="index"),
    path('create/', lambda request: (views.create_person("adam", 20), JsonResponse({'status': 'created'}))[1]),
    path('list/', lambda request: JsonResponse(views.get_all_people(), safe=False)),
    path('person/<int:person_id>/', lambda request, person_id: JsonResponse(views.get_person_by_id(person_id), safe=False)),
    path('update/<int:person_id>/', lambda request, person_id: (views.update_person(person_id, "John", 25), JsonResponse({'status': 'updated'}))[1]),
    path('delete/<int:person_id>/', lambda request, person_id: (views.delete_person(person_id), JsonResponse({'status': 'deleted'}))[1]),
]
