from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView


class IntroductionPageView(TemplateView):
    template_name = 'introduction.html'

