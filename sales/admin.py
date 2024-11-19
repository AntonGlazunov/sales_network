from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from sales.models import Factory, Retail, IE, Contacts, Product


@admin.action(description="Удалить задолженость у выбраных обьектов")
def make_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier_link', 'contact__city', 'debt_rub')
    list_filter = ['contact__city', ]
    actions = [make_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            link = reverse("admin:sales_factory_change", args=[obj.supplier.pk])
            return format_html('<a href="{}">{}</a>', link, obj.supplier)
        else:
            return None
    supplier_link.short_description = "Поставщик"

    def debt_rub(self, obj):
        return f'{obj.debt/100} ₽'
    debt_rub.short_description = 'Задолженость'


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact__city',)
    list_filter = ['contact__city',]


@admin.register(IE)
class IEAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier_link', 'contact__city', 'debt_rub')
    list_filter = ['contact__city', ]
    actions = [make_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            link = reverse("admin:sales_factory_change", args=[obj.supplier.pk])
            return format_html('<a href="{}">{}</a>', link, obj.supplier)
        else:
            return None
    supplier_link.short_description = "Поставщик"

    def debt_rub(self, obj):
        return f'{obj.debt/100} ₽'
    debt_rub.short_description = 'Задолженость'

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model',)
