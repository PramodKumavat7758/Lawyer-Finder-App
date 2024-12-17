from django.db import models
from Lawyer_Finder import settings

class Lawyer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="lawyer_profile")
    address = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=15, null=False)
    email = models.EmailField(null=False)
    full_name = models.CharField(max_length=200, null=False)
    is_approved = models.BooleanField(default=False)

    # Additional profile details (editable by approved lawyers)
    qualifications = models.TextField(blank=True, null=True)
    specializations = models.TextField(blank=True, null=True)
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    court_duty = models.CharField(max_length=200, blank=True, null=True)
    total_cases = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# Blog Model
class Blog(models.Model):
    author = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_photos/', blank=True, null=True)

    def __str__(self):
        return self.title
