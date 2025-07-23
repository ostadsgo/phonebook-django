from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Contact


def index(request):
    query = request.GET.get("q")
    if query:
        contact_list = Contact.objects.filter(employee_name__icontains=query)  # type: ignore
    else:
        contact_list = Contact.objects.all()  # type: ignore

    table_header = [
        "نام کارمند",
        "نام سازمان",
        "شهر",
        "پست سازمانی",
        "شماره داخلی",
        "شماره تماس",
    ]

    # Paginator number
    page_size = request.GET.get("page_size", 10)

    # Paginator
    paginator = Paginator(contact_list, int(page_size))
    page_number = request.GET.get("page")
    contacts = paginator.get_page(page_number)

    return render(
        request,
        "contact/index.html",
        {"contacts": contacts, "table_header": table_header, "page_size": page_size},
    )


def bakhtar_group(request):
    query = request.GET.get("q")
    if query:
        contact_list = Contact.objects.filter(company_name__icontains=query)  # type: ignore
    else:
        contact_list = Contact.objects.values("company_name", "interal_phone")

    
    # Paginator number
    page_size = request.GET.get("page_size", 10)

    # Paginator
    paginator = Paginator(contact_list, int(page_size))
    page_number = request.GET.get("page")
    contacts = paginator.get_page(page_number)

    table_header = [
        "نام سازمان",
        "شماره داخلی",
    ]
    return render(
        request,
        "contact/group.html",
        {"contacts": contacts, "table_header": table_header, "page_size": page_size},
    )
