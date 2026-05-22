from django.db import models

# Создайте модель тегов (Tag):
# Имя тэга (Строковое поле, уникальное)

class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name