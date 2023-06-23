import math
import algorithm as alg
import numpy as np


def test_c_r_tradeoff():

    max_value = 1000
    instance_set = [(i,j) for i in range(1,max_value+1) for j in range(1,max_value+1)]

    DD_AR_crs = []
    RD_AR_crs = []
    DDP_AR_crs = []
    RDP_AR_crs = []
    PAD_AR_crs = []



    epss = np.arange(0.1,1.1,0.1)


    for eps in epss:
        consistent = 1+eps
        a1,a2, delta = alg.a_delta(consistent-1)


        print('a = {0}, delta = {1}, consistency = {2} eps = {3}'.format([a1,a2],delta,consistent,eps))

        PAD_consistency = 1+ eps
        DDP_consistency = PAD_consistency

        RDP_consistency = 1.0*a2*delta/((a2-1)*math.log(1+delta,math.e))
        print(RDP_consistency)


        DD_AR = np.array([-1.0 for _ in instance_set])
        RD_AR = np.array([-1.0 for _ in instance_set])
        DDP_AR = np.array([-1.0 for _ in instance_set])
        RDP_AR = np.array([-1.0 for _ in instance_set])
        PAD_AR = np.array([-1.0 for _ in instance_set])


        for i,instance_prediction in enumerate(instance_set):
            instance,prediction = instance_prediction
            _, DD_AR[i] = alg.doubling(instance)
            _, RD_AR[i] = alg.random_doubling(instance)
            _, DDP_AR[i] = alg.deterministic_prediction(instance,prediction,delta,a1)
            _, RDP_AR[i] = alg.randomized_prediction(instance,prediction,delta,a2)

            _, PAD_AR[i] = alg.PAD(instance,prediction,eps)




        DD_AR_crs.append([PAD_consistency,np.max(DD_AR)])
        RD_AR_crs.append([PAD_consistency,np.max(RD_AR)])
        DDP_AR_crs.append([DDP_consistency,np.max(DDP_AR)])
        RDP_AR_crs.append([RDP_consistency,np.max(RDP_AR)])
        PAD_AR_crs.append([PAD_consistency,np.max(PAD_AR)])
        print(DDP_AR_crs)
        print(RDP_AR_crs)
        print(PAD_AR_crs)



    AR_Name_list = ['DD', 'RD' , 'DDP', "RDP", "PAD"]
    AR_list_cr = [DD_AR_crs, RD_AR_crs,DDP_AR_crs,RDP_AR_crs, PAD_AR_crs]
    with open('Online bidding C_R tradeoff.txt',"w") as file:

        for index in range(len(AR_Name_list)):
            file.write('{0}cr = {1}\n'.format(AR_Name_list[index], AR_list_cr[index]))





if __name__ == '__main__':
    test_c_r_tradeoff()


