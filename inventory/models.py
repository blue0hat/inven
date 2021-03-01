from django.db import models

class Part(models.Model):

    typechoices = (
        ('MB', 'MB'),
        ('FHD', 'FHD'),
        ('KYBD', 'KYBD'),
        ('SSD', 'SSD'),
        ('ELSE', 'ELSE')
    )
    statuschoices = (
        ('NEW', 'New'),
        ('USED', 'Used'),
        ('SENT', 'Sent')

    )

    type = models.CharField(max_length=200, choices=typechoices)
    part = models.CharField(max_length=255)
    partnum = models.CharField(max_length=255, null=True)
    partid = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=statuschoices, default='NEW')
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Type: {0} | {1}'.format(self.type, self.part)