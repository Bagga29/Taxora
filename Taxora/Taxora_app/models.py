from django.db import models

class SignupLead(models.Model):
    ROLE_CHOICES = [
        ("sme", "Small Business Owner"),
        ("ca", "Chartered Accountant"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField(unique=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_role_display()} - {self.email}"
