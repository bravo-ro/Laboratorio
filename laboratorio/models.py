from django.db import models


class CategoriaQuimica(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    ubicacion = models.CharField('ubicación', max_length=80)  
    descripcion = models.TextField('descripción', blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'categoría química'
        verbose_name_plural = 'categorías químicas'

    def __str__(self):
        return self.nombre


class Reactivo(models.Model):
    UNIDADES = [('g', 'g'), ('kg', 'kg'), ('mL', 'mL'), ('L', 'L')]

    categoria = models.ForeignKey(
        CategoriaQuimica,
        on_delete=models.PROTECT, 
        related_name='reactivos',
        verbose_name='categoría',
    )
    nombre = models.CharField(max_length=120)                     
    numero_cas = models.CharField('número CAS', max_length=12)
    uso = models.TextField()
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)  
    unidad = models.CharField(max_length=2, choices=UNIDADES)
    fecha_vencimiento = models.DateField('fecha de vencimiento')  
    es_peligroso = models.BooleanField('peligroso', default=False) 

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.numero_cas})'