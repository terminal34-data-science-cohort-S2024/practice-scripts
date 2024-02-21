"""
Exercise: Analyzing Weather Data with NumPy

Objective: You are provided with a week's worth of weather data from a small town. The data includes daily maximum temperatures (in Celsius), minimum temperatures, and precipitation levels. Your task is to use NumPy to analyze this data.

Data:

- Max Temperatures: `[25, 28, 22, 19, 30, 27, 26]`
- Min Temperatures: `[15, 18, 14, 12, 20, 17, 16]`
- Precipitation (mm): `[5, 0, 12, 2, 0, 0, 1]`

Tasks:

1. Find the mean max temperature for the week.
2. Find the day with the highest temperature variation (difference between the max and min temperature).
3. Calculate the total precipitation for the week.
4. Determine if any day had precipitation levels above 5 mm.
"""

import numpy as np

max_temps = np.array([25, 28, 22, 19, 30, 27, 26])
min_temps = np.array([15, 18, 14, 12, 20, 17, 16])
precipitation = np.array([5, 0, 12, 2, 0, 0, 1])

# **Task 1: Mean Max Temperature**
# Calculate the mean of the max temperatures.

mean_max_temp = np.mean(max_temps)
print(f"Mean max temperature: {mean_max_temp} Celsius")

# **Answer 1:**
# Mean max temperature: 25.285714285714285 Celsius

# **Task 2: Day with Highest Temperature Variation**
# Find the day with the highest difference between max and min temperatures.

temp_variations = max_temps - min_temps
day_of_highest_variation = np.argmax(temp_variations) + 1 # Adding 1 to match day counting from 1
print(f"Day with highest temperature variation: Day {day_of_highest_variation}")

# **Answer 2:**
# Day with highest temperature variation: Day 5

# **Task 3: Total Precipitation**
# Calculate the total precipitation for the week.

total_precipitation = np.sum(precipitation)
print(f"Total precipitation for the week: {total_precipitation} mm")

# **Answer 3:**
# Total precipitation for the week: 20 mm

# **Task 4: Days with Precipitation Above 5 mm**
# Determine days with more than 5 mm of precipitation.

days_with_more_precip = np.where(precipitation > 5)[0] + 1 # Adding 1 for day counting
print(f"Days with more than 5 mm of precipitation: Days {days_with_more_precip}")

# **Answer 4:**
# Days with more than 5 mm of precipitation: Days [3]

