from django.db import models
from workfiles.models import maindata
# Create your models here.


'''
list of content
1- hos info 
2- main sections data 
3- lap and analysis sections info
    .
    .
    .
    .
    .
    .
    .
4- Radiology_Department sections info
    .
    .
    .
    .
    .
    .
    .
    .
5- Pharmacies sections info
    .
    .
    .
    .
    .
    .
    .
    .
    .
6- sergery sections info
    .
    .
    .
    .
    .
    .
    .
    .
    .
5- Warehouses sections info
    .
    .
    .
    .
    .
    .
    .
    .
    .
5- regulare sections info
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
5- rooms
5- clinics
5- beds
5- Employee
5- jop
5- Patients
5- Examinations
5- check
5- 
5- 
5- 
5- 
5- 
5- 

'''



# this class hold hospital mian info
class hospital(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(nall=True,blank=True)
    visions =models.TextField()
    massage = models.TextField()

# this class hold sictions name and relations with hospial  
class sections(models.Model):
    name = models.CharField(max_length=150)
    hos = models.ForeignKey(hospital, on_delete=models.CASCADE )
    leader = models.OneToOneField("app.Model", on_delete=models.CASCADE)
    




#lap and analysis sections info

#
class Laboratories(sections):
   


   

class laps(models.Model):
    name = models.CharField(max_length=150)
    lap = models.ForeignKey(Laboratories, on_delete=models.CASCADE )
    
    
class Analysis(models.Model):
    name = models.CharField(max_length=150)
    Patient_name = models.ForeignKey(Patients, on_delete=models.CASCADE )
    laps_name = models.ForeignKey(laps, on_delete=models.CASCADE )
    analysis_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name




class Analysis_row(models.Model):
    name = models.CharField(max_length=150)
    score = models.IntegerField()
    defult_value = models.IntegerField()
    analysis_name  = models.ForeignKey(Analysis, on_delete=models.CASCADE )
    



    def __str__(self):
        return self.name



# lap and analysis sections info end 






# Radiology_Department sections info
class Radiology_Department(sections):
   


class radioroom(models.Model):
    name = models.CharField(max_length=150)
    room = models.ForeignKey(Radiology_Department, on_delete=models.CASCADE )


class rays(models.Model):
    ray_name = models.CharField(max_length=150)
    Patient_name = models.ForeignKey(Patients, on_delete=models.CASCADE )
    radio_room_name = models.ForeignKey(laps, on_delete=models.CASCADE )
    analysis_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name






# Radiology_Department sections info end 




# Pharmacies sections info
class Pharmacies(sections):#


class pharma(models.Model):
    name = models.CharField(max_length=150)
    room = models.ForeignKey(Radiology_Department, on_delete=models.CASCADE )
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )   
    room_type = models.CharField(max_length=200, null=True, choices=CATEGORY)
    


class medic(models.Model):
    name = models.CharField(max_length=150)
    count_instore = models.IntegerField()
    medic_price = models.DecimalField(max_digits=10, decimal_places=2)


    


class despospel(models.Model):
    name = models.CharField(max_length=150)
    count_instore = models.IntegerField()
    despospel_price = models.DecimalField(max_digits=10, decimal_places=2)
    



# Pharmacies sections info end 












# sergery sections info
class sergerysections(sections):#


class oprations_rooms(models.Model):
    sergery = models.ForeignKey(sergery, on_delete=models.CASCADE )

    

class oprations_taple(models.Model):
    taple_num = models.IntegerField()

    

   



class oprations(models.Model):
    name = models.CharField(max_length=150)
    types = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
        ('Out Door', 'Out Door'),
        ('Out Door', 'Out Door'),
        ('Out Door', 'Out Door'),
    )   
    room_of_opratins = models.CharField(max_length=200, null=True, choices=types)





# sergery sections info end 















# Warehouses sections info
class Warehouses(sections):
    name = models.CharField(max_length=150)




class Warehouse_room(sections):
    name = models.CharField(max_length=150)








# Warehouses sections info end 






# regulare sections info
class sectionshagze(sections):





# regulare sections info end 










#
class rooms(models.model):
    roomnum = models.CharField(max_length=5)
    
    section = models.ForeignKey(sectionshagze, on_delete=models.CASCADE )
#
class clinics(models.Model):
    section = models.ForeignKey(sectionshagze, on_delete=models.CASCADE )
#
class beds(models.Model):
    room = models.ForeignKey(rooms, on_delete=models.CASCADE )
    typeofAdmission = models.CharField(max_length=150)










#
class Employee(models.Model):
    data = models.OneToOneField(maindata, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')

#
class jop(models.Model):
    pass










#
class Patients(models.Model):
    name = models.CharField(max_length=150)
    idnum = models.CharField(max_length=14)
    idimg1 = models.ImageField(nall=True,blank=True)
    idimg2 = models.ImageField(nall=True,blank=True)
    profilimg = models.ImageField(nall=True,blank=True)
    age = models.IntegerField()

#
class Examinations(models.Model):
    date = models.DateTimeField(auto_now=True)
    diagnosis = models.CharField(max_length=150 , default='under checks')
    complaine = models.TextField()
    treatment = models.CharField(max_length=150 , default='under checks')
    patent = models.ForeignKey(Patients, on_delete=models.CASCADE )
    clinic = models.ForeignKey(clinics, on_delete=models.CASCADE )


#
class check(models.Model):
    clinic = models.ForeignKey(clinics, on_delete=models.CASCADE )
    qashf = models.ForeignKey(Examinations, on_delete=models.CASCADE )




class Device(models.Model):
    name = models.CharField(max_length=150)
    jop_related = models.CharField(max_length=150)




'''
Laboratories
Pharmacies
Radiology Department
Warehouses
Warehouse
Items
Inventory

Reception
Patients
Medical Examination
Hospital Admission Department
Employee
Sample Analysis
Device
'''



"""class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # سعر المنتج الحالي

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # ربط المنتج
    quantity = models.PositiveIntegerField()  # الكمية
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # سعر المنتج وقت الطلب
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # الإجمالي
    created_at = models.DateTimeField(auto_now_add=True)  # وقت إنشاء الطلب

    def save(self, *args, **kwargs):
        # عند إنشاء الطلب، يتم حفظ السعر الحالي للمنتج
        if not self.pk:  # يتحقق إذا كان السجل جديدًا
            self.unit_price = self.product.price
            self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"طلب {self.product.name} - الكمية: {self.quantity}"


وكنت اذا المعامع اندبتنى  
       
       مضيت لها ونفسي لا تروغ


    """