from django.db import models

# Create your models here.

class maindata(models.Model):
    name = models.CharField(max_length=70)
    natid = models.CharField(max_length=14)
    phone = models.CharField(max_length=11)
    addres_location = models.CharField(max_length=100)
    deg = models.CharField(max_length=50)
    work = models.CharField(max_length=50,blank=True, null=True)
    work_rank = models.CharField(max_length=50)
    frest_work_place = models.CharField(max_length=100 ,blank=True, null=True)
    carant_work_place = models.CharField(max_length=100 ,blank=True, null=True)
    work_starting_date = models.DateField(auto_now=False, auto_now_add=False)
    hospital_work_starting_date = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name




class breakstime(models.Model):
    person = models.ForeignKey(maindata, on_delete=models.CASCADE)
    breakstime_desc = models.CharField(max_length=100)
    start_from = models.DateField()
    end_from = models.DateField()
   
    def __str__(self):
        return "{} - {}".format(self.person ,self.breakstime_desc)




class fileimg(models.Model):
    file = models.ForeignKey(maindata, on_delete=models.CASCADE)
    img_desc = models.CharField(max_length=100)
    imgs = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.img_desc






