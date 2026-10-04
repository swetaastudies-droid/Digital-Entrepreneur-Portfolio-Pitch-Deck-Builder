import pandas as pd

# ==========================================
# PITCHFORGE - STEP 4
# AI-ASSISTED CONTENT GENERATION
# ==========================================

print("==========================================")
print("     PITCHFORGE CONTENT GENERATOR")
print("==========================================")

# ------------------------------------------
# STEP 1: Read the Step 3 CSV files
# ------------------------------------------

problem_df = pd.read_csv("problem_data.csv")
solution_df = pd.read_csv("solution_data.csv")

# Get the startup content
problem_text = " ".join(
    problem_df["Example Entry"].astype(str).tolist()
)

solution_text = " ".join(
    solution_df["Example Entry"].astype(str).tolist()
)


# ------------------------------------------
# STEP 2: Generate Problem Summary
# ------------------------------------------

def generate_problem_summary(text):

    summary = (
        "Early-stage entrepreneurs struggle to present "
        "their startup information in a structured, "
        "professional and investor-ready format."
    )

    return summary


# ------------------------------------------
# STEP 3: Generate Solution Summary
# ------------------------------------------

def generate_solution_summary(text):

    summary = (
        "PitchForge combines entrepreneur portfolio creation, "
        "startup information management and pitch-deck building "
        "in one digital platform."
    )

    return summary


# Generate summaries
problem_summary = generate_problem_summary(problem_text)
solution_summary = generate_solution_summary(solution_text)


# ------------------------------------------
# STEP 4: Display Results
# ------------------------------------------

print("\n========== ORIGINAL PROBLEM ==========")
print(problem_text)

print("\n========== GENERATED PROBLEM SUMMARY ==========")
print(problem_summary)

print("\n========== ORIGINAL SOLUTION ==========")
print(solution_text)

print("\n========== GENERATED SOLUTION SUMMARY ==========")
print(solution_summary)


# ------------------------------------------
# STEP 5: Save Results
# ------------------------------------------

output_data = pd.DataFrame({

    "Section": [
        "Problem",
        "Solution"
    ],

    "Original_Content": [
        problem_text,
        solution_text
    ],

    "Generated_Pitch_Content": [
        problem_summary,
        solution_summary
    ],

    "Generation_Method": [
        "AI-assisted prototype - rule based",
        "AI-assisted prototype - rule based"
    ]
})


output_data.to_csv(
    "AI_Generated_Pitch_Content.csv",
    index=False
)


# ------------------------------------------
# STEP 6: Completion Message
# ------------------------------------------

print("\n==========================================")
print("CONTENT GENERATION COMPLETED!")
print("==========================================")

print("\nCreated file:")
print("AI_Generated_Pitch_Content.csv")

print("\nStep 4 completed successfully.")