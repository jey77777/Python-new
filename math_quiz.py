import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERATOR = 3
MAX_OPERATOR = 15
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    right = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("-----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True: 
        guess = input(f"Problem # {str(i+1)}: {expr} = ")
        if guess == str(answer):
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("------------------------")
print(f"Nice work! You finished in {total_time} seconds")
