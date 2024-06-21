import psycopg2
from devices import Device, MobileDeviceBuilder
from database import DBConnect, PGMobileDevices


def get_devices_info(device: Device):

    db_connect = None
    try:
        db_connect = DBConnect.get_connect(dbname='shop',
                                           host='localhost',
                                           port=5432,
                                           user='postgres',
                                           password='postgres')
        PGMobileDevices.read(db_connect, device)
    except psycopg2.Error as e:
        print(e)
    finally:
        if db_connect:
            db_connect.close()


mobile_device = MobileDeviceBuilder()
mobile_device.create()
mobile_device.set_device_name('Iphone')
mobile_device.set_model('15 Pro')
current_device = mobile_device.get_device()

get_devices_info(current_device)
