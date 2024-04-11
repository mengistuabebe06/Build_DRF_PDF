from django.db import models


class ExtractedData(models.Model):
    email = models.EmailField(unique=True)
    nouns = models.TextField()
    verbs = models.TextField()

    def __str__(self):
        return self.email
