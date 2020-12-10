#Goals of this analysis:
#Compare the average costs of smokers vs. non-smokers
#Find both the average age of people with kids
#find the youngest person with kids

import csv
import pandas as pd

#import csv to pd.dataframe
dataset = pd.read_csv("insurance.csv")
#check out structure of the data
#print(dataset.head(5))

#1. Goal: Find average costs of smokers vs. nonsmokers:
mean_of_smokers_vs_nonsmokers = dataset.groupby('smoker')["charges"].mean()
#print(mean_of_smokers_vs_nonsmokers)

#alternative
mean_of_smokers = round(dataset[dataset['smoker'] == "yes"]["charges"].mean(), 2)
mean_of_nonsmokers = round(dataset[dataset['smoker'] == "no"]["charges"].mean(), 2)
ratio = round(mean_of_smokers/mean_of_nonsmokers, 1)
print(f"The average insurance costs of smokers are {mean_of_smokers} while the average costs of nonsmokers is {mean_of_nonsmokers}. The costs for smokers is {ratio} times higher! ")

#2. Goal: Find the average age of people with kids:
average_age_with_kids = round(dataset[dataset["children"] >= 1]["age"].mean(), 1)
print(f"The average age of people with kids is {average_age_with_kids} years.")

#3. Goal: Find the youngest person with kids:
youngest_person_with_kids = dataset[dataset["children"] >= 1]["age"].min()
print(f"The youngest person with kids is {youngest_person_with_kids} years old.")




