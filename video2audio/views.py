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

        today = datetime.date.today()

        weekdays = [
            today.strftime("%A"),
            (today - datetime.timedelta(days=1)).strftime("%A"),
            (today - datetime.timedelta(days=2)).strftime("%A"),
            (today - datetime.timedelta(days=3)).strftime("%A"),
            (today - datetime.timedelta(days=4)).strftime("%A"),
            (today - datetime.timedelta(days=5)).strftime("%A"),
            (today - datetime.timedelta(days=6)).strftime("%A"),
        ]

        daily_users = [
            User.objects.filter(joined_at=today - datetime.timedelta(days=6)).count(),
            User.objects.filter(joined_at=today - datetime.timedelta(days=5)).count(),
            User.objects.filter(joined_at=today - datetime.timedelta(days=4)).count(),
            User.objects.filter(joined_at=today - datetime.timedelta(days=3)).count(),
            User.objects.filter(joined_at=today - datetime.timedelta(days=2)).count(),
            User.objects.filter(joined_at=today - datetime.timedelta(days=1)).count(),
            User.objects.filter(joined_at=today).count(),
        ]

        daily_conversions = [
            User.objects.filter(
                joined_at=today - datetime.timedelta(days=6), is_premium=True
            ).count(),
            User.objects.filter(
                joined_at=today - datetime.timedelta(days=5), is_premium=True
            ).count(),
            User.objects.filter(
                joined_at=today - datetime.timedelta(days=4), is_premium=True
            ).count(),
            User.objects.filter(
                joined_at=today - datetime.timedelta(days=3), is_premium=True
            ).count(),
            User.objects.filter(
                joined_at=today - datetime.timedelta(days=2), is_premium=True
            ).count(),
            User.objects.filter(
                joined_at=today - datetime.timedelta(days=1), is_premium=True
            ).count(),
            User.objects.filter(joined_at=today, is_premium=True).count(),
        ]

        january = datetime.date.today().replace(day=1, month=1)

        monthly_users = [
            User.objects.filter(joined_at__gte=january).count(),
            User.objects.filter(
                joined_at__gte=january + datetime.timedelta(days=30)
            ).count(),
            User.objects.filter(
                joined_at__gte=january + datetime.timedelta(days=60)
            ).count(),
            User.objects.filter(
                joined_at__gte=january + datetime.timedelta(days=90)
            ).count(),
            User.objects.filter(
                joined_at__gte=january + datetime.timedelta(days=120)
            ).count(),
            User.objects.filter(
                joined_at__gte=january + datetime.timedelta(days=150)
            ).count(),
            User.objects.filter(
                joined_at__gte=january + datetime.timedelta(days=180)
            ).count(),
            User.objects.filter(
                joined_at__gte=january + datetime.timedelta(days=210)
            ).count(),
        ]
        return render(
            request,
            "index.html",
            {
                "weekdays": str(weekdays),
                "users": users,
                "users_today": users_today,
                "conversions": conversions,
                "conversions_today": conversions_today,
                "premium_users": premium_users,
                "premium_users_today": premium_users_today,
                "daily_users": daily_users,
                "monthly_users": monthly_users,
                "daily_conversions": daily_conversions,
            },
        )
