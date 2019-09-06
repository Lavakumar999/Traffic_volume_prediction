import pandas as pd


#Train data
train_data = pd.read_csv("C://Users//thatisla//Desktop//dataset//DataSets//Train.csv")
# print(len(train_data["weather_description"].unique()))
# print(train_data["weather_description"].unique())
#print(train_data["weather_type"].unique())
weather = {'Clouds':2,'Clear':1,'Rain':10,'Drizzle':9,'Mist':7,'Haze':6,'Fog':4,'Thunderstorm':11,'Snow':3,'Squall':8,'Smoke':5}

train_data["weather_num"] = [weather[item] for item in train_data.weather_type]
# print(train_data["weather_num"])
# print(len(train_data["is_holiday"].unique()))
train_data['holiday'] = train_data['is_holiday'].str.contains("None")
train_data['holiday'] = train_data['holiday'].map({True: 0, False: 1})
# print(train_data["holiday"].unique())
#train_data = train_data.reset_index()
# print(train_data.loc[train_data['traffic_volume'].idxmax()])
# print(train_data.loc[train_data['traffic_volume'].idxmin()])

date_time_split = train_data["date_time"].str.split(" ", n=1, expand=True)
train_data["date"] = date_time_split[0]
date_time_split[1]=date_time_split[1].str.slice(0,2)
train_data["time"] = date_time_split[1]
train_data.loc[train_data['time'].str.contains(':'), 'time'] =train_data["time"].str.slice(0,1)
#print(train_data["time"])

# print(train_data[['time','weather_type','traffic_volume']].sort_values('traffic_volume', ascending=False).nlargest(40, 'traffic_volume'))
#
# print("Asending order=======")
# print(train_data[['time','weather_type','traffic_volume']].sort_values('traffic_volume',ascending=True).nsmallest(40, 'traffic_volume'))
train_trim_frame=train_data[['time','holiday','air_pollution_index','humidity','wind_speed','wind_direction','visibility_in_miles','dew_point','temperature','rain_p_h','snow_p_h','clouds_all','traffic_volume']]

# for i in range(1,24):
#     print("-------------------------------------")
#     print(i)
#     time=str(i)
#     Date_check_mxv=trim_frame[trim_frame['time'].str.match(time)].sort_values('traffic_volume', ascending=False).nlargest(3, 'traffic_volume')
#     Date_check_mnv=trim_frame[trim_frame['time'].str.match(time)].sort_values('traffic_volume',ascending=False).nsmallest(3, 'traffic_volume')
#     Median=trim_frame[trim_frame['time'].str.match(time)]
#     tot=len(trim_frame[trim_frame['time'].str.match(time)])
#     centre=tot/2
#     print(tot,int(centre))
#     print(trim_frame.iloc[int(centre)]['traffic_volume'])



#Test Data
test_data = pd.read_csv("C://Users//thatisla//Desktop//dataset//DataSets//Test.csv")
test_data['holiday'] = test_data['is_holiday'].str.contains("None")
test_data['holiday'] = test_data['holiday'].map({True: 0, False: 1})

date_time_split = test_data["date_time"].str.split(" ", n=1, expand=True)
test_data["date"] = date_time_split[0]
date_time_split[1]=date_time_split[1].str.slice(0,2)
test_data["time"] = date_time_split[1]
test_data.loc[test_data['time'].str.contains(':'), 'time'] =test_data["time"].str.slice(0,1)
test_trim_frame=test_data[['time','holiday','air_pollution_index','humidity','wind_speed','wind_direction','visibility_in_miles','dew_point','temperature','rain_p_h','snow_p_h','clouds_all']]



#FinalFrames
print("Train Frame")
print(train_trim_frame[['time','holiday','traffic_volume']].head(10))
print("Test Frame")
print(test_trim_frame[['time','holiday']].head(10))

training_set = []
training_set_y = []

# Preparing Training Data set
# Extracting each parameter into different list.

for idx in train_trim_frame.index:
    training_set.append(
        [
          int(train_trim_frame['time'][idx]),
          train_trim_frame['holiday'][idx],
          train_trim_frame['air_pollution_index'][idx],
          train_trim_frame['humidity'][idx],
          train_trim_frame['wind_speed'][idx],
          train_trim_frame['wind_direction'][idx],
          train_trim_frame['visibility_in_miles'][idx],
          train_trim_frame['temperature'][idx],
          train_trim_frame['rain_p_h'][idx],
          train_trim_frame['snow_p_h'][idx],
          train_trim_frame['clouds_all'][idx],

        ]
    )
    training_set_y.append(train_trim_frame['traffic_volume'][idx])





print(training_set)
print(training_set_y)

testing_set = []

for idx in test_trim_frame.index:
    testing_set.append(
        [
         int(test_trim_frame['time'][idx]),
         test_trim_frame['holiday'][idx],
         test_trim_frame['air_pollution_index'][idx],
         test_trim_frame['humidity'][idx],
         test_trim_frame['wind_speed'][idx],
         test_trim_frame['wind_direction'][idx],
         test_trim_frame['visibility_in_miles'][idx],
         test_trim_frame['temperature'][idx],
         test_trim_frame['rain_p_h'][idx],
         test_trim_frame['snow_p_h'][idx],
         test_trim_frame['clouds_all'][idx],
         ]
    )

