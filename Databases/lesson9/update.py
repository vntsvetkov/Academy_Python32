import psycopg2
from devices import Device, MobileDevice, MobileDeviceBuilder
from database import DBConnect, PGMobileDevices


def update_records(old_device: MobileDevice, new_device: MobileDevice):
    """Поменять одну запись на другую"""
    db_connect = None
    try:
        db_connect = DBConnect.get_connect(dbname='shop',
                                           host='localhost',
                                           port=5432,
                                           user='postgres',
                                           password='postgres')

        cursor = db_connect.cursor()
        params = (old_device.device_os, old_device.device_name,
                  old_device.model, old_device.memory,
                  old_device.price, old_device.release_date)
        query = """ SELECT mobile_device_id
                    FROM mobile_devices
                    WHERE device_os = %s AND
                          device_name = %s AND
                          model = %s AND
                          memory = %s AND
                          price = %s AND
                          release_date = %s;
                    """
        cursor.execute(query, params)
        data = cursor.fetchall()

        PGMobileDevices.update(db_connect, data[0][0], new_device)
        db_connect.commit()
        cursor.close()

    except psycopg2.Error as e:
        print(e)
    finally:
        if db_connect:
            db_connect.close()


if __name__ == "__main__":

    # Состояние до нажатия редактирования
    device_1 = MobileDeviceBuilder()
    device_1.create()
    device_1.set_device_os("IOS")
    device_1.set_device_name("IPhone")
    device_1.set_model("15 Pro")
    device_1.set_memory(256)
    device_1.set_price(130000.00)
    device_1.set_release_date("2023-07-05")
    device_1.set_counter(1)
    a = device_1.get_device()

    # Состояние после сохранения редактирования
    device_2 = MobileDeviceBuilder()
    device_2.create()
    device_2.set_device_os("IOS")
    device_2.set_device_name("IPhone")
    device_2.set_model("15 Pro")
    device_2.set_memory(256)
    device_2.set_price(117000.00)
    device_2.set_release_date("2023-07-05")
    device_2.set_counter(1)
    b = device_2.get_device()

    update_records(a, b)
