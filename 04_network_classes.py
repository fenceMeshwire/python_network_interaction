#!/usr/bin/env python3

# Python 3.9.5

# network_classes.py

# CLASS A
class_a = [a for a in range(1, 127 ,1)] # 0 and 127 are excluded
bin_class_a = [bin(a) for a in range(1, 127, 1)]
bin_class_a[0], bin_class_a[-1] # 00000001 to 01111110'

# CLASS B
class_b = [b for b in range(128, 192, 1)] # 128 - 191
bin_class_b = [bin(b) for b in range(128, 192, 1)]
bin_class_b[0], bin_class_b[-1] # 10000000 to 10111111

# CLASS C
class_c = [c for c in range(192, 224, 1)] # 192 - 223
bin_class_c = [bin(c) for c in range(192, 224, 1)]
bin_class_c[0], bin_class_c[-1] # 11000000 to 11011111

# NETMASKS - Netpart equals 255, Hostpart equals 0
netmask_class_a = '255.0.0.0'       # 11111111.00000000.00000000.00000000
netmask_class_b = '255.255.0.0'     # 11111111.11111111.00000000.00000000
netmask_class_c = '255.255.255.0'   # 11111111.11111111.11111111.00000000

# NUMBER OF POSSIBLE HOSTS
def get_hosts(binary_digits):
    return 2**binary_digits - 2

if __name__ == '__main__':
    # e.g. 10.0.0.1
    n_hosts_class_a = get_hosts(24) # 24 bit range for possible hosts
    print(n_hosts_class_a) # 16777214
    
    # e.g. 167.16.15.3
    n_host_class_b = get_hosts(16) # 16 bit range for possible hosts
    print(n_host_class_b) # 65534
    
    # e.g. 192.168.0.1
    n_host_class_c = get_hosts(8)  # 8 bit range for possible hosts
    print(n_host_class_c) # 254
