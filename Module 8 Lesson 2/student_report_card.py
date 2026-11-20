import pandas as pd

print("=" * 60)
print("        STUDENT REPORT CARD ANYLYSIS")
print("=" * 60)


data = {
    "Name": [
        "Aarav", "Aarohi", "Aditya", "Anunya", "Krishav", "Matthew", "Ryan", "Camden", "William", "Ethan"

    ],
    "Maths": [85, 92, 78, 88, 95, 80, 70, 90, 75, 82],

    "Sciences": [90, 88, 85, 92, 80, 75, 95, 78, 82, 88],

    "English": [78, 85, 92, 80, 88, 90, 75, 82, 95, 88],

    "History": [88, 90, 85, 92, 80, 75, 95, 78, 82, 88],
}

df = pd.DataFrame(data)

print("\n Totals and Averages")
df["Total"] = df[["Maths", "Sciences", "English", "History"]].sum(axis=1)
df["Average"] = df["Total"]/4

def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average"].apply(assign_grade)

subjects = ["Maths", "Sciences", "English", "History"]
df["Passed_All"] = df[subjects].min(axis=1) >= 40
df["Status"] = df["Passed_All"].map({True: "Pass", False: "Fail"})

print("\n Class Report Card")
print("-" * 60)
display_cols = ["Name", "Maths", "Sciences", "English", "History", "Average", "Grade", "Status"]
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)
print(df[display_cols].to_string(index=False))


print("\n Class Summary")
print("-" * 60)
display_cols = ["Name", "Maths", "Sciences", "English", "History", "Average", "Grade", "Status"]
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)
print(df[display_cols].to_string(index=False))

passed_df = df[df["Passed_All"] == True].copy()
print(f"\n Students who Passed in All Subjects: {len(passed_df)} / {len(df)}")

top5 = passed_df.sort_values("Average", ascending=False).head(5)
print("\n Top 5 Students Based on Average Marks")
print(top5[["Name", "Average", "Grade"]].to_string(index=False))

print("\n Performance by Subject")
print("-" * 45)
for subj in subjects:
    col = df[subj]
    pass_count = (col >= 40).sum()
    print(f"{subj:<10}: Avg = {col.mean():.1f}, High = {col.max()}, Low = {col.min()}Passed = {pass_count}/20")

print("\n Grade Distribution")
print("-" * 25)
grade_counts = df["Grade"].value_counts().sort_index()
for grade, count in grade_counts.items():
    bar = "*" * count
    print(f"Grade {grade}: {bar} ({count})")

failed_df = df[df["Passed_All"] == False].copy()
print(f"\n Students who Failed in One or More Subjects: {len(failed_df)} / {len(df)}")
print("-" * 45)
for _, row in failed_df.iterrows():
    failed_subjects = [subj for subj in subjects if row[subj] < 40]
    print(f"{row['Name']}: Failed in {', '.join(failed_subjects)}")
