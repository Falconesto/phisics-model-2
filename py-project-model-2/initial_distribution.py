import numpy as num
from input import Input


def get():
    result = [Input.U_0]
    n = int(Input.LENGTH / Input.DELTA_X)
    for i in range(1, n):
        current_x = i * Input.DELTA_X
        result.append(0.25*current_x*current_x - 1)

    result.append(Input.U_LENGTH)
    return result
