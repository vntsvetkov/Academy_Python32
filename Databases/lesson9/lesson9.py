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
        devices = PGMobileDevices.read(db_connect, device)
        for d in devices:
            print(d)
    except psycopg2.Error as e:
        print(e)
    finally:
        if db_connect:
            db_connect.close()


if __name__ == "__main__":
    mobile_device = MobileDeviceBuilder()
    mobile_device.create()
    mobile_device.set_device_name('IPhone')
    mobile_device.set_model('15 Pro')
    current_device = mobile_device.get_device()

    get_devices_info(current_device)
