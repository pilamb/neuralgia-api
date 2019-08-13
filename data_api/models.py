from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

AREAS_CHOICES = (
    ('Left', (
        ('VL1', 'Eye/high area, left.'),
        ('VL2', 'Nose,/medium area, left.'),
        ('VL3', 'Mandibular, left.')
        )
    ),
    ('Right', (
        ('VR1', 'Eye/high area, right.'),
        ('VR2', 'Nose,/medium area, right.'),
        ('VR3', 'Mandibular, right.'),
        )
    ),
    ('---', '---'),
)


class Hit(models.Model):
    """
    Represents a moment of neurological pain.
    The target is to be able to trace it with enriched data.
    """
    created = models.DateTimeField(auto_now_add=True)
    triggered_by = models.CharField(max_length=100, blank=True, default='')
    area = models.CharField(
        max_length=3,
        choices=AREAS_CHOICES
    )
    note = models.CharField(max_length=1000, default='')
    rank = models.IntegerField(default=1,
                               validators=[MinValueValidator(1),
                                           MaxValueValidator(10)]
                               )
    meds = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='pains',
                              on_delete=models.CASCADE)
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return " %s had a pain ranked with %s on area %s triggered" \
               " by %s at %s"% (self.owner, self.rank, self.area,
                                            self.triggered_by, self.created)
