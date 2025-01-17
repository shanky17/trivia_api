from django.urls import include, path
from rest_framework import routers
from trivia import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
