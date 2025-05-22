from django.db import models

genders = [('Жен', 'Жен'), ('Муж', 'Муж')]
poison = [('Не яд', 'Не яд'), ('Яд', 'Яд')]


class Snake(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    species = models.CharField(max_length=30, verbose_name='Вид')
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/', verbose_name='Фото')
    birthdate = models.DateTimeField(verbose_name='Возраст')
    poison = models.CharField(choices=poison, verbose_name='Ядовитость')
    gender = models.CharField(choices=genders, verbose_name='Пол')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

