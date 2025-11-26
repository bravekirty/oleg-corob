import django.db.models
import django.utils.timezone

import articles.models


class Attachment(django.db.models.Model):
    article = django.db.models.ForeignKey(
        articles.models.Article,
        on_delete=django.db.models.CASCADE,
        related_name='attachments'
    )
    file = django.db.models.FileField(
        upload_to='attachments/%Y/%m/%d/',
        verbose_name="File"
    )
    name = django.db.models.CharField(
        max_length=100,
        blank=True,
    )
    order = django.db.models.IntegerField()

    def __str__(self):
        return self.name if self.name else f"Attachment {self.id}"

    def save(self, *args, **kwargs):
        if not self.name and self.file:
            self.name = self.file.name
        super().save(*args, **kwargs)