import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sns
df =pd.read_excel(r"C:\Users\kagga\OneDrive\Desktop\project -1\June_2024_May_2025_Transaction.xlsx")
df.columns
df.dtypes
df.info()
df.describe()
df.head()
df.tail()
df.InvoiceQuantity.mean()
df.InvoiceQuantity.median()
df.InvoiceQuantity.mode()
df.InvoiceQuantity.var()
df.InvoiceQuantity.std()
range = max(df.InvoiceQuantity) - min(df.InvoiceQuantity)
range
df.InvoiceQuantity.skew()
df.InvoiceQuantity.kurt()


pt.hist(df.InvoiceQuantity)
pt.show()

sns.boxplot(df.InvoiceQuantity)
pt.tile("boxplot")
pt.show()

sns.kdeplot(df.InvoiceQuantity)
pt.tile("density")
pt.show()


pt.scatter(df.index, df['InvoiceQuantity'])
pt.xlabel('Index')
pt.ylabel('Invoice Quantity')
pt.title('Scatter Plot of Invoice Quantity vs Index')
pt.show()

s = df.select_dtypes(include = "number")
s.corr()

sns.heatmap(s.corr(), annot = True, cmap = "coolwarm")
pt.title("Correlation Heatmap")
pt.show()


pt.bar(height =df.InvoiceQuantity , x = np.arange(18249, 18250,))  
pt.title("barplot")
pt.show()


sns.pairplot(df)
pt.title("pairplot")
pt.show()

import scipy.stats as stats
import pylab
stats.probplot(df.InvoiceQuantity, dist = "norm", plot = pylab)
pt.title("Q-Q Plot")
pt.show()




category_counts = df['AuthorizationStatus'].value_counts()
category_counts.plot(kind='bar')
pt.title('Category Counts')
pt.show()

category_counts = df["ItemCategory"].value_counts()
category_counts.plot(kind = "bar")
pt.title("barplot")
pt.show()




category_counts = df["MinimumOrder"].value_counts()
category_counts.plot(kind = "bar")
pt.title("barplot")
pt.show()



category_counts = df["InvoiceStatus"].value_counts()
category_counts.plot(kind = "bar")
pt.title("barplot")
pt.show()




category_counts = df["OrderStatus"].value_counts()
category_counts.plot(kind = "bar")
pt.title("barplot")
pt.show()


category_counts = df["ExtraFieldsFinalDestination"].value_counts()
category_counts.plot(kind = "bar")
pt.title("barplot")
pt.show()


#Data preprocessing


#ItemPacketSize(column)
#typcasting
df.dtypes
df["ItemPacketSize"] = df["ItemPacketSize"].str.extract('(\d+\.?\d*)')#it helps to remove the grams ,kg 
df.ItemPacketSize  = df.ItemPacketSize.astype("int64")
df.dtypes
#duplicate handling
duplicate = df.duplicated()
duplicate

#outliers analysis
#item packet size
sns.boxplot(df.ItemPacketSize)#no outliers
pt.title("box")
pt.show()

#missing values
df.isna()
df.isna().sum()
df.dtypes
from sklearn.impute import SimpleImputer

mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
df["ItemPacketSize"] = pd.DataFrame(mean_imputer.fit_transform(df[["ItemPacketSize"]]))
df["ItemPacketSize"].isna().sum()

#missing values
df.isna()
df.isna().sum()
df.dtypes
from sklearn.impute import SimpleImputer

mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
df["ItemPacketSize"] = pd.DataFrame(mean_imputer.fit_transform(df[["ItemPacketSize"]]))
df["ItemPacketSize"].isna().sum()


#bussiness moment
df.ItemPacketSize.mean()
df.ItemPacketSize.median()
df.ItemPacketSize.mode()
df.ItemPacketSize.var()
df.ItemPacketSize.std()
range = max(df.ItemPacketSize) - min(df.ItemPacketSize)
range


pt.hist(df.ItemPacketSize)
pt.show()

sns.boxplot(df.ItemPacketSize)
pt.show()

sns.kdeplot(df.ItemPacketSize)
pt.show()



#ItemGrams(column)
#typecasting
df['ItemGrams'] = pd.to_numeric(df['ItemGrams'], errors='coerce')
df.ItemGrams  = df.ItemGrams.astype("float64")
df.dtypes
#duplicate handling
duplicate = df.duplicated()
duplicate


#outliers analysis
sns.boxplot(df.ItemGrams)
pt.title("Boxplot of ItemGrams")
pt.show()

IQR = df["ItemGrams"].quantile(0.75) - df["ItemGrams"].quantile(0.25)
lower_limit = df["ItemGrams"].quantile(0.25) - IQR*0.5
upper_limit = df["ItemGrams"].quantile(0.75)-IQR*0.5

Remove_out = np.where(df.ItemGrams > upper_limit,True , np.where(df.ItemGrams < lower_limit,True,False))
df_out = df.loc[Remove_out, ]
df_trim = df.loc[~(Remove_out),]
sns.boxplot(df_trim.ItemGrams)
pt.title("box")
pt.show()

#missing values
mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
df_trim["ItemGrams"] = pd.DataFrame(mean_imputer.fit_transform(df_trim[["ItemGrams"]]))
df_trim["ItemGrams"].isna().sum()

#bussiness moments
df_trim.ItemGrams.mean()
df_trim.ItemGrams.median()
df_trim.ItemGrams.mode()
df_trim.ItemGrams.var()
df_trim.ItemGrams.std()
df_trim.ItemGrams.skew()
df_trim.ItemGrams.kurt()
range =max(df_trim.ItemGrams) - min(df_trim.ItemGrams)
range


pt.hist(df_trim.ItemGrams)
pt.show()

sns.boxplot(df_trim.ItemGrams)
pt.show()

sns.kdeplot(df_trim.ItemGrams)
pt.show()



#ItemNetWeight(column)
#typecasting
df['ItemNetWeight'] = pd.to_numeric(df['ItemNetWeight'], errors='coerce')
df.ItemGrams  = df.ItemGrams.astype("float64")
df.dtypes
#duplicate handling
duplicate = df.duplicated()
duplicate

duplicate = df.duplicated(keep = False)
duplicate

duplicate = df.drop_duplicates(keep = False)
duplicate

#outlier analysis
sns.boxplot(df.ItemNetWeight)
pt.title("box")
pt.show()

IQR = df["ItemNetWeight"].quantile(0.75) - df["ItemNetWeight"].quantile(0.25)
lower_limit = df["ItemNetWeight"].quantile(0.25) - IQR*0.5
upper_limit = df["ItemNetWeight"].quantile(0.75)-IQR*0.5

Remove_out = np.where(df.ItemNetWeight > upper_limit,True , np.where(df.ItemNetWeight < lower_limit,True,False))
df_out = df.loc[Remove_out, ]
df_trim = df.loc[~(Remove_out),]
sns.boxplot(df_trim.ItemNetWeight)
pt.title("box")
pt.show()

#missing values
mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
df_trim["ItemNetWeight"] = pd.DataFrame(mean_imputer.fit_transform(df_trim[["ItemNetWeight"]]))
df_trim["ItemNetWeight"].isna().sum()


#bussiness moments

df_trim.ItemNetWeight.mean()
df_trim.ItemNetWeight.median()
df_trim.ItemNetWeight.mode()
df_trim.ItemNetWeight.var()
df_trim.ItemNetWeight.std()
range = max(df_trim.ItemNetWeight) - min(df_trim.ItemNetWeight)
range
df_trim.ItemNetWeight.skew()
df_trim.ItemNetWeight.kurt()

pt.hist(df_trim.ItemNetWeight)
pt.show()

sns.boxplot(df_trim.ItemNetWeight)
pt.show()

sns.kdeplot(df_trim.ItemNetWeight)
pt.show()




#quantity(column)
#typecasting
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Quantity'] = df['Quantity'].fillna(0).astype('int64')   
df.Quantity = df.Quantity.astype("int64")

#duplicate handling
duplicate = df.duplicated()
duplicate

duplicate = df.duplicated(keep = False)
duplicate

duplicate = df.drop_duplicates(keep = False)
duplicate

#outlier analysis
sns.boxplot(df.Quantity)
pt.title("box")
pt.show()


IQR = df["Quantity"].quantile(0.75) - df["Quantity"].quantile(0.25)
lower_limit = df["Quantity"].quantile(0.25) - IQR*0.5
upper_limit = df["Quantity"].quantile(0.75)-IQR*0.5

Remove_out = np.where(df.Quantity > upper_limit,True , np.where(df.Quantity < lower_limit,True,False))
df_out = df.loc[Remove_out, ]
df_trim = df.loc[~(Remove_out),]
sns.boxplot(df_trim.Quantity)
pt.title("box")
pt.show()

#missing values
mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
df_trim["Quantity"] = pd.DataFrame(mean_imputer.fit_transform(df_trim[["Quantity"]]))
df_trim["Quantity"].isna().sum()

#bussiness moments

df_trim.Quantity.mean()
df_trim.Quantity.median()
df_trim.Quantity.mode()
df_trim.Quantity.var()
df_trim.Quantity.std()
range = max(df_trim.Quantity) - min(df_trim.Quantity)
range
df_trim.Quantity.skew()
df_trim.Quantity.kurt()
 
pt.hist(df_trim.Quantity)
pt.show()

sns.boxplot(df_trim.Quantity)
pt.show()

sns.kdeplot(df_trim.Quantity)
pt.show()

#Rate(column)
#typecasting
df['Rate'] = pd.to_numeric(df['Rate'], errors='coerce')
df.Rate  = df.Rate.astype("float64")
df.dtypes

#duplicate handling
duplicate = df.duplicated()
duplicate

duplicate = df.duplicated(keep = False)
duplicate

duplicate = df.drop_duplicates(keep = False)
duplicate

#outliers analysis
sns.boxplot(df.Rate)
pt.show("box")
pt.show()

IQR = df["Rate"].quantile(0.75) - df["Rate"].quantile(0.25)
lower_limit = df["Rate"].quantile(0.25) - IQR*0.5
upper_limit = df["Rate"].quantile(0.75)-IQR*0.5

Remove_out = np.where(df.Rate > upper_limit,True , np.where(df.Rate < lower_limit,True,False))
df_out = df.loc[Remove_out, ]
df_trim = df.loc[~(Remove_out),]
sns.boxplot(df_trim.Rate)
pt.title("box")
pt.show()

#missing values

mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
df_trim["Rate"] = pd.DataFrame(mean_imputer.fit_transform(df_trim[["Rate"]]))
df_trim["Rate"].isna().sum()

#bussines moments


df_trim.Rate.mean()
df_trim.Rate.median()
df_trim.Rate.mode()
df_trim.Rate.var()
df_trim.Rate.std()
range = max(df_trim.Rate) - min(df_trim.Rate)
range
df_trim.Rate.skew()
df_trim.Rate.kurt()
pt.hist(df_trim.Rate)
pt.show()

sns.boxplot(df_trim.Rate)
pt.show()

sns.kdeplot(df_trim.Rate)
pt.show()


#InvoiceQuantity(column)
#outliers 
sns.boxplot(df.InvoiceQuantity)
pt.show("box")
pt.show()

IQR = df["InvoiceQuantity"].quantile(0.75) - df["InvoiceQuantity"].quantile(0.25)
lower_limit = df["InvoiceQuantity"].quantile(0.25) - IQR*0.5
upper_limit = df["InvoiceQuantity"].quantile(0.75)-IQR*0.5

Remove_out = np.where(df.InvoiceQuantity > upper_limit,True , np.where(df.InvoiceQuantity < lower_limit,True,False))
df_out = df.loc[Remove_out, ]
df_trim = df.loc[~(Remove_out),]
sns.boxplot(df_trim.InvoiceQuantity)
pt.title("box")
pt.show()

#missing values
mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
df_trim["InvoiceQuantity"] = pd.DataFrame(mean_imputer.fit_transform(df_trim[["InvoiceQuantity"]]))
df_trim["InvoiceQuantity"].isna().sum()

#bussiness moment
df_trim.InvoiceQuantity.mean()
df_trim.InvoiceQuantity.median()
df_trim.InvoiceQuantity.mode()
df_trim.InvoiceQuantity.var()
df_trim.InvoiceQuantity.std()
range = max(df_trim.InvoiceQuantity) - min(df_trim.InvoiceQuantity)
range
df_trim.InvoiceQuantity.skew()
df_trim.InvoiceQuantity.kurt()
pt.hist(df_trim.InvoiceQuantity)
pt.show()

sns.boxplot(df_trim.InvoiceQuantity)
pt.show()

sns.kdeplot(df_trim.InvoiceQuantity)
pt.show()


#scatter plot for itemgrams
pt.scatter(x = df_trim['ItemGrams'], y = df_trim['ItemNetWeight']) 
pt.show()

#q-q plot

import scipy.stats as stats
import pylab
stats.probplot(df_trim.ItemGrams, dist = "norm", plot = pylab)
pt.show()
df_trim[['ItemGrams','ItemNetWeight']].corr()
df_c =df_trim.select_dtypes(include= "number")
df_c .corr()
sns.heatmap(df_c.corr(), annot = True, cmap = "coolwarm") 
pt.show()


#scatter plot for itemnetweight

pt.scatter(x = df_trim['ItemNetWeight'], y = df_trim['Quantity']) 
pt.show()

#q-q plot for probability distribution
stats.probplot(df_trim.ItemNetWeight, dist = "norm", plot = pylab)
pt.show()


#scatter plot for quantity

pt.scatter(x = df_trim['Quantity'], y = df_trim['InvoiceQuantity'])
pt.show()
#q-q plot for probability distribution
stats.probplot(df_trim.Quantity, dist = "norm", plot = pylab)
pt.show()


#rate 
#scatter
pt.scatter(x = df_trim['Rate'], y = df_trim['InvoiceQuantity'])
pt.show()

#q-q plot for probability distribution
stats.probplot(df_trim.Rate, dist = "norm", plot = pylab)
pt.show()


#invoice quantity
#scatter
pt.scatter(x = df_trim['InvoiceQuantity'], y = df_trim['Quantity'])
pt.show()


#q-q plot for probability distribution
stats.probplot(df_trim.InvoiceQuantity, dist = "norm", plot = pylab)
pt.show()













