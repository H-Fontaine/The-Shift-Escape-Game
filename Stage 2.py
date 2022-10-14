data = [[48644524,"A1 Stone","12/2250"],
[96877928,"CoMoonIcations","5/2248"],
[17452966,"Moon&Co","5/2249"],
[32017455,"Sirota","4/2248"],
[79102938,"Mach Storage","4/2248"],
[32017455,"Sirota","12/2249"],
[35673565,"Solgona","4/2248"],
[79102938,"Mach Storage","2/2250"],
[92305923,"Marketoont","2/2248"],
[32017455,"Sirota","1/2248"],
[92305923,"Marketoont","12/2248"],
[16235167,"Dash Moon","7/2250"],
[98578956,"Lumian","1/2250"],
[79102938,"Mach Storage","5/2248"],
[35673565,"Solgona","7/2249"],
[15546787,"Iphinstone","1/2248"],
[72321311,"Arise Ltd","8/2248"],
[38502761,"LunarTransport","2/2249"],
[79102938,"Mach Storage","2/2248"],
[98578956,"Lumian","9/2249"],
[17452966,"Moon&Co","2/2249"],
[68365833,"Moonbrite","5/2248"],
[25419991,"Spero","6/2250"],
[79102938,"Mach Storage","12/2249"],
[16235167,"Dash Moon","9/2249"],
[70898547,"Exchangex","1/2250"],
[38502761,"LunarTransport","6/2249"],
[96877928,"CoMoonIcations","2/2250"],
[17452966,"Moon&Co","4/2250"],
[78162537,"Far Away Limited","9/2250"],
[57326522,"LisaLuna","11/2250"],
[35673565,"Solgona","9/2248"],
[38502761,"LunarTransport","10/2250"],
[16235167,"Dash Moon","12/2249"],
[98578956,"Lumian","4/2249"],
[96877928,"CoMoonIcations","7/2250"],
[15546787,"Iphinstone","8/2248"],
[98578956,"Lumian","4/2248"],
[98578956,"Lumian","4/2248"],
[68365833,"Moonbrite","2/2248"],
[96877928,"CoMoonIcations","5/2250"],
[68362850,"Lunestone","3/2248"],
[78162537,"Far Away Limited","1/2250"],
[78162537,"Far Away Limited","9/2250"],
[96877928,"CoMoonIcations","5/2249"],
[79102938,"Mach Storage","10/2250"],
[48644524,"A1 Stone","12/2248"],
[48644524,"A1 Stone","12/2249"],
[38502761,"LunarTransport","1/2250"],
[79102938,"Mach Storage","9/2249"],
[48644524,"A1 Stone","6/2249"],
[67456889,"Luneca","1/2249"],
[48644524,"A1 Stone","12/2250"],
[78162537,"Far Away Limited","9/2249"],
[32017455,"Sirota","7/2249"],
[15546787,"Iphinstone","10/2249"],
[25419991,"Spero","9/2248"],
[35673565,"Solgona","4/2249"],
[72321311,"Arise Ltd","12/2250"],
[92305923,"Marketoont","4/2249"],
[15546787,"Iphinstone","6/2250"],
[79102938,"Mach Storage","9/2250"],
[15546787,"Iphinstone","4/2250"],
[96877928,"CoMoonIcations","12/2249"],
[38502761,"LunarTransport","9/2249"],
[48644524,"A1 Stone","5/2248"],
[16235167,"Dash Moon","1/2249"],
[25419991,"Spero","10/2248"],
[96877928,"CoMoonIcations","12/2249"],
[68365833,"Moonbrite","7/2248"],
[17452966,"Moon&Co","2/2249"],
[67456889,"Luneca","10/2250"],
[96877928,"CoMoonIcations","6/2248"],
[35673565,"Solgona","9/2248"],
[98578956,"Lumian","11/2249"],
[32017455,"Sirota","9/2248"],
[15546787,"Iphinstone","10/2248"],
[48644524,"A1 Stone","7/2250"],
[38502761,"LunarTransport","7/2249"],
[96877928,"CoMoonIcations","5/2248"],
[78162537,"Far Away Limited","5/2248"],
[68365833,"Moonbrite","12/2250"],
[17452966,"Moon&Co","2/2248"],
[25419991,"Spero","10/2248"],
[35673565,"Solgona","11/2249"],
[48644524,"A1 Stone","8/2250"],
[16235167,"Dash Moon","3/2250"],
[67456889,"Luneca","3/2249"],
[32017455,"Sirota","4/2250"],
[68365833,"Moonbrite","6/2249"],
[68362850,"Lunestone","1/2250"],
[68362850,"Lunestone","2/2249"],
[98578956,"Lumian","10/2249"],
[32017455,"Sirota","11/2250"],
[35673565,"Solgona","5/2249"],
[68362850,"Lunestone","8/2250"],
[67456889,"Luneca","7/2250"],
[96877928,"CoMoonIcations","7/2248"],
[98578956,"Lumian","10/2249"]]



from operator import index
import pandas as pd
import numpy as np


data = np.array(data)
database = pd.DataFrame(data, columns=['Send_ID','Send_CO','Tran_DA'])

def detect_reccurenceV1(database) :
    database = database.to_numpy(dtype = str)
    dates = np.asarray(np.char.rpartition(database[:,2], sep = '/')[:,[0,2]], dtype=int)
    min_year = np.amin(dates[:,1])
    database = np.concatenate([np.reshape(np.asarray(database[:,0], dtype = int), (np.shape(database)[0],1)), np.reshape(dates[:,0] + ((dates[:,1] % min_year) * 12), (np.shape(database)[0],1)) ], axis = 1)

    ##print(database)
    hashmap1 = {database[0][0] : 0}
    hashmap2 = {0 : database[0][0]}
    database[0][0] = 0
    index = 1
    max_date = database[0][1]
    for i in range(1, np.shape(database)[0]) :
        if database[i][1] >= max_date :
            max_date = database[i][1]
        if database[i][0] not in hashmap1 :
            hashmap1[database[i][0]] = index
            hashmap2[index] = database[i][0]
            database[i][0] = index
            index += 1
        else :
            database[i][0] = hashmap1[database[i][0]]
    ##print(database)

    data = np.zeros((index, max_date), dtype= int)
    for i in range(0, np.shape(database)[0]) :
        data[database[i][0]][database[i][1] - 1] = 1





def detect_reccurenceV2(database) :
    database = database.to_numpy(dtype = str)
    dates = np.asarray(np.char.rpartition(database[:,2], sep = '/')[:,[0,2]], dtype=int) ##on parse les dates
    min_year = np.amin(dates[:,1])    
    database = np.stack((np.asarray(database[:,0], dtype = int), dates[:,0] + (((dates[:,1] % min_year) * 12))), axis = -1) ##On prend comme origine des temps janvier de l'année la plus petite et comme unité le mois

    database_lenght = len(database)
    

    #Le but de cette partie du code est de recupérer la date maximale et simplifier les id vers des int de petite taille
    id_to_index = {database[0][0] : 0} #Hashmap pour savoir facilement si on a déjà vu cette id
    index_to_id = [database[0][0]] #La reciproque de la hashmap
    database[0][0] = 0
    nb_of_ids = 1
    max_date = database[0][1]
    for i in range(1, database_lenght) :
        if database[i][1] >= max_date :
            max_date = database[i][1]
        if database[i][0] not in id_to_index :
            id_to_index[database[i][0]] = nb_of_ids
            index_to_id.append(database[i][0])
            database[i][0] = nb_of_ids
            nb_of_ids += 1
        else :
            database[i][0] = id_to_index[database[i][0]] #ugfuygfutykjkj
    


    #Création d'un tableau dans lequel chaque ligne représente les opérations faite par une entreprise : True = opération réalisé ce mois, False = pas d'opération réalisé ce mois
    data = np.zeros((nb_of_ids, max_date), dtype= bool)
    for i in range(0, database_lenght) :
        data[database[i][0]][database[i][1] - 1] = True

    cheating_ids = []


    #Pour chaque ligne (entreprise)
    for i in range(0, nb_of_ids) :
        index_1 = 0
        cheating = False
        while index_1 < max_date and not cheating :
            while index_1 < max_date and not data[i][index_1] :
                index_1 += 1
            
            next_index = index_1 + 1
            index_2 = next_index
            first = True
            while 2 * index_2 - index_1 < max_date and not cheating :
                while 2 * index_2 - index_1 < max_date and not data[i][index_2] :
                    index_2 += 1
                
                if first :
                    next_index = index_2
                    first = False

                if 2 * index_2 - index_1 < max_date and data[i][2 * index_2 - index_1] :
                    cheating_ids.append(index_to_id[i])
                    cheating = True
                else :
                    index_2 += 1
            
            index_1 = next_index #sqfsqfqsdf

    return cheating_ids





def detect_reccurenceV3(database) :
    database = database.to_numpy(dtype = str)
    dates = np.asarray(np.char.rpartition(database[:,2], sep = '/')[:,[0,2]], dtype=int)
    min_year = np.amin(dates[:,1])    
    database = np.stack((np.asarray(database[:,0], dtype = int), dates[:,0] + (((dates[:,1] % min_year) * 12))), axis = -1)

    database_lenght = np.shape(database)[0]
    
    id_to_index = {database[0][0] : 0}
    index_to_id = [database[0][0]]
    database[0][0] = 0
    nb_of_ids = 1
    max_date = database[0][1]
    for i in range(1, database_lenght) :
        if database[i][1] >= max_date :
            max_date = database[i][1]
        if database[i][0] not in id_to_index :
            id_to_index[database[i][0]] = nb_of_ids
            index_to_id.append(database[i][0])
            database[i][0] = nb_of_ids
            nb_of_ids += 1
        else :
            database[i][0] = id_to_index[database[i][0]]
    
    data = np.zeros((nb_of_ids, max_date), dtype= int)
    for i in range(0, database_lenght) :
        data[database[i][0]][database[i][1] - 1] = 1
    
    sequences = np.fromiter((np.concatenate([[1], np.zeros(i, dtype = int), [1], np.zeros(i, dtype = int), [1]]) for i in range(int((max_date - 3) / 2) + 1)), dtype = np.ndarray, count=int((max_date - 3) / 2) + 1)
    cheating_ids = []
    for index in range(nb_of_ids) :
        for sequence in sequences :
            if np.isin(3, np.correlate(data[index], sequence)) :
                cheating_ids.append(index_to_id[index])
                break
    
    return cheating_ids





def detect_reccurenceV4(database) :
    database = database.to_numpy(dtype = str)
    dates = np.asarray(np.char.rpartition(database[:,2], sep = '/')[:,[0,2]], dtype=int)
    min_year = np.amin(dates[:,1])    
    database = np.stack((np.asarray(database[:,0], dtype = int), dates[:,0] + (((dates[:,1] % min_year) * 12))), axis = -1)

    database_lenght = np.shape(database)[0]
    
    id_to_index = {database[0][0] : 0}
    index_to_id = [database[0][0]]
    database[0][0] = 0
    nb_of_ids = 1
    max_date = database[0][1]
    for i in range(1, database_lenght) :
        if database[i][1] >= max_date :
            max_date = database[i][1]
        if database[i][0] not in id_to_index :
            id_to_index[database[i][0]] = nb_of_ids
            index_to_id.append(database[i][0])
            database[i][0] = nb_of_ids
            nb_of_ids += 1
        else :
            database[i][0] = id_to_index[database[i][0]]
    
    index_to_id = np.array(index_to_id)

    data = np.zeros((nb_of_ids, max_date), dtype= int)
    for i in range(0, database_lenght) :
        data[database[i][0]][database[i][1] - 1] = 1

    preselect = np.fromiter((not np.all([np.correlate(data[i], data[i], "full")[:max_date - 1] <= 1]) for i in range(nb_of_ids)), dtype=bool, count = nb_of_ids)
    data = data[preselect]
    index_to_id = index_to_id[preselect]

    cheating_ids = []

    for i in range(0, len(data)) :
        index_1 = 0
        cheating = False
        while index_1 < max_date and not cheating :
            while index_1 < max_date and not data[i][index_1] :
                index_1 += 1
            
            next_index = index_1 + 1
            index_2 = next_index
            first = True
            while 2 * index_2 - index_1 < max_date and not cheating :
                while 2 * index_2 - index_1 < max_date and not data[i][index_2] :
                    index_2 += 1
                
                if first :
                    next_index = index_2
                    first = False

                if 2 * index_2 - index_1 < max_date and data[i][2 * index_2 - index_1] :
                    cheating_ids.append(index_to_id[i])
                    cheating = True
                else :
                    index_2 += 1
            
            index_1 = next_index

    return cheating_ids



import time

start_time = time.time_ns()
for i in range(1000) :
    detect_reccurenceV2(database)
print("--- %s seconds --- V2" % ((time.time_ns() - start_time) / 10**9 ))

start_time = time.time_ns()
for i in range(1000) :
    detect_reccurenceV3(database)
print("--- %s seconds --- V3" % ((time.time_ns() - start_time) / 10**9 ))

start_time = time.time_ns()
for i in range(1000) :
    detect_reccurenceV4(database)
print("--- %s seconds --- V4" % ((time.time_ns() - start_time) / 10**9 ))

if detect_reccurenceV2(database) == detect_reccurenceV3(database) == detect_reccurenceV4(database) :
    print("They all agreed on the response")
else :
    print("At least une function didn't send the same result than the others")