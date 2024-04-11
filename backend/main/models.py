from django.db import models


class ExtractedData(models.Model):
    pdf_file = models.FileField(upload_to="pdf_files/")
    email = models.EmailField(unique=True)
    nouns = models.TextField()
    verbs = models.TextField()

    def __str__(self):
        return self.email
