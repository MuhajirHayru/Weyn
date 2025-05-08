from django.contrib import admin
from .models import fooditem, drinkitem, Order

# Register food and drink items
admin.site.register(fooditem)
admin.site.register(drinkitem)

# Custom filter for 'visible' field
class VisibleFilter(admin.SimpleListFilter):
    title = 'Visibility'
    parameter_name = 'visible'

    def lookups(self, request, model_admin):
        return (
            ('all', 'All Orders'),
            ('visible', 'Visible Orders'),
            ('hidden', 'Hidden Orders'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'visible':
            return queryset.filter(visible=True)
        if self.value() == 'hidden':
            return queryset.filter(visible=False)
        return queryset  # Return all orders by default

# Custom action to hide selected orders
@admin.action(description="Hide selected orders from admin list")
def hide_selected_orders(modeladmin, request, queryset):
    queryset.update(visible=False)

# Customize Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone_number', 'items', 'total_price', 'date_ordered')
    actions = [hide_selected_orders]
    list_filter = (VisibleFilter,)  # Add the custom filter here

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.username == 'muhajirhayru18@gmail.com':
            return qs.filter(visible=True)
        return qs  # Show all orders (including hidden) for other users

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username == 'muhajirhayru18@gmail.com':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

# Register Order model with the custom admin
admin.site.register(Order, OrderAdmin)
