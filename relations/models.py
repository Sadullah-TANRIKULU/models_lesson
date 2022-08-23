from django.db import models

class Creator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name']


# one2one relation
class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Creator, on_delete=models.CASCADE)
    # on_delete : creator tablosundaki yazarı silersem ona ait olan language yi de sil demektir.


    def __str__(self):
        return f"{self.name} - {self.creator}"


    class Meta:
        ordering = ['name']


'''
on_delete properties:

# CASCADE -> if primary deleted, delete forein too.
# SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
# SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value")
# DO NOTHING -> if primary deleted, do nothing.
# PROTECT -> if foreign is exist, can not delete primary.

'''

# many2one relation : piyasada default en çok kullanılan
class Framework(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.language}"


    class Meta:
        ordering = ['name']


# many2many relation
class Developer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    framework = models.ManyToManyField(Framework) # not use on delete!!!


    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


    class Meta:
        ordering = ['first_name']
    
    
    