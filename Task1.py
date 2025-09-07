import matplotlib.pyplot as plt

age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
population = [512, 807, 98]

plt.bar(age_groups, population, color=['yellow', 'blue', 'pink'])
plt.xlabel("Age Groups")
plt.ylabel("Population (in Millions)")
plt.title("India's Population Distribution by Age (2022)")
plt.show()
