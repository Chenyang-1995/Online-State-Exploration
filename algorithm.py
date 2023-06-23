
import numpy as np
import math



def a_delta(eps):
    delta = eps /2
    a1 = (1+eps)/(eps-delta)
    a2 = ((1+eps)*math.log(1+delta,math.e))/((1+eps)*math.log(1+delta,math.e)-delta)
    return a1,a2, delta


def a_delta_multi_cow_path(eps):
    delta = 0
    a = 2.0/eps+1
    return  a, delta


def doubling(target):
    guess_val = 1
    cost = guess_val
    while guess_val < target:
        guess_val = guess_val *2
        cost += guess_val

    AR = 1.0*cost / target

    return cost, AR

def deterministic_prediction(target,prediction,delta,a=2):
    relax_prediction = prediction*(1.0+delta)

    pred_iter = int(math.log(relax_prediction,a))

    guess_val = 1.0*relax_prediction / math.pow(a,pred_iter)
    cost = guess_val
    while guess_val < target:
        guess_val = guess_val *a
        cost += guess_val

    AR = 1.0*cost / target

    return cost, AR


def random_doubling(target):

    AR_list = []
    Cost_list = []
    len = 100
    for x in range(len):

        guess_val = math.pow(2,x*1.0/len)
        cost = guess_val

        while guess_val < target:
            guess_val = guess_val *2
            cost += guess_val

        AR = 1.0*cost / target
        AR_list.append(AR)
        Cost_list.append(cost)

    AR_mean = np.mean(np.array(AR_list))
    Cost_mean = np.mean(np.array(Cost_list))

    return Cost_mean,AR_mean


def randomized_prediction(target,prediction,delta,a=2):
    AR_list = []
    Cost_list = []
    theta = math.log(1+delta,a)
    len = 10
    for x in range(1,1+len):
        beta = 1.0*x*theta/len
        #print(math.pow(a,beta))
        relax_prediction = prediction*math.pow(a,beta)

        pred_iter = int(math.log(relax_prediction,a))

        guess_val = 1.0*relax_prediction / math.pow(a,pred_iter)
        cost = guess_val

        while guess_val < target:
            guess_val = guess_val *a
            cost += guess_val

        AR = 1.0*cost / target
        AR_list.append(AR)
        Cost_list.append(cost)

    AR_mean = np.mean(np.array(AR_list))
    Cost_mean = np.mean(np.array(Cost_list))

    return Cost_mean,AR_mean

def PAD(target, prediction, eps):
    t1 = prediction*eps/5.0
    t2 = prediction*(1+eps/5.0)
    guess_val = 1
    cost = guess_val
    while guess_val < t1:
        guess_val = guess_val*2
        cost+=guess_val
        if guess_val >= target:
            AR = 1.0*cost/target
            return cost, AR

    guess_val = t2
    cost += guess_val
    if guess_val >= target:
        AR = 1.0*cost/target
        return cost, AR
    while guess_val < target:
        guess_val = guess_val *2
        cost += guess_val

    AR = 1.0*cost/target
    return cost, AR



def deter_cow_path_with_prediction(target,prediction,delta,a=2):

    num_dim = len(target)
    target_value = max(target)
    target_dim = target.index(target_value)


    predicted_value = max(prediction)
    predicted_dim = prediction.index(predicted_value)


    relax_predicted_value = predicted_value*(1.0+delta)

    pred_iter = math.ceil(1.0*math.log(relax_predicted_value,a) / num_dim)


    guess_val = 1.0*relax_predicted_value / math.pow(a,pred_iter*num_dim)

    cost = 2*guess_val
    start_dim = predicted_dim
    while guess_val < target_value or start_dim != target_dim:

        guess_val = guess_val *a

        cost += 2*guess_val
        start_dim += 1
        start_dim = start_dim % num_dim

    cost -= 2*guess_val
    cost += target_value

    AR = 1.0*cost / target_value



    return cost, AR

def cow_path_traditional(target,a=2):

    num_dim = len(target)
    target_value = max(target)
    target_dim = target.index(target_value)

    guess_val = 1
    cost = 2*guess_val
    start_dim = 0
    while guess_val < target_value or start_dim != target_dim:

        guess_val = guess_val *a
        cost += 2*guess_val
        start_dim += 1
        start_dim = start_dim % num_dim

    cost -= 2*guess_val
    cost += target_value

    AR = 1.0*cost / target_value



    return cost, AR







