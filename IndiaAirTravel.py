import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np


df1=pd.read_csv("c:\DSC\India Air Travel\data\Airlinewise_DGCA_Q12017.csv")
df1['Period'] = '2017Q1'
df2=pd.read_csv("c:\DSC\India Air Travel\data\Airlinewise_DGCA_Q22017.csv")
df2['Period'] = '2017Q2'
df3=pd.read_csv("c:\DSC\India Air Travel\data\Airlinewise_DGCA_Q32017.csv")
df3['Period'] = '2017Q3'
df4=pd.read_csv("c:\DSC\India Air Travel\data\Airlinewise_DGCA_Q42017.csv")
df4['Period'] = '2017Q4'
alldata=pd.concat([df1,df2,df3,df4])
alldata.columns = alldata.columns.str.replace(' ', '_')
alldata=alldata[alldata.NAME_OF_THE_AIRLINE!='TOTAL (DOMESTIC & FOREIGN CARRIERS)']
alldata=alldata[alldata.NAME_OF_THE_AIRLINE!='TOTAL (DOMESTIC CARRIERS)']
alldata=alldata[alldata.NAME_OF_THE_AIRLINE!='TOTAL (FOREIGN CARRIERS)']

#Q1 What is the number of passengers that flew in and out of India?
pasngronly=alldata[['Category','NAME_OF_THE_AIRLINE','PASSENGERS_TO_INDIA',
                    'PASSENGERS_FROM_INDIA','Period']]
pastotal=pasngronly.groupby('Category')['PASSENGERS_TO_INDIA',
                           'PASSENGERS_FROM_INDIA'].sum()
pastotal['Total'] = pastotal.values[:, 0:].sum(1)
total=pastotal['Total'].sum()
print('No. of total passenger flown in and out of India in 2017 are:'+ str(total))
print(pastotal.to_string())

netmove=pasngronly.groupby('Category')['PASSENGERS_TO_INDIA',
                           'PASSENGERS_FROM_INDIA'].sum()
netmove.loc['Total'] = pastotal[['PASSENGERS_TO_INDIA','PASSENGERS_FROM_INDIA']].sum()
print(netmove.index[2])



#Q2 trend of passengers travelling through different times of the year?
qsummary=alldata[['PASSENGERS_TO_INDIA','PASSENGERS_FROM_INDIA','Period']]
VS2=qsummary.groupby('Period')['PASSENGERS_TO_INDIA',
                    'PASSENGERS_FROM_INDIA'].aggregate(np.sum)
ax = VS2[['PASSENGERS_TO_INDIA','PASSENGERS_FROM_INDIA']].plot(kind='bar'
        , stacked=False, title ="Indian vs. Foreign Airlines", 
        figsize=(8,5),legend=True, fontsize=12)
ax.set_ylim([0,10000000])
ax.set_xlabel("2017 Quarterly Data",fontsize=12)
ax.set_ylabel("No. of Passengers (x10 millions)",fontsize=12)
plt.show()


#Q visible preference between Indian or International carrier to go out of or come in to India
forsummary=alldata[['Category','PASSENGERS_TO_INDIA','PASSENGERS_FROM_INDIA']]
VS1=forsummary.groupby('Category')['PASSENGERS_TO_INDIA',
                      'PASSENGERS_FROM_INDIA'].aggregate(np.sum)
ax = VS1[['PASSENGERS_TO_INDIA','PASSENGERS_FROM_INDIA']].plot(kind='bar', 
        title ="Indian vs. Foreign Airlines",figsize=(8,5),legend=True, 
        fontsize=12)
ax.set_ylim([0,25000000])
ax.set_xlabel("Airline Carriers",fontsize=12)
ax.set_ylabel("No. of Passengers (x10 millions)",fontsize=12)
plt.show()


airlineonly=pasngronly.groupby('NAME_OF_THE_AIRLINE')['PASSENGERS_TO_INDIA',
                           'PASSENGERS_FROM_INDIA'].sum()
airlineonly['Total'] = airlineonly.values[:, 0:].sum(1)
airlineonly=airlineonly.sort_values(['Total'], ascending=False)
print(airlineonly.nlargest(10, 'Total').to_string())



cdf1=pd.read_csv("c:\DSC\India Air Travel\data\Countrywise_DGCA_Q12017.csv")
cdf1['Period'] = '2017Q1'
cdf2=pd.read_csv("c:\DSC\India Air Travel\data\Countrywise_DGCA_Q22017.csv")
cdf2['Period'] = '2017Q2'
cdf3=pd.read_csv("c:\DSC\India Air Travel\data\Countrywise_DGCA_Q32017.csv")
cdf3['Period'] = '2017Q3'
cdf4=pd.read_csv("c:\DSC\India Air Travel\data\Countrywise_DGCA_Q42017.csv")
cdf4['Period'] = '2017Q4'
countrydata=pd.concat([cdf1,cdf2,cdf3,cdf4])
countrydata.columns = countrydata.columns.str.replace(' ', '_')
countrydata=countrydata[countrydata.NAME_OF_THE_COUNTRY!='TOTAL']
    
countryonly=countrydata[['NAME_OF_THE_COUNTRY','PASSENGERS_TO_INDIA',
                        'PASSENGERS_FROM_INDIA','Period']]
countrytotal=countryonly.groupby('NAME_OF_THE_COUNTRY')['PASSENGERS_TO_INDIA',
                               'PASSENGERS_FROM_INDIA'].sum()
    
countrytotal['Total'] = countrytotal.values[:, 0:].sum(1)

result = countrytotal.sort_values(['Total'], ascending=True)

ax = result[['Total']].plot(kind='bar'
        , stacked=False, title ="Indian vs. Foreign Airlines", 
        figsize=(8,5),legend=True, fontsize=6)
ax.set_ylim([0,20000000])
ax.set_xlabel("Coutries",fontsize=12)
ax.set_ylabel("No. of Passengers (x10 millions)",fontsize=12)
plt.show()


fig, ax = plt.subplots(figsize=(15, 15))
ax.set( xlabel='Total Passengers',ylabel='Country',
       title='No. of Passengers by Country of Travel')
ax.barh(result.index.values, result['Total'])
plt.show()

print(result.nlargest(5, 'Total').to_string())
print(result.nlargest(5, 'PASSENGERS_TO_INDIA').to_string())
print(result.nlargest(5, 'PASSENGERS_FROM_INDIA').to_string())

print(result.nsmallest(10, 'Total').to_string())
#print(topfive.to_string())

#############################################################################
cidf1=pd.read_csv("c:\DSC\India Air Travel\data\Citypairwise_DGCA_Q12017.csv")
cidf1['Period'] = '2017Q1'
cidf2=pd.read_csv("c:\DSC\India Air Travel\data\Citypairwise_DGCA_Q22017.csv")
cidf2['Period'] = '2017Q2'
cidf3=pd.read_csv("c:\DSC\India Air Travel\data\Citypairwise_DGCA_Q32017.csv")
cidf3['Period'] = '2017Q3'
cidf4=pd.read_csv("c:\DSC\India Air Travel\data\Citypairwise_DGCA_Q42017.csv")
cidf4['Period'] = '2017Q4'
citydata=pd.concat([cidf1,cidf2,cidf3,cidf4])
citydata.columns = citydata.columns.str.replace(' ', '_')
citydata=citydata[citydata.Category!='Entirely outside the Indian Territory']
citydata=citydata[citydata.CITY_1!='SUB TOTAL']
citydata=citydata[citydata.CITY_1!='GRAND TOTAL']


cityonly=citydata[['CITY_1','CITY_2','PASSENGERS_TO_CITY_2',
                    'PASSENGERS_FROM_CITY_2','Period']]
city1=cityonly.groupby('CITY_1')['PASSENGERS_TO_CITY_2',
                           'PASSENGERS_FROM_CITY_2'].sum()

city1['Total'] = city1.values[:, 0:].sum(1)

city1total = city1.sort_values(['Total'], ascending=False)

top10cities=(city1total.nlargest(10, 'Total'))
print(top10cities.to_string())

print(city1total.nlargest(10, 'Total').to_string())
