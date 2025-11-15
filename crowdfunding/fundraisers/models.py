from django.db import models
from django.contrib.auth import get_user_model

class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_fundraisers'
    )


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser',
        on_delete=models.CASCADE,
        related_name = 'pledges'
    ) 

    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )

# Get a pledge from the database
#some_pledge = Pledge.objects.get(pk=1)

# Now we can grab the fundraiser from our foreignkey field
#some_fundraiser = some_pledge.fundraiser

# Get a fundraiser from the database
#some_fundraiser = Fundraiser.objects.get(pk=1)

# Now we can grab te list of pledges from our related_name property
#associated_pledges = some_fundraiser.pledges


