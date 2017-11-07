# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import usb_pcap_endpoint_number
class Usbmon(KaitaiStruct):
    """A native pcap header of [usbmon](https://www.kernel.org/doc/Documentation/usb/usbmon.txt) part of libpcap and Linux kernel.
    
    .. seealso::
       Source - https://github.com/the-tcpdump-group/libpcap/blob/ba0ef0353ed9f9f49a1edcfb49fefaf12dec54de/pcap/usb.h#L94
    
    
    .. seealso::
       Source - https://www.kernel.org/doc/Documentation/usb/usbmon.txt
    
    
    .. seealso::
       Source - https://www.kernel.org/doc/html/latest/driver-api/usb/URB.html
    
    
    .. seealso::
       Source - https://wiki.wireshark.org/USB
    """
    def __init__(self, header_size, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.header_size = header_size
        self._read()

    def _read(self):
        self._raw_header = self._io.read_bytes(self.header_size)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Usbmon.Header(_io__raw_header, self, self._root)
        self.data = self._io.read_bytes(self.header.data_size)

    class Timestamp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.seconds = self._io.read_s8le()
            self.microseconds = self._io.read_s4le()


    class Header(KaitaiStruct):

        class EventType(Enum):
            completion = 67
            error = 69
            submit = 83

        class TransferType(Enum):
            isochronous = 0
            interrupt = 1
            control = 2
            bulk = 3

        class SetupFlag(Enum):
            relevant = 0
            irrelevant = 45

        class DataFlag(Enum):
            urb = 0
            incoming = 60
            outgoing = 62
            error = 69
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.urb_id = self._io.read_u8le()
            self.event_type = KaitaiStream.resolve_enum(Usbmon.Header.EventType, self._io.read_u1())
            self.transfer_type = KaitaiStream.resolve_enum(Usbmon.Header.TransferType, self._io.read_u1())
            self.endpoint_number = usb_pcap_endpoint_number.UsbPcapEndpointNumber(self._io)
            self.device_address = self._io.read_u1()
            self.bus_id = self._io.read_u2le()
            self.setup_flag = KaitaiStream.resolve_enum(Usbmon.Header.SetupFlag, self._io.read_u1())
            self.data_flag = KaitaiStream.resolve_enum(Usbmon.Header.DataFlag, self._io.read_u1())
            self.timestamp = Usbmon.Timestamp(self._io, self, self._root)
            self.status = self._io.read_s4le()
            self.urb_size = self._io.read_s4le()
            self.data_size = self._io.read_s4le()
            if self.setup_flag == Usbmon.Header.SetupFlag.relevant:
                self.setup = Usbmon.Header.Setup(self._io, self, self._root)


        class Setup(KaitaiStruct):
            """
            .. seealso::
               Source - https://github.com/the-tcpdump-group/libpcap/blob/ba0ef0353ed9f9f49a1edcfb49fefaf12dec54de/pcap/usb.h#L118
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.s = self._io.read_bytes(8)
                self.interval = self._io.read_s4le()
                self.start_frame = self._io.read_s4le()
                self.copy_of_urb_transfer_flags = self._io.read_s4le()
                self.iso_descriptors_count = self._io.read_s4le()

            class PcapUsbSetup(KaitaiStruct):
                """USB setup header as defined in USB specification.
                Appears at the front of each Control S-type packet in DLT_USB captures.
                """
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.request_type = self._io.read_u1()
                    self.request = self._io.read_u1()
                    self.value = self._io.read_u2le()
                    self.index = self._io.read_u2le()
                    self.length = self._io.read_u2le()


            class IsoRec(KaitaiStruct):
                """Information from the URB for Isochronous transfers.
                
                .. seealso::
                   Source - https://github.com/the-tcpdump-group/libpcap/blob/ba0ef0353ed9f9f49a1edcfb49fefaf12dec54de/pcap/usb.h#L70
                """
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.error_count = self._io.read_s4le()
                    self.descriptors_count = self._io.read_s4le()





