import csv


def create_csv(csvfile_name, report_dict):
    with open('/tmp/'+csvfile_name+'.csv', 'wb') as f:  # Just use 'w' mode in 3.
        w = csv.writer(f)

        for key, value in report_dict.items():
            w.writerow([key, value])
