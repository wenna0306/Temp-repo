import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

st.write('this is testing')
use_cols = ['Email ', 'Department ',
       'Date for temperature taking ',
       'Morning Temperature Reading (MLD) ',
       'Afternoon Temperature Reading (MLD) ']
def fetch_dataset(path):
    return pd.read_excel(path, usecols=use_cols, index_col=0)

path = 'D:\\Temperature\\25 Oct to 31 Oct 2021\\MLD Daily Temperature Taking Responses 2021-10-25_2021-10-31 - Copy.xlsx' #👀
df = fetch_dataset(path)
df.columns = df.columns.str.replace(' ', '_')
df.info()

df_AM = df.loc[:, ['Date_for_temperature_taking_', 'Morning_Temperature_Reading_(MLD)_']]
df_PM = df.loc[:, ['Date_for_temperature_taking_', 'Afternoon_Temperature_Reading_(MLD)_']]
df_AM.dropna(inplace=True)
df_PM.dropna(inplace=True)

path1='D:\\Temperature\\attendance_checker.xlsx' #👀
attendance_checker = pd.read_excel(path1, index_col='email')
attendance_checker.head()

df_AM_001 = df_AM.loc[df_AM.Date_for_temperature_taking_=='2021-10-25', 'Morning_Temperature_Reading_(MLD)_']  #👀
df_AM_01 = df_AM_001[~df_AM_001.index.duplicated(keep='first')]
df_PM_001 = df_PM.loc[df_PM.Date_for_temperature_taking_=='2021-10-25', 'Afternoon_Temperature_Reading_(MLD)_'] #👀
df_PM_01 = df_PM_001[~df_PM_001.index.duplicated(keep='first')]

df_AM_002 = df_AM.loc[df_AM.Date_for_temperature_taking_=='2021-10-26', 'Morning_Temperature_Reading_(MLD)_'] #👀
df_AM_02 = df_AM_002[~df_AM_002.index.duplicated(keep='first')]
df_PM_002 = df_PM.loc[df_PM.Date_for_temperature_taking_=='2021-10-26', 'Afternoon_Temperature_Reading_(MLD)_'] #👀
df_PM_02 = df_PM_002[~df_PM_002.index.duplicated(keep='first')]

df_AM_003 = df_AM.loc[df_AM.Date_for_temperature_taking_=='2021-10-27', 'Morning_Temperature_Reading_(MLD)_'] #👀
df_AM_03 = df_AM_003[~df_AM_003.index.duplicated(keep='first')]
df_PM_003 = df_PM.loc[df_PM.Date_for_temperature_taking_=='2021-10-27', 'Afternoon_Temperature_Reading_(MLD)_'] #👀
df_PM_03 = df_PM_003[~df_PM_003.index.duplicated(keep='first')]

df_AM_004 = df_AM.loc[df_AM.Date_for_temperature_taking_=='2021-10-28', 'Morning_Temperature_Reading_(MLD)_'] #👀
df_AM_04 = df_AM_004[~df_AM_004.index.duplicated(keep='first')]
df_PM_004 = df_PM.loc[df_PM.Date_for_temperature_taking_=='2021-10-28', 'Afternoon_Temperature_Reading_(MLD)_'] #👀
df_PM_04 = df_PM_004[~df_PM_004.index.duplicated(keep='first')]

df_AM_005 = df_AM.loc[df_AM.Date_for_temperature_taking_=='2021-10-29', 'Morning_Temperature_Reading_(MLD)_'] #👀
df_AM_05 = df_AM_005[~df_AM_005.index.duplicated(keep='first')]
df_PM_005 = df_PM.loc[df_PM.Date_for_temperature_taking_=='2021-10-29', 'Afternoon_Temperature_Reading_(MLD)_'] #👀
df_PM_05 = df_PM_005[~df_PM_005.index.duplicated(keep='first')]

df_AM_006 = df_AM.loc[df_AM.Date_for_temperature_taking_=='2021-10-30', 'Morning_Temperature_Reading_(MLD)_'] #👀
df_AM_06 = df_AM_006[~df_AM_006.index.duplicated(keep='first')]
df_PM_006 = df_PM.loc[df_PM.Date_for_temperature_taking_=='2021-10-30', 'Afternoon_Temperature_Reading_(MLD)_'] #👀
df_PM_06 = df_PM_006[~df_PM_006.index.duplicated(keep='first')]

df_AM_007 = df_AM.loc[df_AM.Date_for_temperature_taking_=='2021-10-31', 'Morning_Temperature_Reading_(MLD)_'] #👀
df_AM_07 = df_AM_007[~df_AM_007.index.duplicated(keep='first')]
df_PM_007 = df_PM.loc[df_PM.Date_for_temperature_taking_=='2021-10-31', 'Afternoon_Temperature_Reading_(MLD)_'] #👀
df_PM_07 = df_PM_007[~df_PM_007.index.duplicated(keep='first')]

print(df_PM_005[~df_PM_005.index.duplicated(keep='first')]) #important concept
print(df_PM_005[df_PM_005.index.duplicated(keep='first')])

pdlist=[attendance_checker,
      df_AM_01, df_PM_01,
      df_AM_02, df_PM_02,
      df_AM_03, df_PM_03,
      df_AM_04, df_PM_04,
      df_AM_05, df_PM_05,
      df_AM_06, df_PM_06,
      df_AM_07, df_PM_07,
       ]

df01 = pd.concat(pdlist, axis=1)
df01.head()

cols = ['department',
       '01_AM', '01_PM',
       '02_AM', '02_PM',
       '03_AM', '03_PM',
       '04_AM', '04_PM',
       '05_AM', '05_PM',
       '06_AM', '06_PM',
       '07_AM', '07_PM']
df01.columns = cols


col_name=['department', '01', '02', '03', '04', '05', '06', '07']
df01_AM = df01.loc[:, ['department', '01_AM', '02_AM', '03_AM', '04_AM', '05_AM', '06_AM', '07_AM' ]]
df01_PM = df01.loc[:, ['department', '01_PM', '02_PM', '03_PM', '04_PM', '05_PM', '06_PM', '07_PM' ]]
df01_AM.columns=col_name
df01_PM.columns=col_name
df_all = pd.concat([df01_AM, df01_PM]).reset_index().sort_values(['department', 'index'])


df_all.describe()

print(df_all[df_all.department.str.contains('FMA')].shape)
df_fig01 = df_all[df_all.department.str.contains('FMA')].describe().iloc[[0]]/56 #👀


print(df_all[df_all.department.str.contains('IBC')].shape)
df_fig02 = df_all[df_all.department.str.contains('IBC')].describe().iloc[[0]]/64 #👀


print(df_all[df_all.department.str.contains('PROJ')].shape)
df_fig03 = df_all[df_all.department.str.contains('PROJ')].describe().iloc[[0]]/12 #👀

print(df_all.loc[(df_all.department=='Tech & Innovation'), :].shape)
df_fig04 = df_all.loc[(df_all.department=='Tech & Innovation'), :].describe().iloc[[0]]/6 #👀


pd.options.display.float_format = '{:,.2%}'.format
df_fig = pd.concat([df_fig01, df_fig02, df_fig03, df_fig04], axis=0)

list01 = ['FMA', 'IBC', 'Project', 'Tech&Innovation']
list02 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
df_fig.index=list01
df_fig.columns=list02
df_fig

x = df_fig.columns
y01 = df_fig.iloc[0]
y02 = df_fig.iloc[1]
y03 = df_fig.iloc[2]
y04 = df_fig.iloc[3]

fig, ax = plt.subplots()
sns.lineplot(x, y01, color ='k', linestyle='--', linewidth=2, marker='.', markersize=12, label='FMA', ax=ax)
sns.lineplot(x, y02, color='b', linestyle='-.', linewidth=3, marker='o', markersize=10, label='IBC', ax=ax)
sns.lineplot(x, y03, color='#2a7e19', linestyle=':', linewidth=1, marker='>', markersize=10, label='Project')
sns.lineplot(x, y04, color='#b36ff6', linestyle=':', linewidth=1, marker='>', markersize=10, label='Tech & Innovation')

plt.legend()
st.pyplot(fig)
