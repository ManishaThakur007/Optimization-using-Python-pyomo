##Optimal Feed Mix Optimization with Pyomo
**Overview**
This project uses linear programming to solve a real-world feed mix optimization problem for a fictional company, X Feed Company. The objective is to minimize the cost of producing an animal feed mixture that satisfies multiple ingredient ratio constraints and supply limits.

**Problem Statement**
The X Feed Company makes a feed from four ingredients:

Oats (max 300 kg, £0.90/kg)

Corn (max 400 kg, £1.00/kg)

Soybeans (max 200 kg, £0.50/kg)

Vitamin supplement (max 400 kg, £1.70/kg)

Subject to:

At least 30% of the mix must be soybeans

Corn to oats ratio must not exceed 4:1

At least 15% of the mix must be vitamin supplement

The total mix must be at least 665 kg

✅ Objective
Minimize the total cost of the feed mix while satisfying the constraints above.

🛠️ Tools Used
Python 3

Pyomo (Python Optimization Modeling Objects)

GLPK (GNU Linear Programming Kit)

Pandas and NumPy for data handling

Microsoft Excel as input format

📁 Files
AssignmentTemplate-4.xlsx: Contains the input data for ingredient names, costs, supply limits, ratios, and minimum mix requirement.

feed_mix_optimizer.py: Python script to model and solve the optimization problem using Pyomo.

▶️ How to Run
Install the required packages:

bash
Copy
Edit
pip install pyomo pandas numpy openpyxl
Install GLPK solver:

On macOS: brew install glpk

On Ubuntu: sudo apt-get install glpk-utils

Or download from GLPK official site

Run the script:

bash
Copy
Edit
python feed_mix_optimizer.py
📈 Output
If an optimal solution is found, the script prints:

Quantity (kg) of each ingredient to use

Total cost of the optimized mix

💡 Example Output
yaml
Copy
Edit
Optimal solution found!
Oats: 90.0 kg
Corn: 360.0 kg
Soybeans: 199.5 kg
Vitamin supplement: 100.0 kg
Total Cost: £970.15
🧠 Learning Outcomes
Formulating real-world problems as linear programming models

Using Pyomo for optimization in Python

Integrating data from Excel into a Pyomo model

Solving LPs with open-source solvers like GLPK

📜 License
This project is for educational and demonstration purposes. Feel free to adapt it for your own use.
