import pandas as pd

data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

#To convert the input data in pandas dataframe
output=''

for i in data[0]:
    output=output+i+','
output=output+'\n'

for i in data:
    for x in i:
        output=output+str(data[data.index(i)][x])+','
    output=output+'\n'
    
output=output.replace(',\n','\n')
output = output[:-1]

df = pd.DataFrame([x.split(',') for x in output.split('\n')])

#To define the column of dataframe
df.columns =df.iloc[0]
df = df[1:]

#To add the new column BMI
df['BMI']=round((df['WeightKg'].astype(int))/(df['HeightCm'].astype(int)/100)**2,1)

def bmi_category(i):
    if i<=18.4:
        return 'Underweight'
    elif i>=18.5 and i<=24.9:
        return('Normal weight')
    elif i>=25 and i<=29.9:
        return('Overweight')
    elif i>=30 and i<=34.9:
        return('Moderately obese')
    elif i>=35 and i<=39.9:
        return('Severely obese')
    elif i>=40:
        return('Very severely obese')
    
def health_risk(i):
    if i<=18.4:
        return 'Malnutrition risk'
    elif i>=18.5 and i<=24.9:
        return('Low risk')
    elif i>=25 and i<=29.9:
        return('Enhanced risk')
    elif i>=30 and i<=34.9:
        return('Medium risk')
    elif i>=35 and i<=39.9:
        return('High risk')
    elif i>=40:
        return('Very high risk')

df['BMI category']=''   
df['Health risk']='' 

#To assign the value of columns BMI category and Health risk
var=1
for x in df['BMI']:
    df['BMI category'][var]=bmi_category(df['BMI'][var])
    df['Health risk'][var]=health_risk(df['BMI'][var])
    var=var+1

#To get the total number of overweight people
count_data = df.apply(lambda x: True if x['BMI'] >= 25 and x['BMI']<=29.9 else False , axis=1)
count = len(count_data[count_data == True].index)

print(df)

#To print the total number of overweight people is
print('The total number of overweight people is '+str(count))


