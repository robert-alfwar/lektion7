# 1
import math
import cmath

# 2
print('#2')
print(math.sin(1))
print(cmath.sin(1))

# 3
print('#3')
print(f'{type(math.sin(1))} {math.sin(1)}')
print(f'{type(cmath.sin(1))} {cmath.sin(1)}')

# 4
from math import sin
from cmath import sin

# 5
print('#5')
print(f'{type(sin(1))} {sin(1)}')

# 6
print('#6')
from cmath import sin
from math import sin

print(f'{type(sin(1))} {sin(1)}')
# namespace conflict: 2nd import overwrites the first.

# 7
from math import sin
from cmath import sin as csin

# 8
print('#8')
print(f'{type(sin(1))} {sin(1)}')
print(f'{type(csin(1))} {csin(1)}')