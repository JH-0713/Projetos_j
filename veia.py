from random import randint
lj = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
def marcar_p_x(esc1):
    if esc1 == '1':
        lj.pop(0)
        lj.insert(0, '❌')
    elif esc1 == '2':
        lj.pop(1)
        lj.insert(1, '❌')
    elif esc1 == '3':
        lj.pop(2)
        lj.insert(2, '❌')
    elif esc1 == '4':
        lj.pop(3)
        lj.insert(3, '❌')
    elif esc1 == '5':
        lj.pop(4)
        lj.insert(4, '❌')
    elif esc1 == '6':
        lj.pop(5)
        lj.insert(5, '❌')
    elif esc1 == '7':
        lj.pop(6)
        lj.insert(6, '❌')
    elif esc1 == '8':
        lj.pop(7)
        lj.insert(7, '❌')
    elif esc1 == '9':
        lj.pop(8)
        lj.insert(8, '❌')

def marcar_c_x(escr1):
    if escr1 == '❌' or escr1 == '⭕':
        escr1 = str(randint(1, 9))
    elif escr1 == '1':
        lj.pop(0)
        lj.insert(0, '⭕')
    elif escr1 == '2':
        lj.pop(1)
        lj.insert(1, '⭕')
    elif escr1 == '3':
        lj.pop(2)
        lj.insert(2,'⭕')
    elif escr1 == '4':
        lj.pop(3)
        lj.insert(3,'⭕')
    elif escr1 == '5':
        lj.pop(4)
        lj.insert(4,'⭕')
    elif escr1 == '6':
        lj.pop(5)
        lj.insert(5,'⭕')
    elif escr1 == '7':
        lj.pop(6)
        lj.insert(6,'⭕')
    elif escr1 == '8':
        lj.pop(7)
        lj.insert(7,'⭕')
    elif escr1 == '9':
        lj.pop(8)
        lj.insert(8,'⭕')