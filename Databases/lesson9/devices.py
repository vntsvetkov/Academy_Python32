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

    def create_list_devices(self, data: list) -> None:

        for record in data:
            device = MobileDeviceBuilder()
            device.create()
            device.set_device_os(record[0])
            device.set_device_name(record[1])
            device.set_model(record[2])
            device.set_memory(record[3])
            device.set_price(record[4])
            device.set_release_date(record[5])
            device.set_counter(record[6])
            self._devices.append(device.get_device())
            del device

    def add_device(self, device: Device):
        self._devices.append(device)

    def get_list_devices(self):
        return self._devices

