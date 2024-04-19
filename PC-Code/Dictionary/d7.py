# Dict Comprehension

# ⭐ { Key: value for vars in iterable }
d1={i:i**2 for i in range(1,11)}
print(d1)

# using existing dict
distances = {'delhi':1000,'noorpur':400,'lucknow':10000}
d2={key:value*0.62 for (key,value) in distances.items()}
print(d2)

# using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

{i:j for (i,j) in zip(days,temp_C)}

# using if condition 
products={'phone':10,'laptop':0,'tablet':10}
d1={key:value for (key,value) in products.items() if value > 0}
print(d1)

# Nested Comprehension
# print tables of number from 2 to 4
d1={i:{j:i*j for j in range(1,11)} for i in range(2,5)}
print(d1)

# https://campusx1040.graphy.com/s/preview/courses/CampusX-Data-Science-Mentorship-Program#6376dbd8e4b065a4cadac4db
# https://colab.research.google.com/drive/1PtRoTO1A4HwZudf0ZqCq-sqiDpamVeyH?usp=sharing#scrollTo=Oka8jR26S1P3