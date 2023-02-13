from django.db import models

class Togri(models.Model):
    soz = models.CharField(max_length=100)

class Notogri(models.Model):
    n_soz = models.CharField(max_length=100)
    t_soz = models.ForeignKey(Togri, on_delete=models.CASCADE)

# >>> Togri.objects.create(soz='xohish')
# <Togri: Togri object (1)>
# >>> Togri.objects.create(soz="xo'p")
# <Togri: Togri object (2)>
# >>> Togri.objects.create(soz="havas")
# <Togri: Togri object (3)>
# >>> Togri.objects.create(soz="ahvol")
# <Togri: Togri object (4)>
# >>> Togri.objects.create(soz="xolos")
# <Togri: Togri object (5)>
# >>> Togri.objects.create(soz="hovli")
# <Togri: Togri object (6)>
# >>> Togri.objects.create(soz="ehtimol")
# <Togri: Togri object (7)>
# >>> Togri.objects.create(soz="halol")
# <Togri: Togri object (8)>
# >>> Togri.objects.create(soz="xursand")
# <Togri: Togri object (9)>
# >>> Togri.objects.create(soz="ham")
# <Togri: Togri object (10)>
# >>> Togri.objects.create(soz="hamshira")
# <Togri: Togri object (11)>
# >>> Togri.objects.create(soz="hona")
# <Togri: Togri object (12)>
# >>> Togri.objects.create(soz="hozir")
# <Togri: Togri object (13)>

