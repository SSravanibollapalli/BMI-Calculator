height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

int_weight = int(weight)
int_height = float(height)
bmi = ((int_weight) / (int_height ** 2))
print(int(bmi))