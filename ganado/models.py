from django.db import models
from ingresos.models import Company, Client
from planta_alimentos.models import Formula
from vacunas.models import Vacuna



class FierroO(models.Model):
    codigo = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='fierros/o', blank=True, null=True)

    def __unicode__(self):
        return self.codigo

class FierroN(models.Model):
    codigo = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='fierros/n', blank=True, null=True)

    def __unicode__(self):
        return self.codigo

class SaleNote(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    kilograms = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    client = models.ForeignKey(Client, related_name='sale_notes', on_delete=models.SET_NULL, blank=True, null=True)
    carro = models.CharField(max_length=100, blank=True, null=True)
    chofer = models.CharField(max_length=100, blank=True, null=True)
    flete = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    # def __str__(self):
    #     return 'nota {} del cliente'.format(self.id, self.client.client)
        
    def __unicode__(self):
        return 'nota {} del cliente'.format(self.id, self.client.client)


class Factura(models.Model):
    factura = models.CharField(max_length=100, blank=True, null=True)

    # def __str__(self):
    #     return self.factura

    def __unicode__(self):
        return self.factura

    class Meta:
        ordering = ["-id"]

class Raza(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __unicode__(self):
        return self.name

class Corral(models.Model):
    
    fecha_generacion = models.DateTimeField(auto_now_add=True, db_index=True)
    no_corral = models.CharField(max_length=100, unique=True)
    comentarios = models.TextField()
    status = models.BooleanField(default=True)
    numero_serial = models.CharField(max_length=100, null=True, blank=True)
    # numero_semana = models.PositiveIntegerField(default=0)
    # ano = models.PositiveIntegerField(default=2010)
    
    # mes = models.CharField(max_length=100, choices=MONTHS, )
    # cuarto = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return "Corral no. {}".format(self.no_corral)

class Lote(models.Model):
    name = models.CharField(max_length=130, unique=True)
    status = models.BooleanField(default=True)
    corral = models.OneToOneField(Corral, related_name='lotes', on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']



class Animal(models.Model):
   
    TIPOA = (('becerro', 'becerro'),
            ('toro', 'toro'),
            ('vaca', 'vaca'),
            ('vaquilla', 'vaquilla')
            )
    arete_siniga = models.CharField(max_length=30, blank=True, null=True, unique=True)
    arete_rancho = models.CharField(max_length=30, blank=True, null=True)
    fecha_entrada = models.DateTimeField(auto_now_add=False, db_index=True, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, db_index=True, blank=True, null=True)
    peso_entrada = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    costo_kilo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    raza = models.ForeignKey(Raza, related_name='animals', on_delete=models.SET_NULL, blank=True, null=True)
    color = models.CharField(max_length=150, blank=True, null=True)
    #comentarios = models.TextField()
    owner = models.CharField(max_length=150, blank=True, null=True)
    lote = models.ForeignKey(Lote, related_name='animals', on_delete=models.SET_NULL, blank=True, null=True)
    tipo_animal = models.CharField(max_length=100, choices=TIPOA, blank=True, null=True)
    
    status = models.BooleanField(default=True)
    costo_inicial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fierro_original = models.ImageField(upload_to='fierrosO/', blank=True, null=True)
    fierro_nuevo = models.ImageField(upload_to='fierrosN/', blank=True, null=True)
    ref_factura_original = models.ForeignKey(Factura, related_name='animals', blank=True, null=True, on_delete=models.SET_NULL)
    merma = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.ForeignKey(Company, related_name='animals', blank=True, null=True, on_delete=models.SET_NULL)

    sale_note = models.ForeignKey(SaleNote, related_name='animals', on_delete=models.SET_NULL, blank=True, null=True)

    fierroO = models.ForeignKey(FierroO, related_name="animals", on_delete=models.SET_NULL, blank=True, null=True)
    fierroN = models.ForeignKey(FierroN, related_name="animals", on_delete=models.SET_NULL, blank=True, null=True)
    #new things for reportes
    days_in_ranch = models.CharField(max_length=100, blank=True, default="0")
    kg_hechos = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    conversion = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    rendimiento = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    costo_por_dia = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    ganacia_diaria_promedio = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    otromas = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
#yaa
    def last_pesada(self):
        return self.pesadas.last()

    
    # def __str__(self):
    #     return self.arete_rancho

    def __unicode__(self):
        return self.arete_rancho

    class Meta:
        ordering = ['-id']


class GastoAnimal(models.Model):
    TIPO=(
    ('Alimento','Alimento'),
    ('Vacuna', 'Vacuna'))
    created = models.DateField(auto_now_add=False, blank=True, null=True)
    animal = models.ForeignKey(Animal, related_name='aliments', on_delete=models.PROTECT, null=True, blank=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    unity = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=100, choices=TIPO, blank=True, null=True)
    formula = models.ForeignKey(Formula, related_name='gastos_animal', on_delete=models.PROTECT, blank=True, null=True) 
    vacuna = models.ForeignKey(Vacuna, related_name='gastos_animal',  on_delete=models.PROTECT, blank=True, null=True)
    insumo = models.CharField(max_length=100, null=True, blank=True)
    insumo_q = models.IntegerField(blank=True, null=True)
    insumo_cost = models.IntegerField(blank=True, null=True)
    
    # def __str__(self):
    #     return "Gasto no. {}, {} ".format(self.id, self.tipo)

    def __unicode__(self):
        return "Gasto no. {}, {} ".format(self.id, self.tipo)
    class Meta:
        ordering = ["-created"]

class Peso(models.Model):
  created = models.DateField(auto_now_add=True)
  peso = models.DecimalField(max_digits=10, decimal_places=2)
  animal = models.ForeignKey(Animal, related_name='pesadas', on_delete=models.PROTECT)

  def __unicode__(self):
    return "Animal {} Weigths {} kg".format(self.animal.id, self.peso)








