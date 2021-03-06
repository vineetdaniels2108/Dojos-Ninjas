from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    desc = models.TextField(max_length=240, default="Old Dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f" name: {self.name} city = {self.city} state = {self.state} desc = {self.desc}"
    
class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="dojos", on_delete= models.CASCADE)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __repr__(self):
        return f" dojo : {self.dojo} first_name = {self.first_name} last_name = {self.last_name}"
