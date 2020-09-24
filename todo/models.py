from django.db import models

class Todo(models.Model):
    """Model definition for Todo."""

    text = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Todo."""

        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.text

