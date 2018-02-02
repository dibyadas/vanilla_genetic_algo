
# coding: utf-8

# In[1]:

import random


# In[8]:

genes = { "0" : "0000",
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


# In[67]:

inverted = dict([[v,k] for k,v in genes.items()])


# In[19]:

gene_map = []
for i in enumerate(genes):
    gene_map.append(i)


# In[68]:

def create_chromsome(genes):
    chrsme = ""
    index = [random.randint(0,13) for i in range(7)]
    for i in index:
        chrsme += genes[gene_map[i][1]]
    return chrsme


# In[241]:

create_chromsome(genes)


# In[270]:

h = '0100110111010111101000111011'
len(h)


# In[284]:

h = h[:12]+"1"+h[13:]
h,len(h)


# In[285]:

decoder(h)


# In[289]:

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


# In[290]:

def sanitiser(dec_chr):
    copy_dec_chr = dec_chr.copy()
    flag = 0   # 0 for number and 1 for operator
    tobe = []
    for i in range(len(dec_chr)):
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


# In[291]:

y = decoder(h)
y


# In[292]:

sanitiser(y)


# In[288]:

def evaluater(dec_chr):
    return eval("".join(sanitiser(dec_chr)))


# In[293]:

evaluater(y)


# In[ ]:



