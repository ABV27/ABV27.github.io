
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    path('категории', views.категории, name='категории'),
    path('открыть_категорию<int:категория_id>', views.открыть_категорию, name='открыть_категорию'),
    path('открыть<int:объявление_id>', views.открыть, name='открыть'),
    path('новое_объявление', views.новое_объявление, name='новое_объявление'),
    
    path("удалить<int:rubric_id>",views.удалить,name="удалить"),
    path("кабинет",views.кабинет,name="кабинет"),
    
    path("поиск",views.поиск,name="поиск"),
    
    path("нет",views.нет,name="нет"),  
]
