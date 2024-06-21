from abc import ABC, abstractmethod
from devices import Device, MobileDevicesContainer
import psycopg2


class DBConnect:

    _instance = None

    @classmethod
    def get_connect(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = psycopg2.connect(*args, **kwargs)
        return cls._instance


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

        try:
            with connect.cursor() as cursor:

                params = (device.get_device_name, device.get_model)
                query = """SELECT * 
                           FROM mobile_devices
                           WHERE device_name = %s AND model = %s"""
                cursor.execute(query, params)
                data = cursor.fetchall()
                if data:
                    result: list[Device] = MobileDevicesContainer.get_list_devices(data)
                    return result
                else:
                    raise Exception(f"Не найдена запись с параметрами {params}")
        except (Exception, psycopg2.Error) as e:
            print(e)

    @staticmethod
    def update(connect, old_device: Device, new_device: Device):
        ...

    @staticmethod
    def delete(connect, device: Device):
        ...

