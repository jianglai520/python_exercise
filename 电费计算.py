#电费计算

def calculate(power, cost):
    if power <= 0:
        return "Invalid Value"
    elif 0 < power <= 50:
        cost = power * 0.53
        return cost
    else:
        if type(power - 50) == int:
            cost = 0.53 * 50
            for i in range(power - 50):
                cost += 0.53 
                
            return cost

print(calculate(100, 0))

