
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):

    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    name    = models.CharField(max_length=100, null=True)
    avatar  = models.ImageField(upload_to='profile/%Y/%m/%d/', default='profile/default.png')
    #bio     = models.CharField(max_length=200)
    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            new_img = (450, 450)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    def __str__(self):
        if self.name is None:
            return 'None'
        else:
            return self.name
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

class About(models.Model):

    title           = models.CharField(max_length=50, unique=True, default='About')
    qaot_1          = models.TextField()
    sub_title       = models.CharField(max_length=200)
    sub_qaot        = models.TextField()
    qaot_2          = models.TextField()
    birthday        = models.DateField()
    age             = models.IntegerField()
    website         = models.URLField()
    DEG_OPT         = [('Master','Master'),]
    degree          = models.CharField(max_length=50, choices=DEG_OPT)
    phone           = models.CharField(max_length=20)
    email           = models.EmailField()
    city            = models.CharField(max_length=100)
    location        = models.TextField()
    freelance       = models.CharField(max_length=50, default='Available')
    is_chosen       = models.BooleanField(default=False, unique=True)
    twitter_id      = models.CharField(max_length=30, default="#")
    facebook_id     = models.CharField(max_length=30, default="#")
    instagram_id    = models.CharField(max_length=30, default="#")
    skype_id        = models.CharField(max_length=30, default="#")
    linkedin_id     = models.CharField(max_length=30, default="#")
    def __str__(self):
        return self.title
 
class Skill(models.Model):

    title           = models.CharField(max_length=50, unique=True)
    skill_level   = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Resume(models.Model):
    title           = models.CharField(max_length=100)
    items           = models.ManyToManyField('Resume_item', blank=True)
    def __str__(self):
        return self.title
    
class Resume_item(models.Model):
    title           = models.CharField(max_length=100)
    text            = models.TextField(blank=True,null=True)
    year            = models.CharField(max_length=50, blank=True)
    institution     = models.CharField(max_length=150, blank=True)
    break_point     = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Certification(models.Model):
    title               = models.CharField(max_length=150)
    caption             = models.TextField(blank=True)
    image               = models.ImageField(upload_to='certs/%Y/%m/%d/', blank=True)
    institution         = models.CharField(max_length=150, blank=True)
    institution_logo    = models.ImageField(upload_to='certs/%Y/%m/%d/', blank=True)
    verification_link   = models.CharField(max_length=250, default='#')

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 400:
            new_img = (200, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)
        img = Image.open(self.institution_logo.path)
        if img.height > 200 or img.width > 200:
            new_img = (150, 150)
            img.thumbnail(new_img)
            img.save(self.institution_logo.path)

    def __str__(self):
        return self.title
    
class Main(models.Model):
    title           = models.CharField(max_length=100)
    background_image= models.ImageField(upload_to='background/%Y/%m/%d/')
    fixed_text      = models.TextField(default="I'm", blank=True)
    typing_text     = models.TextField(default='Data scientist, Web Developer, Freelancer', blank=True)
    is_chosen       = models.BooleanField(default=False, unique=True)
    
    def __str__(self):
        return self.title
