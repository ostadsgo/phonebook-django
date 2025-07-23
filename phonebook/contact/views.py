from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Contact


def index(request):
    query = request.GET.get('q')
    if query:
        contact_list = Contact.objects.filter(employee_name__icontains=query) # type: ignore
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
    pg_num = request.GET.get("pg_num", 10)

    # Paginator
    paginator = Paginator(contact_list, int(pg_num))
    page_number = request.GET.get("page")
    contacts = paginator.get_page(page_number)
    

    print('-' * 50)
    print(request.GET)
    print('-' * 50)


    return render(
        request,
        "contact/index.html",
        {"contacts": contacts, "table_header": table_header, "pg_num": pg_num},
    )
