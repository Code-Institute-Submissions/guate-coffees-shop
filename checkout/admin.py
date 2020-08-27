from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 
        'username',
        'date',
        'delivery_cost', 
        'order_total',
        'grand_total', 
        'original_cart',
        'stripe_pid',
        )

    fields = (
        'order_number',
        'username',
        'date',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'street_address_1',
        'street_address_2',
        'town_or_city',
        'state',
        'postcode',
        'country',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_cart',
        'stripe_pid',
        )

    list_display = (
        'order_number',
        'date',
        'username',
        'last_name',
        'order_total',
        'delivery_cost',
        'grand_total',
        )

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
