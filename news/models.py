from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    post = models.TextField()
    date = models.DateTimeField()
    tags = models.CharField(max_length=255)
    views = models.IntegerField(null=True, default=0)

    def get_date(self):
        return f"hi"

    def __str__(self) -> str:
        return f"news {self.id}"
        