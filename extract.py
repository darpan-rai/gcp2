import csv

writer = csv.writer(open('log_b.csv', 'a'))
writer.writerow(['IP Address', 'Request Time', 'Request Type', 'Status Code', 'Bytes', 'URL', 'Browser'])

file = open('log_b.txt', 'r')
for line in file:
    split_line = line.split(' ')
    ip = split_line[0]
    request_time = (split_line[3]+split_line[4])[1:(len(split_line[3]+split_line[4]))-1]
    request_type = (split_line[5]+split_line[6]+split_line[7])[1:(len(split_line[5] + split_line[6] + split_line[7]))-1]
    status_code = split_line[8]
    number_of_bytes = split_line[9]
    url = split_line[10][1:len(split_line[10])-1]
    i = 1
    while (split_line[11][i] != "/"):
        i += 1
    browser = split_line[11][1:i]

    writer.writerow([ip, request_time, request_type, status_code, number_of_bytes, url, browser])

file.close()
