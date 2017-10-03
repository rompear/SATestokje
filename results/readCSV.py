"""
Document: sudoku_loader.py
Made by: Romeo Goosens, Joe Harrison
UVA_numbers: 10424458, 11770430
"""

import csv
import numpy as np

"""
Remove outliers
"""
def reject_outliers(data, m=6):
    return data[abs(data - np.mean(data)) < m * np.std(data)]

"""
Read and write data to results.csv
"""
def reader(filename, n, percent):
    csvfile = 'results.csv'
    fieldnames_read = ['max_decision', '#decision', 'detail', '#vars','#clauses','#literals','added_confilcts', 'shrink', 'deleted_conflict_clauses', 'delete_clauses', 'added_confilcts_literals', 'deleted_total_literals', 'implications', 'run_time', 'type']
    filenames_write = ['n', 'percent', 'avg_all', 'avg_1', 'avg_2']
    avg_all = []
    avg_1 = []
    avg_2 = []

    with open(filename) as filenames:

        reader = csv.DictReader(filenames, delimiter=';')
        for row in reader:
            for fieldname in fieldnames_read:
                if(fieldname == '#decision'):
                    try:
                        if(row['type'] == 'all'):
                            avg_all.append(int(row[fieldname]))
                        elif(row['type'] == '1'):
                            avg_1.append(int(row[fieldname]))
                        elif(row['type'] == '2'):
                            avg_2.append(int(row[fieldname]))
                    except Exception as e:
                        print(e)

    avg_all = reject_outliers(np.array(avg_all))

    avg_1 = reject_outliers(np.array(avg_1))
    avg_2 = reject_outliers(np.array(avg_2))

    with open(csvfile, 'a') as csvfiles:
        writer = csv.DictWriter(csvfiles, fieldnames=filenames_write, delimiter=';')
        writer.writerow({filenames_write[0]: n, filenames_write[1]: percent, filenames_write[2]: np.average(avg_all), filenames_write[3]: np.average(avg_1), filenames_write[4]: np.average(avg_2)})

"""
MAIN
"""
if __name__ == '__main__':
    ns = [1,2,3,4,5,6,7,8]
    procents = [10,20,30,40,50,60,70,80,90]
    for n in ns:
        for procent in procents:
            filename =str(procent)+'procent/sudoku_'+str(n)+'.csv'
            reader(filename, n, procent)