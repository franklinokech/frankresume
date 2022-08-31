from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField(default=80)
    image = models.FileField(default='skills_default.jpg', upload_to='skills_images')
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    # Extending User Model Using a One-To-One Link


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_profile.jpg',
                               upload_to='profile_images',
                               blank=True,
                               null=True)
    title = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skill)
    bio = models.TextField()
    cv = models.FileField(upload_to='cv',
                          blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'


class ContactProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Messages')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ['timestamp']


class Testimonial(models.Model):
    thumbnail = models.ImageField(blank=True, null=True, upload_to='testimonial_images')
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    quote = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ['name']


class Media(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='media_uploads')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ['name']


class Portfolio(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    body = RichTextField()
    image = models.ImageField(upload_to='portfolio_images')
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'POrtfolio'
        ordering = ['name']


class Blog(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    body = RichTextField()
    image = models.ImageField(upload_to='blog_images')
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ['date']


class Certificate(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'
