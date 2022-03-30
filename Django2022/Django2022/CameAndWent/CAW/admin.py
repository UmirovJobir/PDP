from django.contrib import admin

from .models import Came, Went, CameAndWent


@admin.register(Came)
class CameAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name", "section", "arrival_time")
    list_display = ("first_name", "last_name", "section", "arrival_time")
    list_filter = ("first_name", "last_name", "section", "arrival_time")


admin.site.register(Went)
admin.site.register(CameAndWent)

# @admin.register(Came)
# class MovieShotsAdmin(admin.ModelAdmin):
#     list_display = ("first_name", "last_name", "section", "arrival_time",)
#     readonly_fields = ("arrival_time",)

# class Came_Admin(admin.ModelAdmin):
#     list_display = ["first_name", "last_name", "section", "arrival_time"]
#     search_fields = ['first_name']
#     readonly_fields = ("arrival_time",)
#
#     class Meta:
#         model = Came
#
#     # def get_queryset(self, request):
#     #     return Came.objects.filter(active=True)
#
# admin.site.register(Came, Came_Admin)
