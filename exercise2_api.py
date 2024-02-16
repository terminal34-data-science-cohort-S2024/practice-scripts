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