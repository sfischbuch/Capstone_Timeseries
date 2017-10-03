import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

forecast0 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_0_t_60_f_14_forecast.pickle')
provenance0 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_0_t_60_f_14_provenance.pickle')
forecast1 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_1_t_60_f_14_forecast.pickle')
forecast2 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_2_t_60_f_14_forecast.pickle')
forecast3 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_2_t_60_f_14_forecast.pickle')
forecast4 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_4_t_60_f_14_forecast.pickle')
forecast5 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_5_t_60_f_14_forecast.pickle')
forecast6 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_6_t_60_f_14_forecast.pickle')
forecast7 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_7_t_60_f_14_forecast.pickle')
forecast8 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_8_t_60_f_14_forecast.pickle')
forecast9 = pd.read_pickle('/home/scott/Desktop/CAPSTONE/feed_9_t_60_f_14_forecast.pickle')
df0 = forecast0.to_frame()
df1 = forecast1.to_frame()
df2 = forecast2.to_frame()
df3 = forecast3.to_frame()
df4 = forecast4.to_frame()
df5 = forecast5.to_frame()
df6 = forecast6.to_frame()
df7 = forecast7.to_frame()
df8 = forecast8.to_frame()
df9 = forecast9.to_frame()
provenance0.to_frame()
df9.unstack(level=0).unstack(level=0).plot(legend=False)
# for i, label in enumerate(df9.unstack(level=0).index):
#     print(i, label)
df0_p0 = df0.swaplevel().loc['p0',:]
df0_p1 = df0.swaplevel().loc['p1',:]
# df0_p0.loc['p0',:]
# ^ Write a script that will pickle these
df9.iloc[15:].unstack(level=0).iloc[1].plot(figsize=(10,8), legend=False, title='p0')
plt.semilogy()
plt.show()
