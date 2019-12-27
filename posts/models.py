from django.db import models

    # Create your MYTHICAL models

class Author(models.Model):
    authors_name = models.CharField(max_length = 16)
    authors_surname = models.CharField(max_length = 32)
    authors_age = models.IntegerField(max_length = 3)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_image = models.CharField(max_length = 150)
    post_text = models.CharField(max_length = 200)
    post_date = models.DateTimeField('Время публикации')


class Publication(models.Model):
    title = models.CharField(max_length = 30)


    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length= 100)
    publications = models.ManyToManyField(Publication)


    def __str__(self):
        return self.headline