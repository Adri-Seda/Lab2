'''
Adriana Seda Pagan

8/31/2023

This Program calculates your age in dog, cat and horse years.
'''

'''this is the dog age converter'''
#initialize variables with default values

human_age = 0.0
month_constant = 12
day_constant = 365.25/12

#grabbing input from the user and converting human age to dog age

human_age = (float(input('Enter your age: ')))
dog_age_conversion = human_age * 7

#converting decimal dog age into year month day format by grabbing decimal and multiplying by appropiate constant
dog_year = int(dog_age_conversion)
dog_month = int((dog_age_conversion % 1) * month_constant)
dog_day = int((dog_age_conversion * month_constant) % 1 * day_constant)


#printing result of calculation to console

print(f'An age {human_age} human should be {dog_year} years {dog_month} months {dog_day} days in dog age')



'''this is the cat age converter'''



#initialize variables with default values

human_age = 0.0
month_constant = 12
day_constant = 365.25/12

#grabbing input from the user and converting human age to cat age

human_age = (float(input('Enter your age: ')))
cat_age_conversion = human_age / 9

#converting decimal cat age into year month day format by grabbing decimal and multiplying by appropiate constant
cat_year = int(cat_age_conversion)
cat_month = int((cat_age_conversion % 1) * month_constant)
cat_day = int((cat_age_conversion * month_constant) % 1 * day_constant)


#printing result of calculation to console

print(f'An age {human_age} human should be {cat_year} years {cat_month} months {cat_day} days in cat age')



'''this is the horse age converter'''



#initialize variables with default values

human_age = 0.0
month_constant = 12
day_constant = 365.25/12

#grabbing input from the user and converting human age to horse age

human_age = (float(input('Enter your age: ')))
horse_age_conversion = 3 * ((((human_age ** 2) - 47) / 7) + 12)

#converting decimal horse age into year month day format by grabbing decimal and multiplying by appropiate constant

horse_year = int(horse_age_conversion)
horse_month = int((horse_age_conversion % 1) * month_constant)
horse_day = int((horse_age_conversion * month_constant) % 1 * day_constant)


#printing result of calculation to console

print(f'An age {human_age} human should be {horse_year} years {horse_month} months {horse_day} days in horse age')








