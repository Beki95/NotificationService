from decouple import config
from typing import Dict, List
import requests
from requests.exceptions import ConnectTimeout

from clients.models import Client
from notifications.models import Notification, SendingMessages
from notifications.settings import ChoiceFilter


class Mailing:

    token = config('TOKEN')
    url = config('URL')

    @classmethod
    def get_headers(cls) -> Dict:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {cls.token}',
        }
        return headers

    @classmethod
    def _get_clients(cls, filter_by) -> List[Client]:
        _filter = {}
        if filter_by == ChoiceFilter.TAG:
            _filter['tag__isnull'] = False
        elif filter_by == ChoiceFilter.CODE:
            _filter['mobile_code__isnull'] = False
        clients = Client.objects.filter(**_filter)
        return clients

    @classmethod
    def save_notifications(cls, _list: List[Notification]) -> None:
        Notification.objects.bulk_create(_list)

    # отправка запроса на сторонний сервис
    @classmethod
    def request(cls, pk: int) -> None:
        obj = SendingMessages.objects.get(id=pk)
        headers = cls.get_headers()
        clients = cls._get_clients(obj.choice_filter)
        notifications_list = []
        for i in clients:

            notification_data = {'sending_message': obj,
                                 'client': i}
            data = {'id': 1,  # по умолчанию id=1 по другому сервис не работает
                    'phone': f'+{i.phone.country_code}'
                             f'{i.phone.national_number}',
                    'text': obj.text}
            try:
                response = requests.post(cls.url,
                                         json=data,
                                         headers=headers,
                                         timeout=10)

                if response.status_code == 400:  # 'Error on the client side'
                    notification_data['status'] = False
                elif response.status_code == 429:  # 'Too many requests'
                    notification_data['status'] = False
            except ConnectTimeout:  # {'error': 'ConnectTimeout'}
                notification_data['status'] = False
            else:
                notification_data['status'] = True
                notification = Notification(**notification_data)
                notifications_list.append(notification)
        cls.save_notifications(notifications_list)
