from django.urls import path
from backend.user.views.v1_views import *

urlpatterns = [
    path('sign_in', SignIn.as_view()),
]
