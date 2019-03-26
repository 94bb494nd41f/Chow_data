import numpy as np
import os
import shutil
import matplotlib.pyplot as plt

def xyz(dateiname , datenliste):
    if 'horizon' in dateiname:
        string='x ' + str(datenlist[3][0]) + ' y ' + str(datenlist[3][1]) + ' z ' + str(datenlist[3][2]) + 'horizontal.csv'
        f = open(string, 'w')
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

    if 'verti' in dateiname:
        string='x ' + str(datenlist[3][0]) + ' y ' + str(datenlist[3][1]) + ' z ' + str(datenlist[3][2]) + 'vertical.csv'
        f = open(string, 'w')
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


def plot(dateiname, dateiliste):


    if 'horizon' in dateiname:
        if dateiliste[3][0]>0 and 0.36 > dateiliste[3][1]>0 :
            os.chdir(cwd+'/horizontaleplots/plots')

            f = plt.figure()
            x_val = [x[2] for x in datenlist]
            y_val = [x[4] for x in datenlist]
            plt.xlabel('z var, x:' + str(datenlist[3][0]) + '\t' + 'y:' + str(datenlist[3][1]))
            plt.ylabel('U_y')
            plt.plot(x_val, y_val, linestyle='None')
            plt.plot(x_val, y_val, 'or', linestyle='None')
            f.savefig(dateiname + 'u_y uber z' + '.pdf', bbox_inches='tight')

    elif 'verti' in dateiname:
        if dateiliste[3][0] > 0 and 1.2 >dateiliste[3][2] > 0.68:

            os.chdir(cwd+'/vertikaleplots/plots')

            f = plt.figure()
            x_val = [x[1] for x in datenlist]
            y_val = [x[3] for x in datenlist]
            plt.xlabel('y var, x:' + str(datenlist[3][0]) + 'z:' + str(datenlist[3][2]))
            plt.ylabel('U_x')
            plt.plot(x_val, y_val, linestyle='None')
            plt.plot(x_val, y_val, 'or', linestyle='None')
            f.savefig(dateiname + 'u_x uber y' + '.pdf', bbox_inches='tight')
            plt.close()


            f = plt.figure()
            x_val = [x[1] for x in datenlist]
            y_val = [x[5] for x in datenlist]
            plt.xlabel('y var, x:' + str(datenlist[3][0]) + '\t' + 'z:' + str(datenlist[3][2]))
            plt.ylabel('U_z')
            plt.plot(x_val, y_val, linestyle='None')
            plt.plot(x_val, y_val, 'or', linestyle='None')
            f.savefig(dateiname + 'u_zx uber y' + '.pdf', bbox_inches='tight')
            plt.close()





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

    print(mydata.shape)
    shutil.rmtree(os.getcwd() + '/vertikaleplots')
    os.mkdir(os.getcwd() + '/vertikaleplots', 0o777)
    #shutil.rmtree(os.getcwd() + '/vertikaleplots/plots')
    os.mkdir(os.getcwd() + '/vertikaleplots/plots', 0o777)
    shutil.rmtree(os.getcwd() + '/horizontaleplots')
    os.mkdir(os.getcwd() + '/horizontaleplots', 0o777)
    #shutil.rmtree(os.getcwd() + '/horizontaleplots/plots')
    os.mkdir(os.getcwd() + '/horizontaleplots/plots', 0o777)

    cwd=os.getcwd()
    #########################################
    #       Vertikale linien
    #########################################
    n=0

    os.chdir(os.getcwd()+'/vertikaleplots')
    vcwd=os.getcwd()
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
                plot(dateiname, datenlist)
                os.chdir(vcwd)

            print('new z vert')
        print('new y vert')
    print ('new x vert')


    #############################################
    #       Horizontal
    #############################################
    n=0
    os.chdir(cwd+'/horizontaleplots')
    hcwd=os.getcwd()
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
                plot(dateiname, datenlist)
                os.chdir(hcwd)
            print('new z hor')
        print('new y hor')
    print ('new x hor')