from django.db import models




class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True,verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):  # метод выводить title записи
        return self.title

    class Meta:
        verbose_name = 'Новость'#наименования модели в единтственном числе
        verbose_name_plural = "Новости"#наименования модели в множественном числе
        ordering = ['-created_at']#сортировка

class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование категорий') #db_index индексирует поле

    def __str__(self):  # метод выводить title записи
        return self.title

    class Meta:
        verbose_name = 'Категория'#наименования модели в единтственном числе
        verbose_name_plural = "Категории"#наименования модели в множественном числе
        ordering = ['title']#сортировка

