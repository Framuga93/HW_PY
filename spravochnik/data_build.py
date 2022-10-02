from random import randint

m_f_name = ['Kirill', 'Aleksey', 'Danila', 'Igor', 'Vasya', ]
w_f_name = [ 'Anna', 'Olga','Masha','Marina', 'Svetlana']
m_s_name = ['Ivanov','Stepanov','Alekseev','Petrov']
w_s_name = ['Ivanova','Stepanova','Alekseeva','Petrova']
index_f_m_name = randint(0, len(m_f_name) - 1)
index_f_w_name = randint(0, len(m_f_name) - 1)
index_s_m_name = randint(0, len(m_s_name) - 1)
index_s_w_name = randint(0, len(w_s_name) - 1)
def get_firstname(n,i):
    k = n[i]
    return k

def get_secondname(n,i):
    k = n[i]
    return k

m_or_w = randint(0,1)

def bio(s):
    if s ==0:return get_firstname(m_f_name,index_f_m_name),get_secondname(m_s_name,index_s_m_name)
    else: return get_firstname(w_f_name,index_f_w_name), get_secondname(w_s_name,index_s_w_name)

print(bio(m_or_w))