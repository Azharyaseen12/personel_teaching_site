from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title




class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Docs(models.Model):
    title = models.CharField(max_length=200)
    docs_file = models.FileField(upload_to='docs/')

    def __str__(self):
        return self.title
