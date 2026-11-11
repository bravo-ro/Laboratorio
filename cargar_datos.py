from datetime import timedelta
from decimal import Decimal

from django.utils import timezone

from laboratorio.models import CategoriaQuimica, Reactivo

categorias = {
    'Ácidos inorgánicos': 'Armario de corrosivos',
    'Bases': 'Armario de corrosivos',
    'Solventes orgánicos': 'Gabinete de inflamables',
    'Oxidantes': 'Estante de oxidantes',
    'Sales e indicadores': 'Estante general',
}
cat = {}
for nombre, ubicacion in categorias.items():
    cat[nombre], _ = CategoriaQuimica.objects.get_or_create(
        nombre=nombre, defaults={'ubicacion': ubicacion},
    )

reactivos = [
    ('Ácido sulfúrico 95-97 %', '7664-93-9', 'Ácidos inorgánicos', '2.5', 'L', 900, 'Titulaciones y ajuste de pH.', True),
    ('Ácido clorhídrico 37 %', '7647-01-0', 'Ácidos inorgánicos', '1', 'L', 600, 'Soluciones patrón.', True),
    ('Ácido nítrico 65 %', '7697-37-2', 'Ácidos inorgánicos', '1', 'L', 25, 'Digestión de muestras.', True),
    ('Hidróxido de sodio', '1310-73-2', 'Bases', '1', 'kg', 1200, 'Soluciones valorantes.', True),
    ('Amoníaco 25 %', '1336-21-6', 'Bases', '1', 'L', 300, 'Preparación de tampones.', True),
    ('Etanol absoluto', '64-17-5', 'Solventes orgánicos', '2.5', 'L', 1500, 'Extracciones y desinfección.', True),
    ('Acetona', '67-64-1', 'Solventes orgánicos', '5', 'L', 800, 'Limpieza de material de vidrio.', True),
    ('Metanol', '67-56-1', 'Solventes orgánicos', '1', 'L', -15, 'Fase móvil en HPLC.', True),
    ('Permanganato de potasio', '7722-64-7', 'Oxidantes', '0.5', 'kg', 700, 'Titulaciones redox.', True),
    ('Peróxido de hidrógeno 30 %', '7722-84-1', 'Oxidantes', '1', 'L', 20, 'Oxidación en digestiones.', True),
    ('Cloruro de sodio', '7647-14-5', 'Sales e indicadores', '1', 'kg', 2000, 'Soluciones salinas.', False),
    ('Sacarosa', '57-50-1', 'Sales e indicadores', '500', 'g', 1000, 'Medios de cultivo y patrones.', False),
    ('Fenolftaleína', '77-09-8', 'Sales e indicadores', '100', 'g', 1000, 'Indicador ácido-base.', True),
]

hoy = timezone.localdate()
for nombre, cas, categoria, cantidad, unidad, dias, uso, peligroso in reactivos:
    _, creado = Reactivo.objects.get_or_create(
        nombre=nombre, numero_cas=cas,
        defaults={
            'categoria': cat[categoria], 'cantidad': Decimal(cantidad), 'unidad': unidad,
            'fecha_vencimiento': hoy + timedelta(days=dias), 'uso': uso, 'es_peligroso': peligroso,
        },
    )
    print(f"{nombre:<28} | {'creado' if creado else 'ya existía'}")

print(f'\nTotal: {CategoriaQuimica.objects.count()} categorías, {Reactivo.objects.count()} reactivos.')