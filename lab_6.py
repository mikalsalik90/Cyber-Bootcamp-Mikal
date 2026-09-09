ips=["192.168.1.1","10.0.0.1","192.168.1.1"]

def unique_sorted_ips(ips_list):
    unique_ips = set(ips_list)
    sorted_ips = sorted(unique_ips)
    return sorted_ips
print(unique_sorted_ips(ips))
