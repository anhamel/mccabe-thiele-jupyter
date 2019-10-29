
def readprgm(fin):
    import numpy as np
    rows = fin.readlines()
    name = list()
    A_list = list()
    B_list = list()
    C_list = list()
    t1_list = list()
    t2_list = list()
    placekeep = list()
    first_line = rows[0][0]
    
    if first_line == 'L':
        id_num = 0
        rows = rows[1:]
        for row in rows:
            row_str = str(row)
            row_split = row_str.split(' ')
            if len(row_split) == 2:
                del(placekeep[:])
                placekeep.append(row_split[0] + " " + row_split[1])
                row_split = placekeep
            for n in row_split:
                split = n.split('\t')
                split_last = split[-1].split('\n')
                split_last = split_last[0]
                t2_list.append(float(split_last))
                t1_list.append(float(split[-2]))
                C_list.append(float(split[-3]))
                B_list.append(float(split[-4])) 
                A_list.append(float(split[-5]))
                name_str = split[-6] + ' ' + split[-2] + '-' + split_last + '°C ' 
                name.append(name_str)        

        length = len(name)
        Antoine_mtrx = np.zeros((length,5))
        antoine_dict = dict()
        for n in range(length):
            Antoine_mtrx[n,0] = A_list[n]
            Antoine_mtrx[n,1] = B_list[n]
            Antoine_mtrx[n,2] = C_list[n]
            Antoine_mtrx[n,3] = t1_list[n]
            Antoine_mtrx[n,4] = t2_list[n]
            antoine_dict[name[n]] = {'a':A_list[n], 'b':B_list[n], 'c':C_list[n], 't1':t1_list[n], 't2':t2_list[n], 'name':name[n]}
        return(Antoine_mtrx,antoine_dict,name,A_list,B_list,C_list,t1_list,t2_list,id_num)
 
    else:
        id_num = 1
        for row in rows:
            row_str = str(row)
            row_split = row_str.split(' ')
            if len(row_split) == 2:
                del(placekeep[:])
                placekeep.append(row_split[0] + " " + row_split[1])
                row_split = placekeep
            for n in row_split:
                split = n.split('\t')
                split_last = split[-1].split('\n')
                split_last = split_last[0]
                t2_list.append(float(split_last))
                t1_list.append(float(split[-2]))
                C_list.append(float(split[-3]))
                B_list.append(float(split[-4])) 
                A_list.append(float(split[-5]))
                if len(n) == 6:
                    name.append(split[0] + split[1])
                else:
                    name.append(split[0])
        length = len(name)
        Antoine_mtrx = np.zeros((length,5))
        antoine_dict = dict()
        for n in range(length):
            Antoine_mtrx[n,0] = A_list[n]
            Antoine_mtrx[n,1] = B_list[n]
            Antoine_mtrx[n,2] = C_list[n]
            Antoine_mtrx[n,3] = t1_list[n]
            Antoine_mtrx[n,4] = t2_list[n]
            antoine_dict[name[n]] = {'a':A_list[n], 'b':B_list[n], 'c':C_list[n], 't1':t1_list[n], 't2':t2_list[n], 'name':name[n]}
        return(Antoine_mtrx,antoine_dict,name,A_list,B_list,C_list,t1_list,t2_list,id_num)
  
