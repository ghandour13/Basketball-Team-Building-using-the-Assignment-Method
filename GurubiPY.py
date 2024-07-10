import gurobipy as gp

# Create a new model
m = gp.Model()

# Create variables
g1 = m.addVar(vtype='B', name="Trae Young")
g2 = m.addVar(vtype='B', name="Jrue Holiday")
g3 = m.addVar(vtype='B', name="Stephen Curry")
g4 = m.addVar(vtype='B', name="Russell Westbrook")
g5 = m.addVar(vtype='B', name="LaMelo Ball")
g6 = m.addVar(vtype='B', name="Luka Doncic")
g7 = m.addVar(vtype='B', name="Alex Caruso")
g8 = m.addVar(vtype='B', name="Josh Hart")
g9 = m.addVar(vtype='B', name="Marcus Smart")
g10 = m.addVar(vtype='B', name="Shai")
f1 = m.addVar(vtype='B', name="Lebron James")
f2 = m.addVar(vtype='B', name="Carmelo Anthony")
f3 = m.addVar(vtype='B', name="Giannis Antetokoumpo")
f4 = m.addVar(vtype='B', name="Jayson Tatum")
f5 = m.addVar(vtype='B', name="Pascal Siakam")
f6 = m.addVar(vtype='B', name="PJ Tucker")
f7 = m.addVar(vtype='B', name="OJ Anunoby")
f8 = m.addVar(vtype='B', name="Jaylen Brown")
f9 = m.addVar(vtype='B', name="Gordon Hayward")
f10 = m.addVar(vtype='B', name="Larry Nance")
c1 = m.addVar(vtype='B', name="Brook Lopez")
c2 = m.addVar(vtype='B', name="Rudy Gobert")
c3 = m.addVar(vtype='B', name="Karl Anthony Towns")
c4 = m.addVar(vtype='B', name="Myles Turner")

playmaking = (94.00*g1 + 87.00*g2 + 93.00*g3 + 95.00*g4 + 90.00*g5 + 99.00*g6 + 84.00*g7 + 72.00*g8 + 84.00*g9 + 91.00*g10 +
              97.00*f1 + 23.00*f2 + 92.00*f3 + 82.00*f4 + 80.00*f5 + 45.00*f6 + 68.00*f7 + 74.00*f8 + 73.00*f9 + 56.00*f10 +
              10.00*c1 + 18.00*c2 + 43.00*c3 + 20.00*c4)/5

defense =  (25.00*g1 + 95.00*g2 + 84.00*g3 + 92.00*g4 + 45.00*g5 + 48.00*g6 + 87.00*g7 + 81.00*g8 + 94.00*g9 + 70.00*g10 +
            90.00*f1 + 23.00*f2 + 99.00*f3 + 90.00*f4 + 81.00*f5 + 89.00*f6 + 89.00*f7 + 84.00*f8 + 74.00*f9 + 76.00*f10 +
            89.00*c1 + 99.00*c2 + 80.00*c3 + 92.00*c4)/5

scoring =  (90.00*g1 + 83.00*g2 + 95.00*g3 + 87.00*g4 + 81.00*g5 + 95.00*g6 + 57.00*g7 + 64.00*g8 + 70.00*g9 + 89.00*g10 +
            99.00*f1 + 73.00*f2 + 99.00*f3 + 93.00*f4 + 82.00*f5 + 22.00*f6 + 55.00*f7 + 85.00*f8 + 73.00*f9 + 66.00*f10 +
            57.00*c1 + 27.00*c2 + 90.00*c3 + 59.00*c4)/5

shooting = (96.00*g1 + 84.00*g2 + 99.00*g3 + 57.00*g4 + 75.00*g5 + 95.00*g6 + 76.00*g7 + 82.00*g8 + 79.00*g9 + 84.00*g10 +
            88.00*f1 + 89.00*f2 + 70.00*f3 + 92.00*f4 + 70.00*f5 + 83.00*f6 + 80.00*f7 + 84.00*f8 + 75.00*f9 + 69.00*f10 +
            84.00*c1 + 23.00*c2 + 92.00*c3 + 80.00*c4)/5

salary =   (24.00*g1 + 25.11*g2 + 45.78*g3 + 47.06*g4 + 08.20*g5 + 30.20*g6 + 09.20*g7 + 06.00*g8 + 13.80*g9 + 05.40*g10 +
            41.20*f1 + 02.64*f2 + 39.30*f3 + 28.10*f4 + 33.00*f5 + 07.00*f6 + 16.07*f7 + 26.70*f8 + 32.70*f9 + 10.60*f10 +
            12.70*c1 + 26.53*c2 + 31.65*c3 + 18.00*c4)

# Set objective function to maximize:

m.setObjective(playmaking + defense + scoring + shooting, gp.GRB.MAXIMIZE)      # Overall Rating

#m.setObjective(playmaking , gp.GRB.MAXIMIZE)                                   # Playmaking
#m.setObjective(defense , gp.GRB.MAXIMIZE)                                      # Defense
#m.setObjective(scoring , gp.GRB.MAXIMIZE)                                      # Scoring
#m.setObjective(shooting , gp.GRB.MAXIMIZE)                                     # Shooting

# User Input

print(f"Please enter the RHS Constraint for:\n")

#playmaking_input = int(input("Playmaking: "))
#defense_input = int(input("Defense: "))
#scoring_input = int(input("Scoring: "))
#shooting_input = int(input("Shooting: "))
salary_input = int(input("Salary: "))

# Add constraints

m.addConstr(g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 +
            f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 +
            c1 + c2 + c3 + c4 == 5)                                     # starting 5

m.addConstr(c1 + c2 + c3 + c4 <= 1)                                     # centers

m.addConstr(g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 <= 2)      # guards

m.addConstr(f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 <= 2)      # forwards

m.addConstr(salary <= salary_input)                                     # salary

# We add a greater than or equal constraints for playmaking, defense, scoring, and shooting.
# The below code are used in case of maximizing a specific skill and not overall rating.

#m.addConstr(playmaking >= 70)     # playmaking
#m.addConstr(defense >= 70)           # defense
#m.addConstr(scoring >= 70)           # scoring
#m.addConstr(shooting >= 70)         # shooting

# Solve it!
m.optimize()

print("\n")

print(f"Your Most Optimal Starting Lineup:\n")
for v in m.getVars():
    if v.X == 1:
        print(v.VarName)

print(f"\n")
print(f"Team Salary: {int(salary.getValue())} million  \n")

#print(f"Team Ratings:\n")

#print(f"Playmaking Rating: {int(playmaking.getValue())}\n")
#print(f"Defense Rating: {int(defense.getValue())}\n")
#print(f"Scoring Rating: {int(scoring.getValue())} \n")
#print(f"Shooting Rating: {int(shooting.getValue())}\n")
print(f"Overall Rating: {int((playmaking.getValue() + defense.getValue() + scoring.getValue() + shooting.getValue())/4)}\n")

