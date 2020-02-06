from django.db import models

class library(models.Model):

    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("library")
        verbose_name_plural = _("libraries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("library_detail", kwargs={"pk": self.pk})
