from django.db import models

class StageEvent(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=45)
    organizer = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class StageEventShow(models.Model):
    stage_event = models.ForeignKey(StageEvent, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.stage_event.name

class TicketBooking(models.Model):
    stage_event = models.ForeignKey(StageEvent, on_delete=models.CASCADE)
    price = models.FloatField()
    customer = models.CharField(max_length=45)
    no_of_seats = models.IntegerField()

    def __str__(self):
        return self.customer

# commit




