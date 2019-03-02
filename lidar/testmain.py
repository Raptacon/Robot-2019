import sampleData
from Packetclass import Packet
from Lidarclass import Lidar
testP=Packet(sampleData.hardSteam)
testL=Lidar(testP)
testL.findDist()