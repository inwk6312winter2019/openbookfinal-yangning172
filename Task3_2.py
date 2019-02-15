from get-network-devices import*

def get_network_device_count():
    count = 0
    for i in r_Json "[Response]" :
        if i == "id":
            count += 1
    print(count) 
