from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # timezone.now si default value jo si funksion qe egzekutohet
    date_posted = models.DateTimeField(default=timezone.now)
    # authori do jete i njejte me userin prandaj kemi perdor foreignkey
    # qe mundson relacion mes dy tabelave,on_delete=models.Cascade fshin postin nese useri fshihet
    author = models.ForeignKey(User, on_delete=models.CASCADE)


# manipulon shfaqjen e te dhenave jane edhe dy funksione tjera siq __repr__
# __init__ dmth e kontrollojm menyren si mi shfaq kto te dhena

    def __str__(self):
        return self.title
