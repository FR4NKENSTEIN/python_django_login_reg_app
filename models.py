from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    def registerValidator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #If any of these conditions are True create those key-value pairs in errors{}
        if len(postData['first_name_reg']) < 2:
            errors['first_name_reg'] = 'First name must be at least two(2) characters.'
        if len(postData['last_name_reg']) < 2:
            errors['last_name_reg'] = 'Last name must be at least two(2) characters.'
        if not EMAIL_REGEX.match(postData['email_reg']):
            errors['email_reg'] = "Invalid email address."
        if len(postData['password_reg']) < 8:
            errors['password_reg'] = 'Your password must be at least eight(8) characters.'
        if postData['confirm'] != postData['password_reg']:
            errors['confirm'] = 'Your password does not match.'
        return errors

    def loginValidator(self,postData):
        errors = {}
        #Find a user to validate
        user_in_db = User.objects.filter(email=postData['email_log'])#Could I use get() here? I really don't know which would be better.
        #If there are no matching users in the database throw an error
        if len(user_in_db) == 0:
            errors['email_log'] = "Invalid emial address."
        else:
            #Else there is a matching user
            this_user = user_in_db [0]
            #Check thier password matches
            if bcrypt.checkpw(postData['password_log'].encode(), this_user.pw_hash.encode()):
                print('passwords match')
            else:
                errors['password_log'] = 'Password does not match.'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f'User {self.id}: {self.first_name} {self.last_name}, {self.email}'
