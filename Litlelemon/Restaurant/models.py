from django.db import models
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    
    Name=models.CharField(max_length=100)
    No_of_guests=models.IntegerField()
    BookingDate=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.Name} : {str(self.BookingDate)}'

class Menu(models.Model):
   
    Title=models.CharField(max_length=100)
    Price=models.DecimalField(decimal_places=2,max_digits=10)
    Inventory=models.IntegerField()
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
