from django.db import models

class Author(models.Model):
    name = models.CharField(("Name"), max_length=50)
    email = models.EmailField(("email"), max_length=254)
    
    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    title = models.CharField(("Title"), max_length=50)
    published = models.DateField(("Date Published"), auto_now=False, auto_now_add=False)
    author = models.ForeignKey("Author", verbose_name=("Author"), on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title