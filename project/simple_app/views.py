# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .filters import ProductFilter
from .forms import ProductForm


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'simple_app/products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
    paginate_by = 2  # количество записей на странице

    def get_queryset(self):
        """ Переопределяем функцию получения списка товаров. """
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации. Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ProductFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs) -> dict:
        """ Метод get_context_data позволяет нам изменить набор данных,
            который будет передан в шаблон.
            С помощью super() мы обращаемся к родительским классам
            и вызываем у них метод get_context_data с теми же аргументами,
            что и были переданы нам. """
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Следующая распродажа в четверг!"
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    """ Получить информацию по отдельному товару. """
    model = Product
    template_name = 'simple_app/product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'


class ProductCreate(CreateView):
    """ Представление для создания товаров. """
    form_class = ProductForm
    model = Product
    template_name = 'simple_app/product_edit.html'


class ProductUpdate(UpdateView):
    """ Представление для редактирования товаров. """
    form_class = ProductForm
    model = Product
    template_name = 'simple_app/product_edit.html'


class ProductDelete(DeleteView):
    """ Представление для удаления товаров. """
    model = Product
    template_name = 'simple_app/product_delete.html'
    success_url = reverse_lazy('product_list')
