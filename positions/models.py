from django.db import models

class Position(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Position: {self.name}"

class PositionRequiredWhen(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"PositionRequiredWhen: {self.name}"

class PositionImage(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    description = models.CharField( max_length=100)
    image = models.ImageField(upload_to='positions/images/')

    def __str__(self):
        return f"PositionImage: {self.position.name}: {self.description}"
