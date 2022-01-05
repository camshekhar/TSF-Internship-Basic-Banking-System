from django.db import models

# Customer Details Model...
class CustomerDetail(models.Model):
    profile_pic = models.ImageField(upload_to="images", default="images/profilepic.jpg")
    name = models.CharField(max_length=100, null=True)
    dob = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    acc_number = models.CharField(max_length=15, null=True)
    curr_balance = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

# Transfer Details Model...
class Transfer(models.Model):
    sender_name = models.CharField(max_length=100, null=True)
    receiver_name = models.CharField(max_length=100, null=True)
    amount = models.IntegerField(default=0)
    trans_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.receiver_name