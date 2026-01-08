from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    conversation_count = models.IntegerField(default=0)
    joined_at = models.DateField(default=timezone.now)
    diamonds = models.IntegerField(default=0)
    is_premium = models.BooleanField(default=False)
    lang = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"

    def __str__(self):
        return f"{self.name} ({self.user_id})"


class Conversion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversions")
    success = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Conversion"
        verbose_name_plural = "Conversions"
        db_table = "conversions"

    def __str__(self):
        return f"Conversion {self.id} for {self.user}"


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    diamonds = models.IntegerField(default=0)  # 💎 sotib olingan diamondlar
    is_lifetime = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        db_table = "payments"

    def __str__(self):
        return f"Payment {self.id} for {self.user}"
