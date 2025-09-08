import pandas as pd
import matplotlib.pyplot as plt

file_path = "tb_ST_Marks.xlsx"
data = pd.read_excel(file_path, header=None, skiprows=1)

data.columns = ["RollNo", "Name", "Maths", "Science", "English", "Computer", "Total", "Percentage"]

print(data.head())

plt.figure(figsize=(10,5))
plt.bar(data["Name"], data["Total"], color="skyblue")
plt.title("Total Marks of Students")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.show()

plt.hist(data["Percentage"], bins=8, color="lightgreen", edgecolor="black")
plt.title("Distribution of Percentages")
plt.xlabel("Percentage")
plt.ylabel("Number of Students")
plt.show()

subject_means = data[["Maths","Science","English","Computer"]].mean()
subject_means.plot(kind="bar", color="coral", figsize=(8,5))
plt.title("Average Marks by Subject")
plt.ylabel("Average Marks")
plt.show()

plt.plot(data["Name"], data["Percentage"], linestyle=":", marker="o", color="purple")
plt.title("Student Percentages (Dotted Line Graph)")
plt.xlabel("Students")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.show()

topper = data.loc[data["Percentage"].idxmax()]
print(f"Topper: {topper['Name']} with {topper['Percentage']}%")
