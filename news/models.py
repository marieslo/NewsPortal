import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


#1. Модель Author:
#Модель, содержащая объекты всех авторов.
#Имеет следующие поля:
    # - cвязь «один к одному» с встроенной моделью пользователей User;
    # - рейтинг пользователя

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.auth_rating = 0
        for post in Post.objects.filter(author__user=self.user):
            self.auth_rating += comment.comment_rating
        for comment in Comment.objects.filter(user=self.user):
            self.auth_rating += comment.comment_rating
        self.save()

    def __str__(self):
        return f'{self.user.username}'


#2. Модель Category:
# Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.). Имеет единственное поле: название категории. Поле должно быть уникальным (в определении поля необходимо написать параметр unique = True).
class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)



# 3.	Модель Post
# Эта модель должна содержать в себе статьи и новости, которые создают пользователи. Каждый объект может иметь одну или несколько категорий.
# Соответственно, модель должна включать следующие поля:
# 	связь «один ко многим» с моделью Author;
# 	поле с выбором — «статья» или «новость»;
# 	автоматически добавляемая дата и время создания;
# 	связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
# 	заголовок статьи/новости;
# 	текст статьи/новости;
# 	рейтинг статьи/новости.
#	Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу.
# 2.	Метод preview() модели Post, который возвращает начало статьи (предварительный просмотр) длиной 124 символа и добавляет многоточие в конце.
class Post(models.Model):
    article = 'AR'
    news = 'NE'

    TYPE = [
        (article, 'статья'),
        (news, 'новость')]

    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_post = models.CharField(max_length=2, choices=TYPE, default=article)
    date_time_post = models.DateTimeField(auto_now_add=True)
    categories_post = models.ManyToManyField(Category, through='PostCategory')
    title_post = models.CharField(max_length=250)
    text_post = models.TextField()
    rating_post = models.FloatField(default=0.0)

    def like(self, amount=1):
        self.articles_rating += amount
        self.save()

    def dislike(self):
        self.like(-1)


#test = Post.objects.create(нужные аргументы)
#test.like()

# 4.	Модель PostCategory
class PostCategory(models.Model):
    cat_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_cat = models.ForeignKey(Category, on_delete=models.CASCADE)

# 5.	Модель Comment
# Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
# Модель будет иметь следующие поля:
# 	связь «один ко многим» с моделью Post;
# 	связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
# 	текст комментария;
# 	дата и время создания комментария;
# 	рейтинг комментария.
# 1.	Методы like() и dislike() в моделях Comment и Post, которые увеличивают/уменьшают рейтинг на единицу.

class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete = models.CASCADE)
    commentator_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length = 200)
    date_time_comment = models.DateTimeField(auto_now_add=True)

    def like(self, amount=1):
        self.articles_rating += amount
        self.save()

    def dislike(self):
        self.like(-1)
#В качестве результата задания подготовьте файл, в котором напишете список всех команд, запускаемых в Django shell.
# Что вы должны сделать в консоли Django?
#1.	Создать двух пользователей (с помощью метода User.objects.create_user('username')).
#2.	Создать два объекта модели Author, связанные с пользователями.
#3.	Добавить 4 категории в модель Category.
#4.	Добавить 2 статьи и 1 новость.
#5.	Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
#6.	Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
#7.	Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
#8.	Обновить рейтинги пользователей.
#9.	Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
#10.	Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
#11.	Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

