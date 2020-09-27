from django.urls import path
from .views import Register, Login, Me

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('me/', Me.as_view())
]
