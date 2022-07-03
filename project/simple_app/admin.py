from django.contrib import admin
from .models import Category, Product

# Регистрируем модели в админке сайта, чтобы там появились представления и формы для работы с ними.
admin.site.register(Category)
admin.site.register(Product)
