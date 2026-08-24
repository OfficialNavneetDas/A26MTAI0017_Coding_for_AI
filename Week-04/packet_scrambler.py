def packet_validater(packet):
    if packet and len(packet)>=10:
        print("Validation passed. processing packet...")
    else:
        print("Validation failed: packet is empty or to short")
        raise ValueError("packet is empty")

def middleout_swap(packet):
    midpoint = len(packet)//2
    front_half = packet[:midpoint]
    back_half = packet[midpoint:]
    scrambled = back_half[::-1]+front_half
    print(scrambled)
    return scrambled

def Sync_bit(packet):
    midpoint = len(packet)//2
    if type(packet[midpoint]) is int:
        packet.insert(midpoint+1,"SYNC-BIT")
    
def zero_removal(scrambled):
    while 0 in scrambled:
        scrambled.remove(0)
#======================Root code=================================
packet = [0,45,67,8,23,43,68,24,0,56,22,13,90,0]
packet_validater(packet)
scrambled = middleout_swap(packet)
print(id(packet) == id(scrambled)) #expect :False

Sync_bit(scrambled)
print(scrambled)

zero_removal(scrambled)
print(f"packet: {packet}")
print(f"scrambled: {scrambled}")

# Constraint
first, *middle , last = scrambled
print(f"Header: {first} Footer: {last} body length:{len(middle)}")
