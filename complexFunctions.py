"""
Created on Wed Mar 20 19:35:11 2019

@author: spopoff
"""

from torch.nn.functional import relu, max_pool2d



def complex_relu(input_r,input_i):
#    assert(input_r.size() == input_i.size())
    return relu(input_r), relu(input_i)

def complex_max_pool(input_r,input_i,kernel_size, stride, padding,
                                dilation, ceil_mode, return_indices):
    return max_pool2d(input_r, kernel_size, stride, padding, dilation, 
                      ceil_mode, return_indices), \
           max_pool2d(input_i, kernel_size, stride, padding, dilation, 
                      ceil_mode, return_indices)
