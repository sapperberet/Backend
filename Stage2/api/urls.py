from django.urls import path
from .views import list_person,C_person,R_person,U_person,D_person
urlpatterns =[

    path('', list_person.as_view()),
    path('create/', C_person.as_view()),
    path('<int:id>/', R_person.as_view()),
    path('update/<int:id>/', U_person.as_view()),
    path('delete/<int:id>/', D_person.as_view())

]