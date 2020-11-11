from __future__ import unicode_literals

from django.contrib import admin
from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    image = models.ImageField(upload_to='images/', null=True) # require Pillow : pip install Pillow
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        # db_table = "configuration"
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    # exclude = ['createdAt', 'createdBy', 'updatedAt', 'updatedBy']
    fields = ('description', 'document', 'image', )
    list_display = ('id', 'description', 'document', 'image', 'uploaded_at',  )
    list_display_links = ('id', )
    search_fields = ('id', )
    ordering = ('id', )