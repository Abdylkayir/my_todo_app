from django.db import models

# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано'),
    ]

    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.description
