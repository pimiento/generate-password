# -*- coding: utf-8 -*-
#------------------------------------------------------------
# генератор словарей
#------------------------------------------------------------

from gen_dict import gen_dict_fsmb
from gen_dict import gen_dict_othsmb
from gen_dict import gen_dict_exc
from gen_dict import gen_dict_one_s
import random

sfile = '/home/mak/devel/scripts/old_work/gen_pass/pereraboka.txt'
dict_first = gen_dict_fsmb(sfile)
dict_sec = gen_dict_othsmb(sfile)
dict_ran = gen_dict_exc(sfile)

def gen_pass(dict_f, dict_s, dict_r, dict_o, len_pass):
    """generate password
    
    Arguments:
    - `dict_f`: dictionary first two symbols
    - `dict_s`: dictionary all other symbols
    - `dict_r`: dictionary all other random symbols
    - `dict_o`: dictionary alone symbols    
    - `len_pass`: lenth of pass
    """
    # password = ''
    list_f = []
    for k, v in dict_f.items():
        for p in range(v):
            list_f.append(k)
    f_st = random.sample(list_f, 1)[0]
    list_s = []
    list_r = []
    pr_st = f_st
    # генерация списка для несуществующих в словаре комбинаций символов
    for k3, v3 in dict_r.items():
        for p3 in range(v3):
            list_r.append(k3)
    itr = 0
    for k, v in dict_s.items():
        if itr < len_pass: # ограничиваем длину пароля
            if k == pr_st:
                for k2, v2 in v.items():
                    for p in range(v2):
                        list_s.append(p)
                f_st = f_st + random.sample(list_s, 1)[0]
                pr_st = f_st[-1:]
                list_s = []
            elif k[-1:] == pr_st[-1:]:
                first_smb = f_st[-1:]
                print 'first smb %s' % first_smb
                sec_smb = random.sample(list_r, 1)[0]
                while first_smb == sec_smb:
                    sec_smb = random.sample(list_r, 1)[0]
                    
            else:
                first_smb = f_st[-1:]
                print 'first smb %s' % first_smb
                sec_smb = random.sample(list_r, 1)[0]
                while first_smb == sec_smb:
                    sec_smb = random.sample(list_r, 1)[0]
                f_st = f_st + sec_smb
                pr_st = f_st[-2:]
            itr +=1
        else:
            break
    print f_st
    
gen_pass(dict_first, dict_sec, dict_ran, 10)
    
