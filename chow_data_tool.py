import numpy as np
import os
import shutil
import matplotlib.pyplot as plt


def xyz(dateiname , datenliste):
    # print(os.getcwd())
    if 'horizon' in dateiname:
        string = 'x' + str(datenlist[1][0]) + ' y ' + str(datenlist[1][1]) + ' z ' + str(datenlist[1][2]) + 'horizontal.csv'
        f = open(string, 'w')
        f.write('# x in m  \ty in m \t z in m \t U_x in m/s \t U_y in m/s \t U_z in m/S \n')
        for a in datenliste:
            x = a[0]
            y = a[1]
            z = a[2]
            ux = a[3]
            uy = a[4]
            uz = a[5]
            f.write(str(x) + ',' + str(y) + ',' + str(z) + ',' + str(ux) + ',' + str(uy) + ',' + str(uz)+'\n')
        f.close()

    if 'verti' in dateiname:
        string='x ' + str(datenlist[1][0]) + ' y ' + str(datenlist[1][1]) + ' z ' + str(datenlist[1][2]) + 'vertical.csv'
        f = open(string, 'w')
        f.write('# x in m  \ty in m \t z in m \t U_x in m/s \t U_y in m/s \t U_z in m/S \n')
        for a in datenliste:
            x = a[0]
            y = a[1]
            z = a[2]
            ux = a[3]
            uy = a[4]
            uz = a[5]
            f.write(str(x) + ',' + str(y) + ',' + str(z) + ',' + str(ux) + ',' + str(uy) + ',' + str(uz)+'\n')
        f.close()
    return ()


def plot(dateiname, dateiliste):
    cwd = os.getcwd()

    if 'horizon' in dateiname:
        print('horizontalplot \n' , os.getcwd())
        os.chdir(cwd+'/plots')

        # #####################
        #  U_y plot
        # #####################
        f = plt.figure()
        x_val = [x[2] for x in datenlist]
        y_val = [x[4]/51.82 for x in datenlist]
        plt.xlabel('z var, x:' + str(datenlist[1][0]) + '\t' + 'y:' + str(datenlist[1][1]))
        plt.ylabel('U_y')
        plt.grid(True)
        plt.plot(x_val, y_val, linestyle='None')
        plt.plot(x_val, y_val, 'or', linestyle='None')
        f.savefig(dateiname + 'u_y:51.82 uber z' + ' x:' + str(datenlist[1][0]) + '\t' + 'y:' + str(datenlist[1][1]) + '.pdf', bbox_inches='tight')

        # #####################
        #  U_z plot_Nomiert
        # #####################
        f = plt.figure()
        x_val = [x[2] for x in datenlist]
        y_val = [x[5]/51.82 for x in datenlist]
        plt.xlabel('z var, x:' + str(datenlist[1][0]) + '\t' + 'y:' + str(datenlist[1][1]))
        plt.ylabel('U_z/51.82')
        plt.grid(True)
        plt.plot(x_val, y_val, linestyle='None')
        plt.plot(x_val, y_val, 'or', linestyle='None')
        f.savefig(dateiname + 'u_z:51.82 uber z' + ' x:' + str(datenlist[1][0]) + '\t' + 'y:' + str(datenlist[1][1]) + '.pdf',
                  bbox_inches='tight')
        plt.close('all')

    elif 'verti' in dateiname:
        print('verticalplot \n' , os.getcwd())
        os.chdir(cwd+'/plots')

        # # #####################
        # #  U_x plot
        # # #####################
        # f = plt.figure()
        # x_val = [x[1] for x in datenlist]
        # y_val = [x[3] for x in datenlist]
        # plt.xlabel('y var, x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]))
        # plt.ylabel('U_x')
        # plt.plot(x_val, y_val, linestyle='None')
        # plt.plot(x_val, y_val, 'or', linestyle='None')
        # f.savefig(dateiname + 'u_x uber y x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]) + '.pdf', bbox_inches='tight')
        # plt.close()

        # #####################
        #  U_x plot normiert
        # #####################
        f = plt.figure()
        x_val = [x[1] for x in datenlist]
        y_val = [x[3]/51.82 for x in datenlist]
        plt.xlabel('y var, x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]))
        plt.ylabel('U_x/51.82')
        plt.plot(x_val, y_val, linestyle='None')
        plt.plot(x_val, y_val, 'or', linestyle='None')
        f.savefig(dateiname + 'u_x:51.82 uber y x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]) + '.pdf', bbox_inches='tight')
        plt.close()

        # #####################
        # ## U_z plot normiert
        # #####################
        # f = plt.figure()
        # x_val = [x[1]/1.2192 for x in datenlist]
        # y_val = [x[5]/51.82 for x in datenlist]
        # #y_val = [np.sqrt(x[4]**2+x[5]**2)/51.82 for x in datenlist]
        # #  xlim((left, right)) restrain x/yrange
        # #  plt.xlim((max(datenlist[5])*0.9 , max(datenlist[5])*1.1))
        # #  plt.ylim((max(datenlist[1])*0.9 , max(datenlist[1])*1.1))
        # plt.xlabel('y var, x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]))
        # plt.ylabel('U_z/51.82')
        # plt.grid(True)
        # plt.plot(x_val, y_val, linestyle='None')
        # plt.plot(x_val, y_val, 'or', linestyle='None')
        # f.savefig(dateiname + 'u_z:51.82 uber y x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]) + '.pdf', bbox_inches='tight')
        # plt.close('all')

        #####################
        ## U_crossflow
        #####################
        f = plt.figure()
        x_val = [x[1]/1.2192 for x in datenlist]
        # crossflow velocity = U_cross=sqrt(u_y**2+u_z**2)/u_inlet
        y_val = [(np.sqrt(x[4]**2+x[5]**2)/51.82)  for x in datenlist]
        # y_val = [np.sqrt(x[4]**2+x[5]**2)/51.82 for x in datenlist]
        #  xlim((left, right)) restrain x/yrange
        #  plt.xlim((max(datenlist[5])*0.9 , max(datenlist[5])*1.1))
        #  plt.ylim((max(datenlist[1])*0.9 , max(datenlist[1])*1.1))
        plt.xlabel('y var, x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]))
        plt.ylabel('U_crossflow sqrt(u_y**2+u_z**2)/u_inlet')
        plt.grid(True)
        plt.plot(x_val, y_val, linestyle='None')
        plt.plot(x_val, y_val, 'or', linestyle='None')
        f.savefig(dateiname + 'u_cross uber y x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]) + '.pdf', bbox_inches='tight')
        plt.close('all')





        # # #####################
        # #  U_y plot
        # # #####################
        # f = plt.figure()
        # x_val = [x[1]/1.2192 for x in datenlist]
        # y_val = [x[4]/51.82 for x in datenlist]
        # #y_val = [np.sqrt(x[4]**2+x[5]**2)/51.82 for x in datenlist]
        # #  xlim((left, right)) restrain x/yrange
        # #  plt.xlim((max(datenlist[5])*0.9 , max(datenlist[5])*1.1))
        # #  plt.ylim((max(datenlist[1])*0.9 , max(datenlist[1])*1.1))
        # plt.xlabel('y var, x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]))
        # plt.ylabel('U_y/51.82')
        # plt.grid(True)
        # plt.plot(x_val, y_val, linestyle='None')
        # plt.plot(x_val, y_val, 'or', linestyle='None')
        # f.savefig(dateiname + 'u_y:51.82 uber y x:' + str(datenlist[1][0]) + '\t' + 'z:' + str(datenlist[1][2]) + '.pdf', bbox_inches='tight')
        # plt.close('all')

    return()


if __name__ == '__main__':
    mydata = np.genfromtxt(str("chow_meter_origin_trailingedge.csv"), skip_header=0, dtype=float, delimiter=',')
    print(type(mydata))
    print('bytes' , mydata.nbytes)
    x_list = []
    y_list = []
    z_list = []
    #  mydata=np.array([[1,2,3],[1,3,2],[1,4,5],[1,7,8],[1,10,8]])
    #  get all different x,y,z values into one list
    for i in mydata:
        # print(i)
        if i.item(0) not in x_list and 0.85 > i.item(0) > -0.37:
            x_list.append(i.item(0))

        if i.item(1) not in y_list:
            y_list.append(i.item(1))

        if i.item(2) not in z_list and 0.9 > i.item(2) > 0.75:
            z_list.append(i.item(2))

    print(mydata.shape)
    #  check for directories and create / delete recreate
    if 'vertikaleplots' in os.listdir():
        shutil.rmtree(os.getcwd() + '/vertikaleplots')
        os.mkdir(os.getcwd() + '/vertikaleplots', 0o777)
        os.mkdir(os.getcwd() + '/vertikaleplots/plots', 0o777)
    if 'vertikaleplots' not in os.listdir():
        os.mkdir(os.getcwd() + '/vertikaleplots', 0o777)
        os.mkdir(os.getcwd() + '/vertikaleplots/plots', 0o777)
    if 'horizontaleplots' in os.listdir():
        shutil.rmtree(os.getcwd() + '/horizontaleplots')
        os.mkdir(os.getcwd() + '/horizontaleplots', 0o777)
        os.mkdir(os.getcwd() + '/horizontaleplots/plots', 0o777)
    if 'horizontaleplots' not in os.listdir():
        os.mkdir(os.getcwd() + '/horizontaleplots', 0o777)
        os.mkdir(os.getcwd() + '/horizontaleplots/plots', 0o777)

    n=0
    nn=0
    cwd = os.getcwd()
    vcwd=cwd+'/vertikaleplots'
    hcwd=cwd+'/horizontaleplots'
    os.chdir(cwd)
    for x in x_list:

    #     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #     #        Horizontalv2
    #     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #     for y in y_list:
    #         datenlist = []
    #         for i in mydata:
    #             if i.item(0)==x and i.item(1)==y:
    #                 datenlist.append(i)
    #                 # print('dinge')
    #                 n=n+1
    #                 print(n, 'compared values:')
    #         dateiname = 'horizontaleplots'
    #         if len(datenlist) > 1:
    #             os.chdir(hcwd)
    #             xyz(dateiname, datenlist)
    #             plot(dateiname, datenlist)
    #             os.chdir(hcwd)
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        #        Vertikale linienv2
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        os.chdir(cwd)
        for z in z_list:

            datenlist = []
            for i in mydata:

                if i.item(0) == x and i.item(2) == z:
                    datenlist.append(i)
                    #  print('dinge')
                    n = n + 1
                    print(n, 'compared values:', n)

            dateiname = 'vertikaleplots'
            if len(datenlist) > 1:
                os.chdir(vcwd)
                xyz(dateiname, datenlist)
                plot(dateiname, datenlist)
                os.chdir(vcwd)
        print ('new x:',  x, 'von:', x_list)
    print('alle Daten Fertig')
