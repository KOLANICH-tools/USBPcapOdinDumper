# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Odin3(KaitaiStruct):
    """[Samsung Odin](https://en.wikipedia.org/wiki/Odin_(firmware_flashing_software)) is a proprietary piece of software developed by Samsung and used to flash firmware into Samsung devices. Odin utility has a Loke counterpart in the device bootloader. This ksy documents the message format of the protocol they talk to each other.
    The protocol was reverse engineered by Benjamin Dobell who have created a MIT-licensed utility Heimdall, on which source code this ksy is based.
    If you wanna test and augment this spec keep in mind that a lot of websites spreading leaked versions of Odin utility were created with the sole purpose of spreading malware glued with the tool. The most trustworthy website I know is the one belonging to chainfire, a well-known dev on Android scene.
    
    .. seealso::
       Source - https://gitlab.com/BenjaminDobell/Heimdall/tree/master/heimdall/source
    """

    class ChipType(Enum):
        ram = 0
        nand = 1

    class TrRequest(Enum):
        flash = 0
        dump = 1
        part = 2
        end = 3
        unknown2000 = 8192

    class Destination(Enum):
        phone = 0
        modem = 1

    class PacketType(Enum):
        send_file_part = 0
        session = 100
        pit_file = 101
        file_transfer = 102
        end_session = 103
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.type = KaitaiStream.resolve_enum(Odin3.PacketType, self._io.read_u4le())
        _on = self.type
        if _on == Odin3.PacketType.end_session:
            self._raw_content = self._io.read_bytes_full()
            _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
            self.content = Odin3.EndSession(_io__raw_content, self, self._root)
        elif _on == Odin3.PacketType.session:
            self._raw_content = self._io.read_bytes_full()
            _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
            self.content = Odin3.Session(_io__raw_content, self, self._root)
        elif _on == Odin3.PacketType.file_transfer:
            self._raw_content = self._io.read_bytes_full()
            _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
            self.content = Odin3.FileTransfer(_io__raw_content, self, self._root)
        elif _on == Odin3.PacketType.pit_file:
            self._raw_content = self._io.read_bytes_full()
            _io__raw_content = KaitaiStream(BytesIO(self._raw_content))
            self.content = Odin3.PitFile(_io__raw_content, self, self._root)
        else:
            self.content = self._io.read_bytes_full()

    class EndSession(KaitaiStruct):

        class Request(Enum):
            end_session = 0
            reboot_device = 1
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request = KaitaiStream.resolve_enum(Odin3.EndSession.Request, self._io.read_u4le())


    class FileTransfer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request = KaitaiStream.resolve_enum(Odin3.TrRequest, self._io.read_u4le())
            _on = self.request
            if _on == Odin3.TrRequest.flash:
                self.content = Odin3.FileTransfer.Flash(self._io, self, self._root)
            elif _on == Odin3.TrRequest.dump:
                self.content = Odin3.FileTransfer.Dump(self._io, self, self._root)
            elif _on == Odin3.TrRequest.part:
                self.content = Odin3.FileTransfer.Part(self._io, self, self._root)
            elif _on == Odin3.TrRequest.end:
                self.content = Odin3.FileTransfer.End(self._io, self, self._root)

        class Flash(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.sequence_byte_count = self._io.read_u4le()


        class Part(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.sequence_byte_count = self._io.read_u4le()
                self.part_index = self._io.read_u4le()


        class Dump(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.chip_type = KaitaiStream.resolve_enum(Odin3.ChipType, self._io.read_u4le())
                self.chip_id = self._io.read_u4le()


        class End(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.destination = KaitaiStream.resolve_enum(Odin3.Destination, self._io.read_u4le())
                self.sequence_byte_count = self._io.read_u4le()
                self.unknown1 = self._io.read_u4le()
                self.device_type = self._io.read_u4le()
                _on = self.destination
                if _on == Odin3.Destination.phone:
                    self.content = Odin3.FileTransfer.End.Phone(self._io, self, self._root)
                self.end_of_file = self._io.read_u4le()

            class Phone(KaitaiStruct):

                class File(Enum):
                    primary_bootloader = 0
                    pit = 1
                    secondary_bootloader = 3
                    secondary_bootloader_backup = 4
                    kernel = 6
                    recovery = 7
                    tablet_modem = 8
                    modem = 11
                    unknown12 = 18
                    efs = 20
                    param_lfs = 21
                    factory_file_system = 22
                    database_data = 23
                    cache = 24
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self.file_identifier = KaitaiStream.resolve_enum(Odin3.FileTransfer.End.Phone.File, self._io.read_u4le())




    class PitFile(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request = KaitaiStream.resolve_enum(Odin3.TrRequest, self._io.read_u4le())
            _on = self.request
            if _on == Odin3.TrRequest.flash:
                self.content = Odin3.PitFile.Flash(self._io, self, self._root)
            elif _on == Odin3.TrRequest.part:
                self.content = Odin3.PitFile.Part(self._io, self, self._root)
            elif _on == Odin3.TrRequest.end:
                self.content = Odin3.PitFile.End(self._io, self, self._root)

        class Flash(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.part_size = self._io.read_u4le()


        class Part(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.part_index = self._io.read_u4le()


        class End(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.file_size = self._io.read_u4le()



    class Session(KaitaiStruct):

        class Request(Enum):
            begin_session = 0
            device_type = 1
            total_bytes = 2
            enable_some_sort_of_flag = 3
            file_part_size = 5
            enable_tflash = 8
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request = KaitaiStream.resolve_enum(Odin3.Session.Request, self._io.read_u4le())
            _on = self.request
            if _on == Odin3.Session.Request.total_bytes:
                self.content = Odin3.Session.TotalBytes(self._io, self, self._root)
            elif _on == Odin3.Session.Request.file_part_size:
                self.content = Odin3.Session.FilePartSize(self._io, self, self._root)

        class FilePartSize(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.file_part_size = self._io.read_u4le()


        class TotalBytes(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.total_bytes = self._io.read_u4le()



    @property
    def odin_handshake_message(self):
        if hasattr(self, '_m_odin_handshake_message'):
            return self._m_odin_handshake_message if hasattr(self, '_m_odin_handshake_message') else None

        self._m_odin_handshake_message = self._io.read_bytes(5)
        return self._m_odin_handshake_message if hasattr(self, '_m_odin_handshake_message') else None

    @property
    def loke_handshake_message(self):
        if hasattr(self, '_m_loke_handshake_message'):
            return self._m_loke_handshake_message if hasattr(self, '_m_loke_handshake_message') else None

        self._m_loke_handshake_message = self._io.read_bytes(4)
        return self._m_loke_handshake_message if hasattr(self, '_m_loke_handshake_message') else None


