# views.py

from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def home(request):
    # HTML-вёрстка для страницы "главная"
    html = """
    <h1>Добро пожаловать на мой Django-сайт!</h1>
    <p>Это мой первый Django-сайт. Я рад приветствовать вас здесь!</p>
    """
    # Логирование посещения страницы
    logger.info('Посещена страница "главная"')
    return HttpResponse(html)


def about(request):
    # HTML-вёрстка для страницы "о себе"
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Меня зовут [ваше имя]. Я создал этот сайт с помощью Django.</p>
    """
    # Логирование посещения страницы
    logger.info('Посещена страница "о себе"')
    return HttpResponse(html)
