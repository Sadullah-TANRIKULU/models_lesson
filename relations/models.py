from django.db import models

class Creator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name']


class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)
    # on_delete : creator tablosundaki yazarı silersem ona ait olan language yi de sil demektir.


    def __str__(self):
        return f"{self.name} - {self.creator}"
    