time = '1h 45m,360s,25m,30m 120s,2h 60s'
timelist = time.split(',')
total_min = 0
for i in timelist:
    timelist_total = i.split()
    for j in timelist_total:
        if 'h' in j:
            timelist1 = j.replace('h', '')
            total_min += 60*(int(timelist1))
        #timelist_n += t1
        elif 'm' in j:
            timelist2 = j.replace('m', '')
            total_min += 1*(int(timelist2))
        elif 's' in j:
            timelist3 = j.replace('s', '') 
            total_min +=  (int(timelist3))/60
print(int(total_min))


