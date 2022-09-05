from django.contrib import admin

from UserAdmin.models import Cloud
from .models import Cloud
from django.utils.html import format_html

class CloudAdmin(admin.ModelAdmin):
    list_display=("id","name","lessData","Address","click_me")
    list_display_links=("id","name","Address","lessData","click_me")

    def lessData(self,obj):
        print(obj)
        return format_html(f'<span style="color:red"> {obj.Address[:10]}</span>')

    def click_me(self,obj):
        return format_html("<button>view</button>")


admin.site.register(Cloud,CloudAdmin)