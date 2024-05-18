from scipy.optimize import fsolve

def equations(vars):
    E, En, P = vars
    eq1 = E - (71250000 + 0.125*En + 0.1*P)
    eq2 = En - (40750000 + 0.1*E + 0.05*P)
    eq3 = P - (20000000 + 0.0625*En)
    return [eq1, eq2, eq3]

# Initial guess for E, En, P
initial_guess = [0, 0, 0]

# Solve the system of equations
E, En, P = fsolve(equations, initial_guess)

print("E =", E)
print("En =", En)
print("P =", P)

final = 71250000 + 0.125*49885641.6772554 + 0.1*23117852.604828462
print(final)