from liss import liss
from linear import *
from os.path import join, abspath

# liss(1, 9, './images')
# ar = sheet_to_array(join('..', 'data', 'line.xlsx'))
# print(ar)
# save_pict(join('..', 'data', 'line.xlsx'), 'images/line.png')
D = sheet_to_array(join('..', 'data', 'line.xlsx'))
D1, A = kill_extend(D)
a, b = ab(D1)
save_pict(D, 'images/line1.png', a=a, b=b)
save_pict(D1, 'images/line2.png', a=a, b=b, add_points=A)