import os
import json
import datetime
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():

    start_date = '2024-02-21' # Example date
    end_date = '2024-02-21' # Same as start_date for one day's data
    api_key = 'YOUR_API'

    url = 'https://api.nasa.gov/neo/rest/v1/feed?' + \
        f'start_date={start_date}&end_date={end_date}&api_key={api_key}'

    # use the requests library to generate the request for data download
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        data = response.json()  # Parse JSON Data
        print('Downloaded data correctly.')
    else:
        print('Failed to retrieve data. Please check your API key and internet connection.')

    # get the piece of data we need from the json object
    asteroids = data['near_earth_objects'][start_date]

    # simple data assimilation, the row values are not completely
    # set into a single value, lots of multi-object columns
    # better assimilation, lets cleanup the data ourselves
    asteroids_data_list = []
    for asteroid in asteroids:

        # print the keys from the json dictionary for each observation
        # dict_keys(['links', 'id', 'neo_reference_id', 'name', 'nasa_jpl_url', 
        # 'absolute_magnitude_h', 'estimated_diameter', 'is_potentially_hazardous_asteroid', 'close_approach_data', 'is_sentry_object'])

        # example use case to insert the data
        # print(asteroid['is_sentry_object'])

        # get the data we need
        asteroid_data_dict = {
            'name': asteroid['name'],
            'id': asteroid['id'],
            'neo_reference_id': asteroid['neo_reference_id'],
            'link': asteroid['links']['self'],
            'nasa_jpl_url': asteroid['nasa_jpl_url'],
            'absolute_magnitude_h': asteroid['absolute_magnitude_h'],
            'is_sentry_object': asteroid['is_sentry_object'],
            'is_potentially_hazardous_asteroid': asteroid['is_potentially_hazardous_asteroid'],
            'diameter': asteroid['estimated_diameter']['meters']['estimated_diameter_max']
        }

        # {'close_approach_date': '2024-02-21', 'close_approach_date_full': '2024-Feb-21 10:10', 'epoch_date_close_approach': 1708510200000, 'relative_velocity': {'kilometers_per_second': '15.3033181047', 'kilometers_per_hour': '55091.9451769682', 'miles_per_hour': '34231.9922684334'}, 'miss_distance': {'astronomical': '0.1598481563', 'lunar': '62.1809328007', 'kilometers': '23912943.705907081', 'miles': '14858814.2064804778'}, 'orbiting_body': 'Earth'}

        print(asteroid_data_dict)
        #print(asteroid['close_approach_data'][0])
        asteroid_data_dict.update(asteroid['close_approach_data'][0])
        asteroids_data_list.append(asteroid_data_dict)

    asteroid_df = pd.DataFrame(asteroids_data_list)

    # question 1: number of asteroids for this day
    num_asteroids = len(asteroid_df)
    print(f"Number of asteroids on {start_date}: {num_asteroids}")

    # question 2: largest asteroid based on diameter
    largest_asteroid = asteroid_df.loc[asteroid_df['diameter'].idxmax()]
    print(f"Largest asteroid: {largest_asteroid['name']} (Diameter: {largest_asteroid['diameter']} meters)")

    sns.histplot(data=asteroid_df, x="diameter")
    plt.show()

    sns.histplot(data=asteroid_df, x="diameter", hue="is_potentially_hazardous_asteroid")
    plt.show()


if __name__ == "__main__":
    main()
