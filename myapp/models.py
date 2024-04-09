import bcrypt
from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # For simplicity, store passwords as plaintext (not recommended for production)
    email = models.EmailField(unique=True)
    
    @staticmethod
    def hash_password(password):
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')  # Decode bytes to string for storage

    def set_password(self, password):
        # Hash the provided password and set it as the hashed_password field
        self.hashed_password = self.hash_password(password)

    def check_password(self, password):
        # Check if the provided password matches the hashed password
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8'))

    class Meta:
        app_label = ''  # Explicitly specify the app_label
        db_table = 'users' # specify the table name