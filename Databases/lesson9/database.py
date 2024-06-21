from abc import ABC, abstractmethod
from devices import Device, MobileDevice, MobileDevicesContainer
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
        # Вызвать запрос вставки данных из объекта
        ...

    @staticmethod
    def read(connect, device: Device) -> list[Device]:

        try:
            with connect.cursor() as cursor:

                params = (device.get_device_name(), device.get_model())
                query = """SELECT * 
                           FROM mobile_devices
                           WHERE device_name = %s AND model = %s"""
                cursor.execute(query, params)
                data = cursor.fetchall()

                if data:
                    container = MobileDevicesContainer()
                    container.create_list_devices(data)
                    return container.get_list_devices()
                else:
                    raise Exception(f"Не найдена запись с параметрами {params}")
        except (Exception, psycopg2.Error) as e:
            print(e)

    @staticmethod
    def update(connect, index_old_device: int, new_device: MobileDevice):

        try:
            with connect.cursor() as cursor:
                params = (new_device.device_os, new_device.device_name,
                          new_device.model, new_device.memory,
                          new_device.price, new_device.release_date,
                          new_device.counter, index_old_device)
                query = """ UPDATE mobile_devices
                            SET 
                                device_os = %s,
                                device_name = %s,
                                model = %s,
                                memory = %s,
                                price = %s,
                                release_date = %s,
                                counter = %s
                            WHERE mobile_device_id = %s; """
                cursor.execute(query, params)
        except (Exception, psycopg2.Error) as e:
            print(e)

    @staticmethod
    def delete(connect, device: Device):
        # Найти индекс девайса и удалить его
        ...

