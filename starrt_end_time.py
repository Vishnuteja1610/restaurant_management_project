from datetime import datetime, timedelta

class Reservation(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @classmethod
    def find_available_slots(cls, start_range, end_range,slot_duration_minutes==30):
        existing_reservations = cls.objects.filter(
            start_time__lt=end_range,
            end_time__gt=start_range
        ).order_by('start_time')

        available_slots=[]
        current_start=start_range
        