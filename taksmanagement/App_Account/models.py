from django.db import models

#To Create Custom User Model And Admin Panel
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
#for send error message and successmessage
from django.utils.translation import gettext_lazy

#For Autometically create one to one objects
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyUserManager(BaseUserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("The Email Must Be Set !")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super User Must Have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super User Must Have is_superuser=True")
        
        return self._create_user(email,password,**extra_fields)
    

class User(AbstractBaseUser,PermissionsMixin):
    username=None
    email=models.EmailField(unique=True,null=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []
    objects=MyUserManager()
    is_staff=models.BooleanField(
        gettext_lazy('staff status'),
        default=False,
        help_text=gettext_lazy("Designates Wheter the User can log in this site")
    )
    is_active=models.BooleanField(
        gettext_lazy('active'),
        default=True,
        help_text=('Designates Whether This User Should Be Trated as Actice.Unselect This Instead Of Deleting')
    )
    
    
    def __str__(self) :
        return str(self.email)
    def get_full_name(self):
        return str(self.email)
    def get_short_name(self):
        return str(self.email)
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    username=models.CharField(max_length=264,blank=True)
    full_name=models.CharField( max_length=264,blank=True)
    address=models.TextField(max_length=300,blank=True)
    city=models.CharField( max_length=64,blank=True)
    zipcode=models.CharField( max_length=64,blank=True)
    country=models.CharField( max_length=64,blank=True)
    phone=models.CharField( max_length=20,blank=True)
    date_join=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.username) + " " + str(self.user) 
    
    def is_fully_filled(self):
        fields_name=[f.name for f in self._meta.get_fields()]
        
        for field_name in fields_name:
            value = getattr (self,field_name)
            if value is None or value=='':
                return False
            return True
                
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()