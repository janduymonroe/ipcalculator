import math
from ipaddress import IPv4Network, IPv4Address, IPV4LENGTH

class_a = {'ip': '10.0.0.0/8', 'maxnet': 126, 'maxhost': 16777214, 'hostbits':8}
class_b = {'ip': '172.16.0.0/16', 'maxnet': 16382, 'maxhost': 65534, 'hostbits':16}
class_c = {'ip': '192.168.0.0/24', 'maxnet': 2097150, 'maxhost': 254, 'hostbits':24}


def netcalc(amount, netamount):
    total = amount * netamount
    if amount <= class_c['maxhost'] and total <= class_c['maxhost']:
        return class_c
    elif amount <= class_b['maxhost'] and total <= class_b['maxhost']:
        return class_b
    elif amount <= class_a['maxhost'] and total <= class_a['maxhost']:
        return class_a
    else:
        print("Quantity out of the possíble IP range.\n")
        __main__()


def cidrcalc(netamount, hostbits):
    cidr = round(math.log(netamount,2)) + hostbits
    return cidr



def subnetcalc(ip, cidr, netamount):
    net = IPv4Network(ip)
    subnet = net.subnets(new_prefix=cidr)
    subnetlist = [ip for ip in (map(IPv4Network, subnet))]
    broadcast = [ip.broadcast_address for ip in subnetlist]
    hosts = [ip for ip in subnetlist[0].hosts()]

    if len(subnetlist) < netamount:
      print("Subnets amount is impossible for hosts amount asked.\n")
      print("The calculation will be doing with the maximum subnets possible for the amount of hosts asked.")


    print(f"O IP escolhido foi {subnetlist[0]}.")
    print(f"A sua rede é composta de {len(subnetlist)} subredes com {len(hosts)} cada.")
    confirm(subnetlist, broadcast)

def confirm(subnetlist, broadcast):
    confirm = input("Do you need to print the subnets and its masks (y ou n)? ")
    if confirm == 'y':
        print("-"*60)
        print("Subnets and its masks list:")
        print("-"*60)
        for order, net in enumerate(subnetlist):
            print(f"{net}   to   {broadcast[order]}")
    elif confirm == 'n':
        print("\nEnd!")

    else:
        print("You must type 'y'(yes) ou 'n'(no).")
        confirm()


def __main__():
    amount = int(input("How many hosts will be used? "))
    netamount = int(input("How many nets will be needed? "))
    chose = netcalc(amount, netamount)
    ip = chose['ip']
    cidr = cidrcalc(netamount, chose['hostbits'])
    subnetcalc(ip, cidr, netamount)



if __name__ == '__main__':
    __main__()
