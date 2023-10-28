from django.db import models

# Define a model for the scheduled social media posts
class ScheduledPost(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
    ]

    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    post_content = models.TextField()
    schedule_time = models.DateTimeField()

    def __str__(self):
        return f"{self.platform} Post - {self.schedule_time}"
