from django.contrib import admin

from bot import models


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'command',
        'next_step',
    )
    search_fields = (
        'command',
        'next_step',
    )


@admin.register(models.Step)
class StepAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'delay',
        'date_of_begin',
    )
    search_fields = (
        'title',
        'message',
        'delay',
        'date_of_begin',
    )


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'vk_id',
        'step',
    )
    search_fields = (
        'name',
        'vk_id',
    )
    list_filter = (
        'step',
    )
