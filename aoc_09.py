import numpy as np
from scipy.ndimage import label

input_array = np.array([list(line) for line in open("Data/aoc_09.txt").read().splitlines()]).astype(int)

right = np.where(input_array-np.roll(input_array,1,axis=1)<0,True,False)
right[:,0] = True
left = np.where(input_array-np.roll(input_array,-1,axis=1)<0,True,False)
left[:,-1] = True
up = np.where(input_array-np.roll(input_array,-1,axis=0)<0,True,False)
up[-1,:] = True
down = np.where(input_array-np.roll(input_array,1,axis=0)<0,True,False)
down[0,:] = True

print(f"Answer 1: {sum(input_array[right&left&up&down]+1)}")

#using scipy.ndimage
basin_array_size_counts = np.sort(np.unique((label(np.where(input_array != 9, 1, 0))[0]),return_counts=True)[1])
print(f"Answer 2: {basin_array_size_counts[-2]*basin_array_size_counts[-3]*basin_array_size_counts[-4]}")

