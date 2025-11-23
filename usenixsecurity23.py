from scapy.all import rdpcap, TCP

pcapng=rdpcap('/.pcapng')
datalist=[]
for p in pcapng:
    if TCP in p and p[TCP].flags & 0x08:
        if p[TCP].payload:
            datalist.append(p[TCP].payload.load)

def popcount(pkt):
    return sum(bin(b).count('1') for b in pkt)
def ex1(pkt):
    count = popcount(pkt)
    length = len(pkt)
    ratio = count / length
    return (ratio<=3.4 or ratio>=4.6)
def ex2(pkt):
    return all(0x20<=b<=0x7e for b in pkt[:6])
def ex3(pkt):
    return sum(1 for b in pkt if 0x20<=b<=0x7e)>(len(pkt)/2)
def ex4(pkt):
    return any(
        sum(1 for b in pkt[k:k+20] if 0x20<=b<=0x7e)>20
        for k in range(len(pkt)-20)
        )

if __name__=="__main__":
    for data in datalist:
        if ex1(data):
            print('Ex1!')
        if ex2(data):
            print('Ex2!')
        if ex3(data):
            print('Ex3!')
        if ex4(data):
            print('Ex4!')

