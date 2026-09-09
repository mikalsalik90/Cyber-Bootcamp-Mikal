ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1"]

def get_unique_ips(ip_list):
    return sorted(list(set(ip_list)))

print (get_unique_ips(ips))