from django.db import models

class book(models.Model):

    title = models.CharField(max_length=50)
    isbn_Number = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
