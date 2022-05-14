#BMI Calculate حساب كتلة قياس كتلة الجسم
# اول سطرين عبارة عن انه اخد مني بينات الطول بدون ما يطبعها (Input
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
# BMI Equation معادلة ال مؤشر كتلة الجسم
BMI = weight / (height/100)**2
#Depends of the result of the equation i make output that tells me if my weight is healty, underweight? ..etc
#بناء على ناتج المعادلة سيتم طباعة المخرج باخباري اذا كان وزني مناسباً ام اقل من الوزن الطبيعي ... الخ
if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
elif BMI <= 34.9:
    print("You are severely over weight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")
# A7 Code