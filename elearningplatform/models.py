from django.db import models
class Multichoice(models.Model):
    pass
class Articles2(models.Model):
    title=models.CharField(max_length=100)
    textdata=models.CharField(max_length=5000)
    def __str__(self):
        return self.textdata
class Videotutorial(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=50)
    videoclip=models.URLField(max_length=500)
    def __str__(self):
        return self.title
class Add_Questions(models.Model):
    Question = models.CharField(max_length=20000,null=True, unique=True)
    A = models.CharField(max_length=20000,null=True, blank=True)
    B = models.CharField(max_length=20000,null=True,blank=True)
    C = models.CharField(max_length=20000,null=True,blank=True)
    D = models.CharField(max_length=20000,null=True,blank=True)
    E=models.CharField(max_length=20000, null=True,blank=True)
    Answer = models.CharField(max_length=20000,null=True ,blank=True)
    Answer_expalanation=models.CharField(max_length=20000,null=True,blank=True)
    
    def __str__(self):
        return self.Question
        
    

# Create your models here.
