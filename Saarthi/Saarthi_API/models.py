from django.db import models
import uuid as user_id_generator


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30, unique=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.user_id

    class Meta:
        ordering = ['-created_at']
        db_table = 'users'

    def save(self, *args, **kwargs):
        print(self.created_at, 'self.created_at')
        print(self.updated_at, 'updated_at')
        if not self.created_at:
            self.user_id = self.first_name.lower() + str(user_id_generator.uuid1()).split('-')[0][:4]
        super().save(*args, **kwargs)


class ChatHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=300)
    reply = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.msg

    class Meta:
        ordering = ['updated_at']
        db_table = 'chathistory'
