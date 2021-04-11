
import re


def unroll(line_, variable, number, flag_=True):

    line = line_ 


    indexs_plus = [m.end() for m in re.finditer(variable + '\+', line)]
    indexs_minus = [m.end() for m in re.finditer(variable + '-', line)]

   
    line = list(line)
    lines = [line[:] for _ in range(number)]

    result = []
    for i, line in enumerate(lines):
        
        flag = 1
        if flag_ is False:
            flag = -1

        for index in indexs_plus:
            res_t = int(line[index]) + i * flag
            line[index] = res_t
            if res_t < 0:
                line[index - 1] = ""

        for index in indexs_minus:
            res_t = -int(line[index]) + i * flag
            line[index] = res_t
            if res_t >= 0:
                line[index - 1] = "+"
            else:
                line[index - 1] = ""
       
        result.append("".join(str(e) for e in line) + "\n")

  
    return "".join(str(e) for e in result)
