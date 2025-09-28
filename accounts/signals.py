# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from workfiles.models import maindata


@receiver(post_save, sender=CustomUser)
def create_or_update_maindata(sender, instance, created, **kwargs):
    if created:
        # Check if maindata with the same natid exists
        try:
            maindata_instance = maindata.objects.get(natid=instance.natid)
            instance.maindata = maindata_instance
            instance.save()
        except maindata.DoesNotExist:
            pass  # Handle case where maindata instance does not exist



@receiver(post_save, sender=maindata)
def create_or_update_customuser(sender, instance, created, **kwargs):
    try:
        user_instance = CustomUser.objects.get(natid=instance.natid)
        user_instance.maindata = instance
        user_instance.save()
    except CustomUser.DoesNotExist:
        pass  # Handle case where CustomUser instance does not exist




@receiver(post_save, sender=CustomUser)
def link_maindata_to_user(sender, instance, created, **kwargs):
    if created:
        try:
            maindata_instance = maindata.objects.get(natid=instance.natid)
            instance.maindata = maindata_instance
            instance.save()
        except maindata.DoesNotExist:
            pass