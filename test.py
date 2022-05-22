import os
os.system("cls")

from random import randint as rnt

from matplotlib import pyplot as plt

from app import get_all_readings
from app.models import Jar, Plant


plant = Plant.query.get(8)

p = plant.plant_data()

print(p[0])

print('\n')

j = get_all_readings()

print(j[0])

# fig = plt.figure()

# ax_1 = fig.add_subplot(1, 1, 1)
# ax_1.set_title('Temperatura')

# ax_1.plot([ i for i in range( j[0] + 1 ) ], 'r--', label='Jar Data')
# ax_1.plot([ x for x in range( p[0] + 1 ) ], 'b-', label='Plant Data')
# ax_1.legend(loc='best')


# x = [ rnt(1, j[0] + 1) for _ in range(20) ]
# y = [ rnt(1, p[0] + 1) for _ in range(20) ]


# plt.plot(x, y, 'b-', label='Temperature')


# plt.hist([1,2,3], [1,2,3], 'bar', color='red')

plt.title('Temperatura')
plt.legend(loc='best')

plt.hist([0, j[0]], density=True, histtype='bar', color='blue', orientation='horizontal', label='Jar')
plt.hist([0, p[0]], density=True, histtype='bar', color='red', orientation='horizontal', label='Plant')


plt.show()









#region query to_dict()

# from app import app

# from app.models import Plant

# plants = Plant.query.all()

# for p in plants:

#     pl = vars(p)

#     pl.pop('_sa_instance_state')

#     print(pl)

#endregion

