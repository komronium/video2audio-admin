import datetime

from django.shortcuts import render
from django.views import View

from video2audio.models import Conversion, Payment, User


class HomeView(View):
    def get(self, request):
        users = User.objects.count()
        users_today = User.objects.filter(joined_at=datetime.date.today()).count()
        conversions = Conversion.objects.count()
        conversions_today = Conversion.objects.filter(
            created_at=datetime.date.today()
        ).count()
        premium_users = User.objects.filter(is_premium=True).count()
        premium_users_today = User.objects.filter(
            is_premium=True, joined_at=datetime.date.today()
        ).count()

        return render(
            request,
            "index.html",
            {
                "users": users,
                "users_today": users_today,
                "conversions": conversions,
                "conversions_today": conversions_today,
                "premium_users": premium_users,
                "premium_users_today": premium_users_today,
            },
        )
