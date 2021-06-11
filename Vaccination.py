# Covid-19-vaccination
A Python Code for Covid-19 Vaccination in India Using Machine Learning

# It is defined by the Shamsher using  Python Machine Learning

#Some Libraries We Need to Import From The Pip Library
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sb # use to Matplotlib Underneath to Plot Graphs
import matplotlib.pyplot as plt #Use to Plot Graphs
import numpy as np # it is used to calculate the mathematical equations
import cufflinks as cl # use to connect the Pandas data frame with Plotly enabling to create Visualizations directly
import plotly.offline as po # This Allows us to generate graphs offline and save them in local Machine
import warnings # importing Warning Library to ignore the minor bugs
warnings.filterwarnings('ignore')

# Enabling the offline Mode to Generate Graphs
po.init_notebook_mode(connected=True)
cl.go_offline()

# Fetcing CSV file from the dirctory
df = pd.read_csv('covid_vaccine_statewise.csv')

# This allows us to Fetch first Top 5 Data from the list
df.head()
# Checking if the file is null if There is no data then Calling Sum() function To add present Data
df.isnull().sum()

# Setting up the Figure Size to 10,12
plt.rcParams['figure.figsize'] = 10, 12 


# First Dose Administered & Second Dose Administered
f, sub = plt.subplots(figsize=(28, 28))
content= df[['State','First Dose Administered','Second Dose Administered']]   
content.sort_values('First Dose Administered',ascending=False,inplace=True)
sb.set_color_codes("pastel")
sb.barplot(x="First Dose Administered", y="State", data=content,label="First Dose Administered", color="blue")
sb.set_color_codes("muted")
sb.barplot(x="Second Dose Administered", y="State", data=content, label="Second Dose Administered", color="green")
sub.legend(ncol=2, loc="lower right", frameon=True)
sub.set(xlim=(0, 700000), ylabel="",xlabel="First Dose Administered & Second Dose Administered")
sb.despine(left=True, bottom=True)



# Male(Individuals Vaccinated) & Female(Individuals Vaccinated)
f, sub = plt.subplots(figsize=(28, 28))
content = df[['State','Male(Individuals Vaccinated)','Female(Individuals Vaccinated)']]   
content.sort_values('Female(Individuals Vaccinated)',ascending=False,inplace=True)
sb.set_color_codes("pastel")
sb.barplot(x="Male(Individuals Vaccinated)", y="State", data=content,label="Male", color="black")
sb.set_color_codes("muted")
sb.barplot(x="Female(Individuals Vaccinated)", y="State", data=content, label="Female", color="orange")
sub.legend(ncol=2, loc="lower right", frameon=True)
sub.set(xlim=(0, 700000), ylabel="",xlabel="Male(Individuals Vaccinated) & Female(Individuals Vaccinated)")
sb.despine(left=True, bottom=True)


#Total Individuals Vaccinated
f, sub = plt.subplots(figsize=(28, 28))
content = df[['State','Total Individuals Vaccinated']]   
content.sort_values('Total Individuals Vaccinated',ascending=False,inplace=True)
sb.set_color_codes("pastel")
sb.barplot(x="Total Individuals Vaccinated", y="State", data=content,label="Total Individuals Vaccinated", color="skyblue")
sb.set_color_codes("muted")
sub.set(xlim=(0, 500000), ylabel="",xlabel="Total Individuals Vaccinated")


# Total Covaxin Administered 
f, sub = plt.subplots(figsize=(28, 28))
content = df[['State','Total Covaxin Administered']]   
content.sort_values('Total Covaxin Administered',ascending=False,inplace=True)
sb.set_color_codes("pastel")
sb.barplot(x="Total Covaxin Administered", y="State", data=content,label="Total Covaxin Administered", color="yellow")
sb.set_color_codes("muted")
sub.set(xlim=(0, 500000), ylabel="",xlabel="Total Covaxin Administered")

# Total CoviShield Administered
f, sub = plt.subplots(figsize=(28, 28))
content = df[['State','Total CoviShield Administered']]   
content.sort_values('Total CoviShield Administered',ascending=False,inplace=True)
sb.set_color_codes("pastel")
sb.barplot(x="Total CoviShield Administered", y="State", data=content,label="Total CoviShield Administered", color="lightgreen")
sb.set_color_codes("muted")
sub.set(xlim=(0, 500000), ylabel="",xlabel="Total CoviShield Administered")


#Total Doses Administered
f, sub = plt.subplots(figsize=(28, 28))
content = df[['State','Total Doses Administered']]   
content.sort_values('Total Doses Administered',ascending=False,inplace=True)
sb.set_color_codes("pastel")
sb.barplot(x="Total Doses Administered", y="State", data=content,label="Total Doses Administered", color="orange")
sb.set_color_codes("muted")
sub.set(xlim=(0, 500000), ylabel="",xlabel="Total Doses Administered")

#code for circle
labels=np.array(['18-45 years (Age)', '45-60 years (Age)', '60+ years (Age)'])
stats=df.loc[386,labels].values
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)

# close the plot
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig=plt.figure()
circle = fig.add_subplot(111, polar=True)
circle.plot(angles, stats, 'o-', linewidth=2)
circle.set_thetagrids(angles * 180/np.pi, labels)
circle.grid(True)
