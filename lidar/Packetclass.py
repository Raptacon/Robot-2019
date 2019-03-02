from sampleData import easyPacket
class Packet(object):
	def __init__(self, arr=easyPacket):
		self.packet=arr
		self.full=False
	def isFull(self): #If this is a correctly sized packet, return true. Most likely it is not.
		return self.full
	def setFull(self,fulld):
		self.full=fulld
	def getValues(self):
		return self.packet
	def setValues(self,pack):
		self.packet=pack