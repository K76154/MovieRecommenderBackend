from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from MovieRecommenderBackend.apps.URLDispatcher.choices import GENDER_CHOICES


class MyUserManager(BaseUserManager):
    def create_user(self, email, age, gender, password=None):
        """
        Creates and saves a User with the given email, age, gender and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            age=age,
            gender=gender
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, age, gender, password):
        """
        Creates and saves a superuser with the given email, age, gender and password.
        """
        user = self.create_user(
            email,
            password=password,
            age=age,
            gender=gender,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class RatingUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['user_id']


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    ratingUser = models.OneToOneField(RatingUser, primary_key=True)
    age = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(999), MinValueValidator(0)])
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['age', 'gender']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=11)
    link = models.URLField()
    average_rating = models.FloatField()

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['-average_rating']


class RatingData(models.Model):
    user = models.ForeignKey(RatingUser)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(null=False, blank=False)
    timestamp = models.BigIntegerField(null=True, blank=False)

    class Meta:
        verbose_name = 'Rating Data'
        verbose_name_plural = 'Rating Data'

