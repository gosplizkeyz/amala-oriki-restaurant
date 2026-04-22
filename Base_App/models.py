from django.db import models
import uuid

# Create your models here.

class ItemList(models.Model):
    CATEGORY_TYPE = (
        ('food', 'Food'),
        ('snack', 'Snack'),
    )

    Category_name = models.CharField(max_length=50)
    category_type = models.CharField(max_length=10, choices=CATEGORY_TYPE, default='food')

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    item_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True, null=True)  # keep but optional
    category = models.ForeignKey(ItemList, related_name="items", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Items/', blank=True)

    def __str__(self):
        return self.item_name


class AboutUs(models.Model):
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.description



class Feedback(models.Model):
    user_name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='feedback_images/', null=True, blank=True)  # Save inside /media/feedback_images/
    
    def __str__(self):
        return self.user_name
    


class BookTable(models.Model):
    user_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    total_person = models.IntegerField()
    booking_date = models.DateField()
    
    def __str__(self):
        return self.user_name


#FOR THE SPIN
class SpinReward(models.Model):
    code = models.CharField(max_length=20, unique=True)
    reward = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reward} - {self.code}"