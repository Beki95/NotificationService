from django_q.models import Schedule
from typing import Dict

from .models import SendingMessages


class ScheduledTask:

    def __init__(self, obj_id: int) -> None:
        self.obj_id = obj_id

    def get_data(self) -> Dict:
        obj = SendingMessages.objects.filter(id=self.obj_id).first()
        return {
            'text': obj.text,
            'filter_by': obj.choice_filter,
            'obj': obj
        }

    def create_scheduled_task(self):
        obj = self.get_data()
        schedule = Schedule(
            name='mailing',
            args=f"{obj['obj'].id}",
            func='notifications.services.Mailing.request',
            schedule_type=Schedule.ONCE,
            minutes=1,
            repeats=1,
            next_run=obj['obj'].start_date,
        )
        schedule.save()
