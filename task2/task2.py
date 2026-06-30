import pandas as pd 
import matplotlib.pyplot as plt
##Read data 
data = pd.read_csv("titanic.csv") 
df = pd.DataFrame(data)
#____________________________________________________________________________________________________
## Clean data 
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Age"] = df["Age"].astype(int)
df["Age"] = df["Age"].replace(0,df["Age"].median())
df["Cabin"] = df["Cabin"].astype(str)
df["Cabin"] = df["Cabin"].fillna("Missing")
df["Cabin_letter"] = df["Cabin"].str[0]
df["Cabin_letter"] = df["Cabin_letter"].replace("M","Missing")
df["Embarked"] = df["Embarked"].fillna("Missing")
#____________________________________________________________________________________________________
## Age EDA
df["Age"].plot(kind= "hist", bins =20)
plt.xlabel("Age")
plt.ylabel("Number of passengers")
plt.show()

## Fare EDA
df["Fare"].plot(kind= "hist",bins=20)
plt.xlabel("Fare")
plt.ylabel("Number of passengers")
plt.show()

## Pclass EDA 
print("\n-----------------------------")
print("Number of passenger in Pclass")
print("-----------------------------")
print(df["Pclass"].value_counts().sort_index())

## Sex EDA 
print("\n-----------------------------")
print("Number of passenger in Sex")
print("-----------------------------")
print(df["Sex"].value_counts().sort_index()) 

## Cabin EDA
print("\n-----------------------------")
print("Number of passenger in Cabin")
print("-----------------------------")
print(df["Cabin_letter"].value_counts().sort_index())

## Survived EDA 
print("\n-----------------------------")
print("Number of Survived passenger")
print("-----------------------------")
print(df["Survived"].value_counts().sort_index())

#____________________________________________________________________________________________________
## Relation between survived and Sex
sex_percent= (df.groupby("Sex")["Survived"].mean()*100).astype(int)
sex_percent = sex_percent.reset_index()
sex_percent.columns = ["Sex","Survived%"] 
print("\n-----------------------------")
print("Survival Percentage by Sex")
print("-----------------------------")
print(sex_percent)
print("Females had a much higher survival rate than males")
sex_percent.plot(kind="bar", y="Survived%")
plt.xticks(ticks=[0,1], labels=["Female", "Male"], rotation=0)
plt.title("Survival Percentage by Sex")
plt.ylabel("Survived %")
plt.xlabel("Sex")
plt.show()

## Relation between survived and Pclass
pclass_percent= (df.groupby("Pclass")["Survived"].mean()*100).astype(int)
pclass_percent = pclass_percent.reset_index()
pclass_percent.columns = ["Pclass","Survived%"]
print("\n-----------------------------")
print("Survival Percentage by Pclass")
print("-----------------------------") 
print(pclass_percent)
print("Passengers in first class had a higher survival rate than those in third class.")
pclass_percent.plot(kind="bar",y="Survived%")
plt.xticks(ticks=[0,1,2], labels=["First Class","Second Class","Third Class"], rotation=0)
plt.title("Survival Percentage by Pclass")
plt.ylabel("Survived %")
plt.xlabel("Pclass")
plt.show()

## Relation between survived and Cabin_letter
cabin_percent = ((df.groupby("Cabin_letter")["Survived"].mean()*100).astype(int))
cabin_percent = cabin_percent.reset_index()
cabin_percent.columns = ["Cabin_letter", "Survived %"]
print("\n-----------------------------")
print("Survival Percentage by Cabin_letter")
print("-----------------------------")
print(cabin_percent)
print("A large number of passengers had missing cabin information, which may suggest that many third-class passengers did not have assigned cabins.")
cabin_percent.plot(kind="bar")
plt.xticks(ticks=[0,1,2,3,4,5,6,7,8], labels=["A","B","C","D","E","F","G","Missing","T"], rotation=0)
plt.title("Survival Percentage by Cabin")
plt.ylabel("Survived %")
plt.xlabel("Cabin")
plt.show()

## Relation between survived and Age
df["Age_group"] = pd.cut(df["Age"],bins=[0,12,18,60,100], labels = ["child","teenager","adult","senior"])
age_table = pd.crosstab(df["Age_group"],df["Survived"])
age_table["Total"] = age_table[1] + age_table[0]
age_table["Survived%"] = ((age_table[1] / age_table["Total"]) * 100).astype(int)
print("\n-----------------------------")
print("Survival Percentage by Age")
print("-----------------------------")
print(age_table)
print("Children had a slightly higher chance of survival compared to adults.")
age_table.plot(kind="bar",y="Survived%")
plt.xticks(ticks=[0,1,2,3], labels=["child","teenager","adult","senior"], rotation=0)
plt.title("Survival Percentage by Age")
plt.ylabel("Survived %")
plt.xlabel("Age")
plt.show()

## Relation between survived and Fare
df["Fare_group"] = pd.qcut(df["Fare"],q=4, labels= ["Low","Medium","High","Very High"])
Fare_table = pd.crosstab(df["Fare_group"],df["Survived"])
Fare_table["Total"] = Fare_table[1] + Fare_table[0]
Fare_table["Survived%"] = ((Fare_table[1] / Fare_table["Total"]) * 100).astype(int)
print("\n-----------------------------")
print("Survival Percentage by Fare_table")
print("-----------------------------")
print(Fare_table)
print("Passengers who paid higher fares had better survival chances.")
Fare_table.plot(kind="bar", y="Survived%")
plt.xticks(ticks=[0,1,2,3], labels=["Low","Medium","High","Very High"], rotation=0)
plt.title("Survival Percentage by Fare")
plt.ylabel("Survived %")
plt.xlabel("Fare")
plt.show()
#____________________________________________________________________________________________________
df.to_csv("titanic_clean.csv", index=False)
