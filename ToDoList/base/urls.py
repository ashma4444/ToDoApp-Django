from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    # path('delete/<int:id>', views.delete),
    path('delete/<int:id>', views.delete, name="delete"),
    path('<int:id>', views.update, name="update"),
]