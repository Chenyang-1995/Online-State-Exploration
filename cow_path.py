
import algorithm as alg
import numpy as np




def test_c_r_tradeoff_for_cow_path():


    max_value = 1000
    instance_set = [(i,j) for i in range(1,max_value+1) for j in range(1,max_value+1)]
    dims = [2,4,6,8,10]



    DDP_AR_crs = [[] for _ in dims]

    epss = np.arange(2,24,2)
    print('epss = {}'.format(epss))


    for eps in epss:
        consistent = 1+eps
        a, delta = alg.a_delta_multi_cow_path(eps)


        print('a = {0}, delta = {1}, consistency = {2} eps = {3}'.format(a,delta,consistent,eps))



        DDP_AR = [[] for dim in dims ]


        for dim_index, dim in enumerate(dims):
            for target_dim in range(dim):

                for i,instance_prediction in enumerate(instance_set):
                    instance = [0 for _ in range(dim)]
                    instance[target_dim] = instance_prediction[0]
                    prediction = [0 for _ in range(dim)]
                    prediction[0]=instance_prediction[1]

                    _, AR = alg.deter_cow_path_with_prediction(instance,prediction,delta,a)
                    DDP_AR[dim_index].append(AR)


            DDP_AR_crs[dim_index].append(max(DDP_AR[dim_index])) #(math.log(max(DDP_AR[dim_index]),2))
            print('eps = {2}, dim = {0}, robust = {1}'.format(dim, DDP_AR_crs[dim_index][-1],eps))






    AR_Name_list = ['DDP_{}'.format(dim) for dim in dims]
    AR_list_cr = DDP_AR_crs
    with open('Cow path C_R tradeoff.txt',"w") as file:
        for index in range(len(AR_Name_list)):
            file.write('{0}_cr = {1}\n'.format(AR_Name_list[index], AR_list_cr[index]))



if __name__ == '__main__':
    test_c_r_tradeoff_for_cow_path()


