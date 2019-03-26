import numpy as np
import os
import shutil

def xyz(dateiname , datenliste):
    print('schreib in Datei',dateiname)
    f = open(dateiname, 'w')
    f.write('#x in m  \ty in m \t z in m \t U_x in m/s \t U_y in m/s \t U_z in m/S \n')
    for a in datenliste:
        x = a[0]
        y = a[1]
        z = a[2]
        ux = a[3]
        uy = a[4]
        uz = a[5]
        f.write(str(x) + ',' + str(y) + ',' + str(z) + ',' + str(ux) + ',' + str(uy) + ',' + str(uz)+'\n')
    f.close




if __name__ == '__main__':
    mydata = np.genfromtxt(str("chow_meter+trans.csv"), skip_header=0, dtype=float, delimiter=',')
    print(type(mydata))
    print('bytes' , mydata.nbytes)
    x_list = []
    y_list = []
    z_list = []
    #mydata=np.array([[1,2,3],[1,3,2],[1,4,5],[1,7,8],[1,10,8]])
    for i in mydata:
        #print(i)
        if i.item(0) not in x_list:
            x_list.append(i.item(0))
        if i.item(1) not in y_list:
            y_list.append(i.item(1))
        if i.item(2) not in z_list:
            z_list.append(i.item(2))
    #print(x_list)
    #res=np.where(mydata == -0.4826)
    #print(res[1], type(res), len(res))
    print(mydata.shape)
    shutil.rmtree(os.getcwd() + '/vertikaleplots')
    os.mkdir(os.getcwd() + '/vertikaleplots', 0o777)
    shutil.rmtree(os.getcwd() + '/horizontaleplots')
    os.mkdir(os.getcwd() + '/horizontaleplots', 0o777)
    cwd=os.getcwd()
    #########################################
    #       Vertikale linien
    #########################################
    n=0

    os.chdir(os.getcwd()+'/vertikaleplots')
    for x in x_list:
        for y in y_list:
            datenlist=[]
            for z in z_list:
                for i in mydata:
                    if i.item(0)==x and i.item(1)==y and i.item(2)==z:
                        datenlist.append(i)
                        #print('dinge')
                        n=n+1
            print(datenlist,n)
            dateiname = 'vertikaleplots' + str(n)
            if len(datenlist) >= 3:
                xyz(dateiname, datenlist)

            print('new z vert')
        print('new y vert')
    print ('new x vert')


    #############################################
    #       Horizontal
    #############################################
    n=0
    os.chdir(cwd+'/horizontaleplots')
    for x in x_list:
        for z in z_list:
            datenlist=[]
            for y in y_list:
                for i in mydata:
                    if i.item(0)==x and i.item(1)==y and i.item(2)==z:
                        datenlist.append(i)
                        #print('dinge')
                        n=n+1
            print(datenlist,n)
            dateiname = 'horizontaleplots' + str(n)
            if len(datenlist) >= 3:
                xyz(dateiname, datenlist)

            print('new z hor')
        print('new y hor')
    print ('new x hor')




