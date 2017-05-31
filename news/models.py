from django.db import models

class Category(models.Model):
    name = models.CharField('Category name', max_length=100)
    slug = models.SlugField('Link', unique=True, max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField('Link', max_length=255, unique=True)
    text = models.TextField(verbose_name='Content')
    categories = models.ManyToManyField(Category, verbose_name='Categories')
    posted_date = models.DateTimeField('Add date', auto_now_add=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.title