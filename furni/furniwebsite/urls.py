from django.urls import path

#from furniwebsite import views
from . import views

app_name="furni"
urlpatterns = [
    path('',views.index, name="index"),
    path('about',views.about, name="about"),
    path('edit/', views.edit, name="edit"),
    path('insert',views.insertData, name="insertData"),
    path('update/<id>/',views.updateData, name="updateData"),
    path('delete/<id>/',views.deleteData, name="deleteData")




]