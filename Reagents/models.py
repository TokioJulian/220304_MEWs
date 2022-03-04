from django.db import models

# Create your models here.

class Reagent(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    purpose = models.CharField(max_length=255, blank=True)
    reference = models.CharField(max_length=255, blank=True)
    LotNo = models.CharField(max_length=255, unique=True, blank=True)

    #------------------------------------------------------------------------
    date_prepared = models.DateField(null=True)
    person_preparing = models.CharField(max_length=255, blank=True)
    #validation_duration = models.DurationField(blank=True)
    #expires_on = date_prepared + validation_duration
    expires_on = models.DateField(blank=True, null=True)
    confirmed_by = models.CharField(
                                    max_length=255,
                                    blank=True
                                    )
    confirmed_on = models.DateField(blank=True, null=True)
    #------------------------------------------------------------------------
    date_finished = models.DateField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True)
    #------------------------------------------------------------------------
    dillution_medium = models.CharField(max_length=255, blank=True)
    final_qty = models.FloatField( blank=False, null=False )
    unit = models.CharField(max_length=5, blank=False)
    note = models.TextField(blank=True )
    ingredient = models.ManyToManyField('self',
                                         related_name='ingredient',
                                         #on_delete = models.DO_NOTHING,
                                         blank=True, 
                                        #  null=True 
                                         )
    #------------------------------------------------------------------------
    # image01 = models.ImageField(blank=True, null=True)
    # image02 = models.ImageField(blank=True, null=True)
    # image03 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name



# class Ingredient(models.Model):
#     name = models.CharField(max_length=255, blank=False)
#     maker = models.CharField(max_length=255, default='和光', blank=False)
#     grade = models.CharField(max_length=255)
#     LotNo = models.CharField(max_length=255)
#     qty = models.FloatField()
#     unit = models.CharField(max_length=5)
#     used_for = models.ForeignKey(Reagent, on_delete=models.DO_NOTHING)