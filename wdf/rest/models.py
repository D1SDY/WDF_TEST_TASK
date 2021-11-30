from django.db import models

# Create your models here.
class Logs(models.Model):
    text = models.CharField(max_length=200)
    user_id = models.IntegerField()

    def __str__(self):
        return "Log with text:\n " + self.text + "was created by user with id: \n" + str(self.user_id)