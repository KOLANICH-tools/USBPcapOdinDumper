import re

from RichConsole import groups, rsjoin

from .Dumping import Dumping
from .kaitai.odin3 import *


class OdinDumping(Dumping):
	def isUseful(self, packet):
		return packet.meta.transfer_type.name == "bulk" or len(packet.body) >= 1024 or packet.body == b"ODIN" or packet.body == b"LOKE"

	def transformPacket(self, pckt):
		return pckt

	invalidEnumRx = re.compile("^(.+) is not a valid (.+)$")

	def generateName(self, pckt):
		if pckt.body == b"ODIN" or pckt.body == b"LOKE":
			pckt.name = rsjoin("_", (pckt.name, str(pckt.body, encoding="ascii")))
		else:
			errorName = None
			try:
				o = Odin3.from_bytes(pckt.body)
				pckt.name = rsjoin("_", (pckt.name, o.type.name))
				if hasattr(o.content, "request"):
					pckt.name = rsjoin("_", (pckt.name, groups.Fore.green(str(o.content.request))))
			except ValueError as error:
				errorName = "ENUM"
				m = __class__.invalidEnumRx.match(error.args[0])
				if m:
					(num, name) = m.groups()
					try:
						num = hex(int(num))
					except BaseException:
						pass
					errorName = rsjoin("_", (errorName, groups.Fore.lightblueEx(name), groups.Fore.cyan(num)))
			except Exception as error:
				errorName = ""
			if errorName is not None:
				pckt.name = rsjoin("_", (pckt.name, groups.Fore.red(rsjoin("_", ("ERROR_ODIN3", errorName)))))
		return pckt
