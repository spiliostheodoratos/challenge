import pandas as pd
import pytest

data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]

output=''

for i in data[0]:
    output=output+i+','
output=output+"BMI Category"+','+"BMI Range (kg/m2)"+","+"Health risk"
output=output+'\n'


def check_bmi(bmi):
    if bmi <= 18.4:
        return("Underweight","Malnutrition risk") 
    elif bmi >18.5 and bmi < 24.9:
        return("Normal weight","Low risk") 
    elif (bmi >25) and (bmi < 29.9):
        return("Overweight","Enhanced risk") 
    elif bmi >30 and bmi < 34.9:
        return("Moderately obese","Medium risk")
    elif bmi >35 and bmi < 39.9:
        return("Severely obese","High risk") 
    else:
        return("Very severely obese","Very high risk") 



     



for i in data:

    li=[]
    for x in i:
        li.append(str(data[data.index(i)][x]))
        output=output+str(data[data.index(i)][x])+','
    height_in_m=int(li[-2])*.01
    bmi=int(li[-1])/(height_in_m*height_in_m)
    cat,risk=check_bmi(bmi)
    output=output+cat+","+str(bmi)+","+risk
    
    output=output+'\n'

    
output=output.replace(',\n','\n')
#output = output[:-1]
#output = output[:-1]

#df = pd.DataFrame([x.split(',') for x in output.split('\n')])
#df['BMI']=1

#print(output)

def str2frame(estr, sep = ',', lineterm = '\n', set_header = True):
    dat = [x.split(sep) for x in estr.split(lineterm)][1:-1]
    cdf = pd.DataFrame(dat)
    if set_header:
        cdf = cdf.T.set_index(0, drop = True).T # flip, set ix, flip back
    return cdf


a=str2frame(output)

print(a)


def test_method():
    assert check_bmi(18.4)==("Underweight","Malnutrition risk")
    assert check_bmi(19.5)==("Normal weight","Low risk")
    assert check_bmi(26)==("Overweight","Enhanced risk")
    assert check_bmi(31)==("Moderately obese","Medium risk")
