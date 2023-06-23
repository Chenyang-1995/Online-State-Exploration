import matplotlib.pyplot as plt




def draw_ARs_tradeoff(Algo_list,Algo_Names,fname,x_label='Consistency',y_label = 'Robustness', position = None):
    plt.cla()

    color_list = ['k','r','g', 'm', 'y',  'b', 'c','#CEFFCE','#D2691E']#['k','r','b', 'm', 'y', 'g',  ]
    marker_list = ['o', 'v', '^', '<', '>', 's','3','8','|','x'] #['o', 'v', '^', '<', '>', 's']
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    for i in range(len(Algo_Names)):

        print(Algo_list[i][0])
        print(Algo_list[i][1])
        plt.plot(Algo_list[i][0], Algo_list[i][1], color=color_list[i],linestyle='-', linewidth=1,label = Algo_Names[i], marker=marker_list[i])


    if len(Algo_Names) > 1:
        if position == None:
            plt.legend(loc='upper right')
        else:
            plt.legend(loc=position)
    plt.tight_layout()
    plt.savefig(fname, dpi=200)

def draw_ARs_tradeoff_log_scale(Algo_list,Algo_Names,fname,x_label='Consistency',y_label = 'Robustness', position = None):
    plt.cla()

    color_list = ['k','r','g', 'm', 'y',  'b', 'c','#CEFFCE','#D2691E']#['k','r','b', 'm', 'y', 'g',  ]
    marker_list = ['o', 'v', '^', '<', '>', 's','3','8','|','x'] #['o', 'v', '^', '<', '>', 's']
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.yscale("log",basey=2)
    for i in range(len(Algo_Names)):

        print(Algo_list[i][0])
        print(Algo_list[i][1])
        plt.plot(Algo_list[i][0], Algo_list[i][1], color=color_list[i],linestyle='-', linewidth=1,label = Algo_Names[i], marker=marker_list[i])


    if len(Algo_Names) > 1:
        if position == None:
            plt.legend(loc='upper right')
        else:
            plt.legend(loc=position)
    plt.tight_layout()
    plt.savefig(fname, dpi=200)

