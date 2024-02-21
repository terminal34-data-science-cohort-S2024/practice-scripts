"""
Exercise #2a: Basic Data Retrieval with JSON
Scenario

Your task is to retrieve data about animal observations for a specific species using the Global Biodiversity Information Facility (GBIF) API and perform basic analysis on this data.

API Endpoint

The GBIF API endpoint for species occurrence data is:
```
https://api.gbif.org/v1/occurrence/search?scientificName=SPECIES_NAME
```
Replace `SPECIES_NAME` with the scientific name of an animal species (e.g., "Panthera leo" for lions).

Tasks
Fetch Animal Observation Data:
Use Python to make a request to the GBIF API and retrieve observation data for a specific animal species.
Parse JSON Data:
Parse the JSON data returned from the API into a Python data structure.
Data Analysis:
Convert the data into a Pandas DataFrame.
Calculate and print the total number of observations retrieved.
Analyze the geographical distribution of observations (e.g., count observations by country).

Implementation

You will need to implement a Python solution for this exercise. Ensure you have the `requests` and `pandas` libraries installed, and optionally `matplotlib` for plotting.
"""
# Purpose: Get animal information from GBIF API
# Author: Jordan A Caraballo Vega
# Version: 0.0.1
import sys
import requests
import pandas as pd


def main():

    # call the data
    species_name = 'Panthera leo'
    print(f'Species name: {species_name}')

    # construct API url
    url = f'https://api.gbif.org/v1/occurrence/search?scientificName={species_name}'
    print(url)

    # request to the API
    response = requests.get(url)
    print(response)

    # load the data
    if response.status_code == 200:

        print("Processing")

        data = response.json()
        print(data)

        observations = data['results']
        print(observations)

        species_df = pd.DataFrame(observations)
        print(species_df)

        print(species_df.columns)

    else:

        sys.exit("Not processing, problems with API request")

    # analyze the data

    return


if __name__ == "__main__":

    main()
