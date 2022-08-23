from random import choices
from django.db import models
# framework model demektir. gömlek modeldir. yakası nasıl olsun, rengi nasıl olsun, bedeni nasıl olsun bize gösterir. OOP kalıp demektir.

class Student(models.Model):
    COUNTRIES = [             # choices için 
        ('TR', 'Turkey'),
        ('US', 'America'),
        ('DE', 'Germany'),
        ('FR', 'France'),
    ]
    first_name = models.CharField('Adı', max_length=50)
    last_name = models.CharField('Soyadı', max_length=50)
    number = models.IntegerField('Numara')
# makemigrations komutu ile migrations folder içinde 0001_initial.py dosyası oluşur, her sefereinde artarak devam eder.
    about = models.TextField("Hakkında", blank=True, null=True)
    country = models.CharField('Ülke', max_length=2, choices=COUNTRIES, default='TR')
    avatar = models.ImageField("Resim", blank=True, null=True, upload_to='media/')
    registered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"
    

    class Meta:    # class meta özellikleriyle sort, reverse sort, rename vs yapılabilir
        ordering = ['-number']
        verbose_name_plural = 'Öğrenciler'









