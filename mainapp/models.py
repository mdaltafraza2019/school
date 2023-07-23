from django.db import models

# Create your models here.
CITY=(
   ( "purnia","purnia"),
   ( "katihar","katihar"),
   ( "bhagalpur","bhagalpur"),
   ( "kisanganj","kisanganj"),
   ( "patna","patna"),
   ( "goa","goa"),
)
class Student(models.Model):
    name=models.CharField(max_length=200)
    contact=models.CharField(max_length=11)
    email=models.EmailField()
    city=models.CharField(max_length=100,choices=CITY)

    def __str__(self):
        return self.name
