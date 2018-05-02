####

## Author : Dibya Prakash Das

####

import random

def make_crossover(mating_pool, co_prob):
    for i in range(len(mating_pool)-1):
        if random.randint(0,99)/100 < co_prob:
            point_of_crossover = random.randint(1, len(mating_pool[i]))
            temp1 = mating_pool[i][:point_of_crossover] +  mating_pool[i+1][point_of_crossover:]
            mating_pool[i+1] = mating_pool[i+1][:point_of_crossover] +  mating_pool[i][point_of_crossover:]
            mating_pool[i] = temp1
    return mating_pool

def calc_cumulative(fitness):
    cumsum = []
    temp_sum = 0
    for i in fitness:
        temp_sum += i
        cumsum.append(temp_sum)
    return cumsum

def lessthan(x,cumulative_fitness):
    index = 0
    cumulative_fitness = [0] + cumulative_fitness
    for i in range(len(cumulative_fitness)):
        if x > cumulative_fitness[i] and x < cumulative_fitness[i+1]:
            return i

def count(corresponding,mating_pool):
    chrom_count = {i:0 for i in range(len(mating_pool))}
    for i in corresponding:
        chrom_count[i] += 1
    return [chrom_count[i] for i in range(len(mating_pool))]

def create_next_gen(corresponding, mating_pool):
    expected_count = count(corresponding, mating_pool)
    new_mating_pool = []
    for i in range(len(expected_count)):
        for j in range(expected_count[i]):
            new_mating_pool.append(mating_pool[i])
    random.shuffle(new_mating_pool)
    return new_mating_pool