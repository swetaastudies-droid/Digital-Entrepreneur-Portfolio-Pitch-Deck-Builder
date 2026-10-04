import pandas as pd

# ==========================================
# PITCHFORGE - STEP 3
# Data Processing & Organization
# ==========================================

# Excel file created in Step 2
input_file = "PitchForge_Step_2_Data_Collection.xlsx"

# Read the Startup_Data sheet
df = pd.read_excel(input_file, sheet_name="Startup_Data")

print("\nOriginal Data:")
print(df)

# ==========================================
# Organize data into required sections
# ==========================================

profile = df[df["Section"] == "Profile"]
problem = df[df["Section"] == "Problem"]
solution = df[df["Section"] == "Solution"]
market = df[df["Section"] == "Target Market"]
financials = df[df["Section"] == "Business Model"]

# ==========================================
# Display the sections
# ==========================================

print("\n========== PROFILE ==========")
print(profile)

print("\n========== PROBLEM ==========")
print(problem)

print("\n========== SOLUTION ==========")
print(solution)

print("\n========== MARKET ==========")
print(market)

print("\n========== FINANCIALS ==========")
print(financials)

# ==========================================
# Save each section as a separate CSV file
# ==========================================

profile.to_csv("profile_data.csv", index=False)
problem.to_csv("problem_data.csv", index=False)
solution.to_csv("solution_data.csv", index=False)
market.to_csv("market_data.csv", index=False)
financials.to_csv("financials_data.csv", index=False)

print("\n======================================")
print("PitchForge data organization completed!")
print("======================================")

print("\nCreated files:")
print("1. profile_data.csv")
print("2. problem_data.csv")
print("3. solution_data.csv")
print("4. market_data.csv")
print("5. financials_data.csv")