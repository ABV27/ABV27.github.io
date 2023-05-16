from django.shortcuts import render
from .models import Категория,Объявление
from django.contrib.auth.decorators import login_required #Сначала импортируется функция login_required
# Чтобы перенаправление работало, необходимо внести изменения settings.py (# Мои настройки LOGIN_URL = '/users/login/')
from django.http import Http404
# Create your views here.
цвет = ["#FFD700","#0000FF","#32CD32"]

def index(request):
    категории = Категория.objects.all()
    объявлении = Объявление.objects.all()
    context = {"категории":категории,"объявлении":объявлении,"цвет":цвет}
    return render(request, 'learning_logs/index.html',context)

def категории(request):
    категории = Категория.objects.all()
    context = {"категории":категории,"цвет":цвет}
    return render(request, 'learning_logs/категории.html',context)

def открыть_категорию(request,категория_id):
    bbs = Объявление.objects.filter(категория=категория_id)
    объявлении = Объявление.objects.all()
    категории = Категория.objects.all()
    context = {"bbs":bbs,"категории":категории,"объявлении":объявлении,"цвет":цвет}
    return render(request, 'learning_logs/открыть_категорию.html',context)

def открыть(request,объявление_id):
    bbs = Объявление.objects.get(id=объявление_id)
    ййй = bbs.число
    if ййй == None:
        ййй = 0
    ййй += 1
    bbs.число = ййй
    bbs.save()
    context = {"bbs":bbs,}
    return render(request, 'learning_logs/открыть.html',context)


from django.http import HttpResponseRedirect#класс HttpResponseRedirect, который будет использоваться для перенаправления пользователя к странице topics
from django.urls import reverse#Функция reverse() определяет URL по заданной схеме URL
from .forms import ОбъявлениеForm#импортируется только что написанная форма TopicForm
@login_required
def новое_объявление(request):#запрос
    qqq = Объявление.objects.filter(wner=request.user)
    число = len(qqq)
    if число >= 3:
        return HttpResponseRedirect(reverse('learning_logs:кабинет'))
    """Определяет новую тему."""
    if request.method != 'POST':#GET для чтения с сервера.POST для заполнения и отправки через форму
        # Данные не отправлялись; создается пустая форма.
        form = ОбъявлениеForm()#Если метод запроса отличен от POST вернуть пустую форму
    else:
        # Отправлены данные POST; обработать данные.
        form = ОбъявлениеForm(request.POST, request.FILES)# передаем ему данные, введенные пользователем, хранящиеся в request.POST
        if form.is_valid():
            new_topic = form.save(commit=False)#Чтоб небыла нуль
            new_topic.wner = request.user#Важно ---- wner
            if new_topic.цена == None:
                new_topic.цена = 0
            new_topic.save()                      
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:index'))#После того как данные будут сохранены, страницу можно покинуть (см.книгу)
    context = {'form': form}
    return render(request, 'learning_logs/новое_объявление.html', context)

@login_required
def кабинет(request):
    bbs = Объявление.objects.filter(wner=request.user)
    число = len(bbs)
    context ={"bbs": bbs,"число":число}
    return render(request, "learning_logs/кабинет.html ", context)

@login_required
def удалить(request, rubric_id):
    удалить = Объявление.objects.get(pk=rubric_id)
    удалить.delete()
    return HttpResponseRedirect(reverse('learning_logs:кабинет'))


def поиск (request):
    категории = Категория.objects.all()
    объявлении = Объявление.objects.all()
    person = request.POST.get("имя")
    bbs = Объявление.objects.filter(товар=person)
    if len(bbs)!= 0:      
        context = {"person": person,"bbs": bbs,"категории":категории,"объявлении":объявлении,"цвет":цвет}
        return render(request, "learning_logs/поиск.html ", context) 
    else:
        return HttpResponseRedirect(reverse('learning_logs:нет'))
        
def нет (request):
    return render(request, "learning_logs/нет.html ")








