from django.db import models , User
#from depart.models import AppUser
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid


class BaseModel(models.Model):
    uid= models.UUIDField(default=uuid.uuid4 , editable=False , primary_key=True)
    created_at= models.DateField(auto_now_add= True)
    updated_at =models.DateField(auto_now_add= True)
    
    class Meta:
        abstract = True
    
class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=256)
    icon = models.ImageField(upload_to='amenities/')
    
    def __str__(self) -> str:
        return self.amenity_name
    

class Facilities(BaseModel):
    facility_name = models.CharField(max_length=128)
    
class Club(BaseModel):
    club_name=  models.CharField(max_length=128 , null=False)
    club_price = models.IntegerField()
    description = models.TextField()
    amenities = models.ManyToManyField(Amenities, related_name="clubs")
    mamber=models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.club_name
    
class ClubImages(BaseModel):
    club= models.ForeignKey(Club , related_name ="club_images" , on_delete=models.CASCADE )
    image= models.ImageField(upload_to='clubs/',null= False, default=  "images/no-image.jpg")
    
    
class  MemberShip(BaseModel):
    club= models.ForeignKey(Club , related_name ="club_memberships" , on_delete=models.CASCADE )
    user = models.ForeignKey(User, related_name="user" , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    mambership = models.CharField(max_length=255 , choices=(('Pre Paid' , 'Pre Paid'),('Post Paid' , 'Post Paid')))
    
