from openai import OpenAI
import os
import pandas as pd
from getpass import getpass

# ==========================================
# PITCHFORGE - STEP 4
# AI-POWERED CONTENT GENERATION
# ==========================================

# Ask for API key securely
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    api_key = getpass("Enter your OpenAI API key: ")

client = OpenAI(api_key=api_key)

# ==========================================
# Read PitchForge data from Step 3
# ==========================================

problem_df = pd.read_csv("problem_data.csv")
solution_df = pd.read_csv("solution_data.csv")

# Get problem and solution text
problem_text = " ".join(
    problem_df["Example Entry"].astype(str).tolist()
)

solution_text = " ".join(
    solution_df["Example Entry"].astype(str).tolist()
)

# ==========================================
# Generate Problem Summary
# ==========================================

problem_response = client.responses.create(
    model="gpt-6-luna",
    instructions="""
    You are a startup pitch-deck consultant.
    Convert the startup problem into ONE concise,
    investor-friendly sentence.

    Rules:
    - Maximum 25 words
    - Clear and professional
    - Preserve the original meaning
    - Do not invent statistics
    - Do not invent customers or traction
    """,
    input=f"Startup problem:\n{problem_text}"
)

problem_summary = problem_response.output_text.strip()


# ==========================================
# Generate Solution Summary
# ==========================================

solution_response = client.responses.create(
    model="gpt-6-luna",
    instructions="""
    You are a startup pitch-deck consultant.
    Convert the startup solution into ONE concise,
    investor-friendly sentence.

    Rules:
    - Maximum 25 words
    - Clear and professional
    - Explain what the startup provides
    - Preserve the original meaning
    - Do not invent features, customers or results
    """,
    input=f"Startup solution:\n{solution_text}"
)

solution_summary = solution_response.output_text.strip()


# ==========================================
# Display Results
# ==========================================

print("\n==========================================")
print("       PITCHFORGE AI CONTENT GENERATOR")
print("==========================================")

print("\nORIGINAL PROBLEM:")
print(problem_text)

print("\nAI-GENERATED PROBLEM SUMMARY:")
print(problem_summary)

print("\nORIGINAL SOLUTION:")
print(solution_text)

print("\nAI-GENERATED SOLUTION SUMMARY:")
print(solution_summary)


# ==========================================
# Save AI-generated content
# ==========================================

output_data = pd.DataFrame({
    "Section": ["Problem", "Solution"],
    "Original_Content": [problem_text, solution_text],
    "AI_Summary": [problem_summary, solution_summary]
})

output_data.to_csv(
    "AI_Generated_Pitch_Content.csv",
    index=False
)

print("\n==========================================")
print("AI content generation completed!")
print("==========================================")
print("\nCreated file:")
print("AI_Generated_Pitch_Content.csv")