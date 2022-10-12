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

from gpg import Data
import pandas as pd
import numpy as np
import scipy.signal as sc

data = np.array(data)
database = pd.DataFrame(data, columns=['Send_ID','Send_CO','Tran_DA'])

def detect_reccurence(database) :
    database = database.to_numpy(dtype = str)
    dates = np.asarray(np.char.rpartition(database[:,2], sep = '/')[:,[0,2]], dtype=int)
    min_year = np.amin(dates[:,1])
    database = np.concatenate([np.reshape(np.asarray(database[:,0], dtype = int), (99,1)), np.reshape(dates[:,0] + ((dates[:,1] % min_year) * 12), (99,1)) ], axis = 1)

    print(database)
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
    print(database)

    data = np.zeros((index, max_date), dtype= int)
    for i in range(0, np.shape(database)[0]) :
        data[database[i][0]][database[i][1] - 1] = 1

    print(data)
    

    
    





detect_reccurence(database)