from django.db import models

from accounts.models import User

class Report(models.Model):
    UTILITY_CHOICES = (
        ('water', 'Water'),
        ('electricity', 'Electricity'),
        ('road', 'Road'),
        ('waste', 'Waste Management'),
        ('streetlight', 'Street Light'),
        ('other', 'Other'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    utility_type = models.CharField(max_length=20, choices=UTILITY_CHOICES)
    location = models.CharField(max_length=255)
    gps_coordinates = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    photo = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.utility_type} - {self.location}"
