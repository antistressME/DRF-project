from django.contrib import admin

from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = (
        "id",
        "user",
        "payment_date",
        "paid_course",
        "paid_lesson",
        "payment_sum",
        "payment_method",
    )
