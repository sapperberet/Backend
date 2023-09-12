from django.urls import path
from views import ItemList , LocationList, ItemDetail , LocationDetail
urlpatterns =[
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),


]