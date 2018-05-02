####

## Author : Dibya Prakash Das

####


import random


genes =        { "0" : "0000",
                 "1" : "0001",
                 "2" : "0010",
                 "3" : "0011",
                 "4" : "0100",
                 "5" : "0101",
                 "6" : "0110",
                 "7" : "0111",
                 "8" : "1000",
                 "9" : "1001",
                 "+" : "1010",
                 "-" : "1011",
                 "*" : "1100",
                 "/" : "1101"}

inverted = {genes[i]:i for i in genes}


gene_map = []
for i in enumerate(genes):
    gene_map.append(i)

def create_chromsome(genes=genes):
    chrsme = ""
    index = [random.randint(0,13) for i in range(7)]
    for i in index:
        chrsme += genes[gene_map[i][1]]
    return chrsme


def decoder(chromosome):
    genes = []
    for i in range(7):
        genes.append(chromosome[4*i:4*(i+1)])
    for i in range(len(genes)):
        try:
            genes[i] = inverted[genes[i]]
        except KeyError:
            genes[i] = "na"
    return genes


def sanitiser(dec_chr):
    copy_dec_chr = dec_chr.copy()
    flag = 0   # 0 for number and 1 for operator
    tobe = []
    for i in range(len(dec_chr)):
        if dec_chr[i] == 'na':
            tobe.append(i)
        try:
            int(dec_chr[i])
            if flag == 1:
                tobe.append(i)
            flag = 1
        except ValueError:  # means it's an operator
            if flag == 1:
                flag = 0 
                continue
            else:
                tobe.append(i)
    tobe.sort(reverse=True)
    for i in tobe:
        copy_dec_chr.pop(i)
    if copy_dec_chr[-1] in ["+","-","/","*","na"]:
        return copy_dec_chr[:-1]
    return copy_dec_chr


def evaluater(dec_chr):
    try:
        return eval("".join(sanitiser(dec_chr)))
    except ZeroDivisionError:
        return 0
    except Exception as e:
        return e
