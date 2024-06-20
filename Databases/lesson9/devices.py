from datetime import date
from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def get_device_name(self):
        ...

    @abstractmethod
    def get_model(self):
        ...


class MobileDevice(Device):

    def __init__(self):
        self.device_os = None
        self.device_name = None
        self.model = None
        self.memory = None
        self.price = None
        self.release_date = None
        self.counter = None

    def get_device_name(self):
        return self.device_name

    def get_model(self):
        return self.model


class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_device_os(self, device_os):
        ...

    @abstractmethod
    def set_device_name(self, device_name):
        ...

    @abstractmethod
    def set_model(self, model):
        ...

    @abstractmethod
    def set_memory(self, memory):
        ...

    @abstractmethod
    def set_price(self, price):
        ...

    @abstractmethod
    def set_release_date(self, release_date):
        ...

    @abstractmethod
    def set_counter(self, counter):
        ...

    @abstractmethod
    def get_device(self):
        ...


class MobileDeviceBuilder(Builder):

    _device: MobileDevice

    def create(self):
        self._device = MobileDevice()

    def set_device_os(self, device_os):
        self._device.device_os = device_os

    def set_device_name(self, device_name):
        self._device.device_name = device_name

    def set_model(self, model):
        self._device.model = model

    def set_price(self, price):
        self._device.price = price

    def set_memory(self, memory):
        self._device.memory = memory

    def set_counter(self, counter):
        self._device.counter = counter

    def set_release_date(self, release_date):
        self._device.release_date = release_date

    def get_device(self):
        return self._device


class MobileDevicesContainer:

    def __init__(self):
        self._devices: list[Device] = []

    @classmethod
    def create_list_devices(cls, data: list) -> list[Device]:
        # перезаписывает data (список кортежей) в self._devices (список объектов Device)
        ...

    def add_device(self, device: Device):
        self._devices.append(device)

    def get_list_devices(self):
        return self._devices

