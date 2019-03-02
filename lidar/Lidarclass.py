class Lidar(object):
    def __init__(self, packet):
        self.packet=packet
        self.packArr=self.packet.getValues()
        if self.packet.isFull()==False: #If the packet given is not a full 9 byte packet or is too long, find a full packet inside
            self.packArr=self.packet.getValues()
            x=0 #An index
            checksumin=0
            begin=0
            for i in self.packArr[:-1]:
                if i==89 and self.packArr[x+1]==89: #Look for the two indicators
                    checksumin=x+8
                    begin=x
                    tot = sum(self.packArr[begin:checksumin])
                    tot=(0x00FF & tot)
                    if checksumin<len(self.packArr) and tot==self.packArr[checksumin]:
                        self.packet.setValues(self.packArr[begin:checksumin]) #Set the packet's array as the (hopefully) correct 9 byte packet
                        self.packArr=self.packArr[begin:checksumin]
                        self.packet.setFull(True) #Say that the packet now contains a full 9 byte packet
                        break #break to avoid errors
                    elif checksumin>=len(self.packArr):
                        print('The index: '+str(checksumin)+' was out of range: '+str(len(self.packArr)-1))
                x+=1
            
            if(self.packet.isFull()==False):
                 print('I have failed to find a packet')
        if self.packet.isFull():
            strengthLow = self.packArr[2]
            strengthHigh = self.packArr[3]
            strength = strengthLow | (strengthHigh << 8)
            print('Dist: '+str(strength))
        else:
            print('The packet is not full, so I cannot find distance')