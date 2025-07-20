from django.shortcuts import render

from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    table_header = [
        "نام کارمند",
        "نام سازمان",
        "شهر",
        "پست سازمانی",
        "شماره داخلی",
        "شماره تماس",
    ]
    return render(
        request,
        "contact/index.html",
        {"contacts": contacts, "table_header": table_header},
    )
