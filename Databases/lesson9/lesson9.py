import psycopg2

from abc import ABC, abstractmethod
from datetime import date


class DBConnect:

    _instance = None

    @classmethod
    def get_connect(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = psycopg2.connect(*args, **kwargs)
        return cls._instance

    @classmethod
    def close(cls):
        cls._instance.close()


class Device(ABC):
    ...


class MobileDevice(Device):

    def __init__(self, device_os: str,
                 device_name: str,
                 model: str,
                 memory: int,
                 price: float,
                 release_date: date,
                 counter: int):
        self._device_os = device_os
        self.device_name = device_name
        self.model = model
        self._memory = memory
        self._price = price
        self._release_date = release_date
        self._counter = counter


class MobileDevicesContainer:

    def __init__(self):
        self._devices: list[Device] = []

    @classmethod
    def create_list_devices(cls, data: list[tuple]):
        # перезаписывает data в self._devices
        ...

    def get_list_devices(self):
        return self._devices

class DBManager(ABC):

    @staticmethod
    @abstractmethod
    def create(connect, device: Device):
        ...

    @staticmethod
    @abstractmethod
    def read(connect, device: Device):
        ...

    @staticmethod
    @abstractmethod
    def update(connect, old_device: Device, new_device: Device):
        ...

    @staticmethod
    @abstractmethod
    def delete(connect, device: Device):
        ...


class PGMobileDevices(DBManager):

    @staticmethod
    def create(connect, device: Device):
        ...

    @staticmethod
    def read(connect, device: Device) -> list[Device]:
        with connect.cursor() as cursor:

            params = (device.device_name, device.model)
            query = """SELECT * 
                       FROM mobile_devices
                       WHERE device_name = %s AND model = %s"""
            cursor.execute(query, params)
            data = cursor.fetchall()
            if len(data) > 0:
                # Преобразовать список кортежей в список Device
                result: list[Device] = get_list_devices()
                return result
            else:
                # Бросить исключение "Не найдена запись по параметрам"
                pass

    @staticmethod
    def update(connect, old_device: Device, new_device: Device):
        ...

    @staticmethod
    def delete(connect, device: Device):
        ...


db_connect = None
try:
    db_connect = DBConnect.get_connect(dbname='shop',
                                       host='localhost',
                                       port=5432,
                                       user='postgres',
                                       password='postgres')
except psycopg2.Error as e:
    print(e)
else:

    mobile_device = MobileDevice(device_os='IOS',
                                 device_name='Iphone',
                                 model='15 Pro',
                                 memory=256,
                                 price=130000,
                                 release_date=date(2023, 7, 5),
                                 counter=1)
    PGMobileDevices.read(db_connect, mobile_device)
finally:
    if db_connect:
        db_connect.close()