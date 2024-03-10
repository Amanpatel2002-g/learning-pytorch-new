import numpy as np

def gradient_descent(x, y):
    best_m = best_b = m_curr = b_curr = 0
    iterations = 100000
    n = len(x)
    learning_rate = 0.05
    minimum_cost = float("inf")
    with open("output.txt", "w") as file:
        for i in range(iterations):
            y_predicted = m_curr*x + b_curr
            cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
            if(minimum_cost>cost):
                minimum_cost = cost
                best_m = m_curr
                best_b = b_curr
            md = -(2/n)*sum(x*(y-y_predicted))
            bd = -(2/n)*sum(y-y_predicted)
            m_curr = m_curr - learning_rate*md
            b_curr = b_curr - learning_rate*bd
            file.write(f"\n m: {m_curr}, b: {b_curr}, cost: {cost}, iteration: {i}")
    
    print("completed ---------------------------------------------😁😁😁😁😁😁")
    print(f"minimum cost is {minimum_cost}")
    print(f"best m is {best_m}")
    print(f"best b is {best_b}")
    

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])
gradient_descent(x, y)
