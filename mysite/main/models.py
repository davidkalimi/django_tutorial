from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('APARTMENT', 'דירה'),
        ('VILLA', 'וילה'),
        ('LOT', 'מגרש'),
        # הוסף אפשרויות נוספות לפי הצורך
    ]

    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE_CHOICES, default='APARTMENT')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    square_meters = models.PositiveIntegerField()
    num_rooms = models.PositiveSmallIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    elevator = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    mamad = models.BooleanField(default=False)  # ממ"ד
    air_conditioning = models.BooleanField(default=False)
    sun_boiler = models.BooleanField(default=False)  # דוד שמש
    storage = models.BooleanField(default=False)
    renovated = models.BooleanField(default=False)
    access_for_disabled = models.BooleanField(default=False)
    num_floors_in_building = models.PositiveIntegerField(null=True, blank=True)
    floor_number = models.PositiveIntegerField(null=True, blank=True)
    avg_annual_yield = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # תשואה שנתית ממוצעת
    avg_rent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # שכר דירה ממוצע
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    neighborhood_score = models.JSONField(null=True, blank=True)  # ציוני שכונה (מילון של ערכים)

    def __str__(self):
        return f"{self.title} - {self.location}"

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='investments')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='investments')
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # אחוז ההשקעה בנכס
    amount = models.DecimalField(max_digits=12, decimal_places=2)  # סכום ההשקעה
    date_invested = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # סטטוס ההשקעה (אקטיבית/לא אקטיבית)
    referral_code = models.CharField(max_length=20, null=True, blank=True)  # קוד להפניה למתווכים

    def __str__(self):
        return f"{self.user.username} - {self.percentage}% of {self.property.title}"



class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('REGULAR', 'רגיל'),
        ('PREMIUM', 'פרימיום'),
        ('BROKER', 'מתווך'),
        ('ADMIN', 'מנהל מערכת')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='REGULAR')
    identification_verified = models.BooleanField(default=False)  # מאמת אם המשתמש עבר את הוולידציה
    
    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"