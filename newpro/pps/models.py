from django.db import models

# Create your models here.

    
    
class fooditem(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField()
    catagory=[('breakfast','breakfast'),
              ('lunch_and_dinner','lunch'),]
    
    Fstatus=models.CharField(max_length=100 ,choices=catagory,default='breakfast')
    price=models.DecimalField(max_digits=12,decimal_places=3)
    type = models.CharField(max_length=20, choices=[('food', 'Food'), ('drink', 'Drink')], default='food')
    quantity=models.IntegerField(default=0)
    description=models.TextField(null=True,blank=True)
    
    def  __str__(self):
        return self.title      
class drinkitem(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField()
    catagory=[('juice','juice'),
             ('hot_drink','hot_drink'),
             ('soft_drinks','soft_drinks'),]
    
    Dstatus=models.CharField(max_length=100 ,choices=catagory,default='juice')
    price=models.DecimalField(max_digits=12,decimal_places=3)
    type = models.CharField(max_length=20, choices=[('food', 'Food'), ('drink', 'Drink')], default='drink')
    quantity=models.IntegerField()
    description=models.TextField(null=True,blank=True)
    
    def  __str__(self):
        return self.title

from datetime import datetime, time


from django.db import models
import json
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    items = models.TextField()  # Store items as a JSON string
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    hidden_for_user = models.CharField(max_length=255, blank=True, null=True)  # Track username instead of email
    def get_items(self):
        return json.loads(self.items)  # Convert JSON string back to a dictionary

    def __str__(self):
        return f"Order by {self.customer_name} on {self.date_ordered}"



        

    
    


    
    