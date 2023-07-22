from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100, null=True)
    avatar      = models.ImageField(upload_to='profile/%Y/%m/%d/', default='profile/default.png')
    is_chosen   = models.BooleanField(default=True, unique=True)
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
    DEG_OPT         = [('PhD','PhD'),('Master','Master'),('Bachelor\'s','Bachelor\'s')]
    degree          = models.CharField(max_length=50, choices=DEG_OPT)
    phone           = models.CharField(max_length=20)
    email           = models.EmailField()
    city            = models.CharField(max_length=100)
    location        = models.TextField()
    geo_location    = models.CharField(max_length=150, default='32.7177373,51.5233033')
    freelance       = models.CharField(max_length=50, default='Available')
    twitter_id      = models.CharField(max_length=30, default="#")
    facebook_id     = models.CharField(max_length=30, default="#")
    instagram_id    = models.CharField(max_length=30, default="#")
    skype_id        = models.CharField(max_length=30, default="#")
    linkedin_id     = models.CharField(max_length=30, default="#")
    profile_image   = models.ImageField(upload_to='profile/%Y/%m/%d/', default='profile/default.png')
    is_chosen       = models.BooleanField(default=False, unique=True)
    #bio     = models.CharField(max_length=200)
    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width > 300:
            new_img = (450, 450)
            img.thumbnail(new_img)
            img.save(self.profile_image.path)

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
    site_name       = models.CharField(max_length=100, default='mysite.ir')
    designed_by     = models.CharField(max_length=100, default='Alibaghban.ir')
    designed_by_link= models.CharField(max_length=100, default='https://alibaghban.ir')
    background_image= models.ImageField(upload_to='background/%Y/%m/%d/')
    fixed_text      = models.TextField(default="I'm", blank=True)
    typing_text     = models.TextField(default='Data scientist, Web Developer, Freelancer', blank=True)
    favicon         = models.ImageField(upload_to='background/%Y/%m/%d/', blank=True)
    favicon_apple   = models.ImageField(upload_to='background/%Y/%m/%d/', blank=True)
    is_chosen       = models.BooleanField(default=False, unique=True)
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.favicon.path)
        if img.height > 33 or img.width > 33:
            new_img = (32, 32)
            img.thumbnail(new_img)
            img.save(self.favicon.path)
        img = Image.open(self.favicon_apple.path)
        if img.height > 181 or img.width > 181:
            new_img = (180, 180)
            img.thumbnail(new_img)
            img.save(self.favicon_apple.path)
    def __str__(self):
        return self.title
