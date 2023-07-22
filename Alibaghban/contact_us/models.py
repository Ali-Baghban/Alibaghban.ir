from django.db import models
from datetime import datetime

class Message(models.Model):
    name        = models.CharField(max_length=200)
    email       = models.EmailField()
    subject     = models.CharField(max_length=300)
    message     = models.TextField()
    sent_time   = models.DateTimeField(default=datetime.now())
    checked     = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
