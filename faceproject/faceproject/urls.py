from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.face_detection, name='face_detection'),
    path('another-page/', views.another_page, name='another_page'),
]
