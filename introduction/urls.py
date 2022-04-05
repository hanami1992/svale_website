from django.urls import path

from introduction.views import IntroductionPageView

urlpatterns = [
    path('', IntroductionPageView.as_view(), name='introduction')
]