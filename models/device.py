from models.device_type import DeviceType

class Device():
    def __init__(self, ip: str, name: str, type: DeviceType, last_seen: int):
        self.ip = ip
        self.name = name
        self.type = DeviceType(type)
        self.last_seen = last_seen
    
    def __str__(self):
        return 'Device %s (%s) last seen %s' % (self.ip, self.name, self.last_seen)