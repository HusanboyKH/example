from django.urls import path
from .views import (AllCrateTodoView,RUDToDoView)


urlpatterns = [
    path('',AllCrateTodoView.as_view()),
    path('<pk>/RUD',RUDToDoView.as_view()),
    ]
