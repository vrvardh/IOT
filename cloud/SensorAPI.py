from mbed_cloud import ConnectAPI
from DB_Connect_Util import update_db, sendNotification

SENSOR_VALUES_PATH = "/3000/0/1"

def getSensorValues():
        api = ConnectAPI()
        # calling start_notifications is required for getting/setting resource synchronously
        api.start_notifications()
        devices = api.list_connected_devices().data
        if not devices:
            raise Exception("No connected devices registered. Aborting")
        while True:
            # Synchronously get the initial/current value of the resource
            accel_gyro = api.get_resource_value(devices[0].id, SENSOR_VALUES_PATH)
            print(accel_gyro)
            update_db(accel_gyro)

if __name__ == "__main__":
 getSensorValues()
