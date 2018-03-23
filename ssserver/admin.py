from django.contrib import admin
from . import models


class SSUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'level', 'port', 'traffic', 'fulltraffic', ]

    def fulltraffic(self, obj):
        return '{} GB'.format(obj.transfer_enable / 1024 / 1024 / 1024)
    fulltraffic.short_description = '总流量'

    def traffic(self, obj):
        return '{} GB'.format(obj.get_traffic())
    traffic.short_description = '使用流量'

    search_fields = ['user__username', 'user__email', 'port', 'user__pk']


class TrafficLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'node_id', 'traffic', 'log_date', ]  # TODO: node_id是用来排序的，不能删除（update：不知道能不能删除）


class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'level',
                    'human_used_traffic', 'human_total_traffic', 'show', ]


class NodeOnlineAdmin(admin.ModelAdmin):
    list_display = ['id', 'online_user']


class NodeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'load']


class AliveIpAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ip', 'log_time']


# Register your models here.
admin.site.register(models.SSUser, SSUserAdmin)
admin.site.register(models.TrafficLog, TrafficLogAdmin)
admin.site.register(models.Node, NodeAdmin)
admin.site.register(models.NodeOnlineLog, NodeOnlineAdmin)
admin.site.register(models.NodeInfoLog, NodeInfoAdmin)
admin.site.register(models.AliveIp, AliveIpAdmin)
