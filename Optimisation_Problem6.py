#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:21:39 2024

@author: manishathakur
"""

import numpy as np
from pyomo.environ import *
import pandas as pd

file_name='AssignmentTemplate-4.xlsx'

df = pd.read_excel("AssignmentTemplate-4.xlsx", "Problem6", index_col=0) 

ing_names = df.loc[df.index[0:-1], df.columns[0]].keys()
print(ing_names)

df_np = df.to_numpy()

supplies = df_np[0:-1,-1]
print(supplies)

ratio = df_np[0:-1,0]
print(ratio)

ing_length = len(ing_names)
suppliesno = len(supplies)
ratio_length = len(ratio)



cost = df_np[0:,2:-1]
print(cost)

mixture = df_np[-1,0]
print(mixture)

model = ConcreteModel()

model.ing = Var(range(ing_length), domain=NonNegativeReals)

def objective_rule(model):
    return sum(cost[i] * model.ing[i] for i in range(ing_length))

model.cost = Objective(rule=objective_rule, sense=minimize)

def supply_rule(model,i):
    return (model.ing[i] <= supplies[i])

model.supplyCons = Constraint(range(suppliesno), rule=supply_rule)

total_mix = sum(model.ing[i] for i in range(ing_length))

def ratio_rule(model, i):    
    return model.ing[i] >=  total_mix * ratio[i]

model.ratioCons = Constraint(range(ratio_length), rule=ratio_rule)


# Minimum total mix constraint
def total_mix_rule(model):
    return sum(model.ing[i] for i in range(ing_length)) >= mixture

model.totalMix = Constraint(rule=total_mix_rule)

# Solve the model
solver = SolverFactory('glpk')
results = solver.solve(model, tee=True)

# Check if the solution is optimal
if results.solver.termination_condition == TerminationCondition.optimal:
    print("Optimal solution found!")
    for i in range(ing_length):
        print(f"{ing_names[i]}: {model.ing[i].value} kg")
    print(f"Total Cost: £{model.cost()}")
else:
    print("Solve failed or no optimal solution found.")
































