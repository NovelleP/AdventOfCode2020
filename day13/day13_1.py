if __name__ == '__main__':
    with open('input', 'r') as f:
        time = int(f.readline())
        bus_ids = [int(bus_id) for bus_id in f.readline().split(',') if bus_id != 'x']

    min_waitting = float('inf')
    selected_busid = -1
    for bus_id in bus_ids:
        c = time // bus_id
        nearest_time = bus_id * c if (bus_id * c) >= time else (bus_id * (c + 1))
        if (curr_min_waitting := (nearest_time - time)) < min_waitting:
            min_waitting = curr_min_waitting
            selected_busid = bus_id
    print(min_waitting * selected_busid)