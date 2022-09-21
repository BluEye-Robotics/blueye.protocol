from .v2.tcp_protocol_class import TcpClient  # noqa F401
from .v2.udp_client import UdpClient  # noqa F401
from .v2.udp_protocol_dict import (  # noqa F401
    _generator_hash,
    _json_hash,
    protocol_data,
)
from .v2.udp_protocol_parser import AppProtocol  # noqa F401
from .v3 import *  # noqa F401
from .v3 import (
    BatteryBq40Z50,
    BatteryBq40Z50Tel,
    CpuTemperature,
    CpuTemperatureTel,
    PilotGpsPositionCtrl,
    PilotGpsPositionTel,
)


# The following definitions are needed to circumvent an issue with how
# betterproto "pythonizes" the names of classes.
class PilotGPSPositionCtrl(PilotGpsPositionCtrl):
    pass


class PilotGPSPositionTel(PilotGpsPositionTel):
    pass


class BatteryBQ40Z50(BatteryBq40Z50):
    pass


class BatteryBQ40Z50Tel(BatteryBq40Z50Tel):
    pass


class CPUTemperature(CpuTemperature):
    pass


class CPUTemperatureTel(CpuTemperatureTel):
    pass
