from django.db import models
from datetime import datetime


class Employee(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombre')
    dpi = models.CharField(max_length=13, verbose_name='No. DPI')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Registro')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    cvitae = models.FileField(upload_to='cvitae/%y/%m/%d', null=True, blank=True)


    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
