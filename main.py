import sys
from DataReader import DataReader
from DataProcessor import DataProcessor

def main():
    health_centers_filename = sys.argv[1]
    population_metrics_census_tract_filename = sys.argv[2]
    population_metrics_citywide_filename = sys.argv[3]
    citywide_disparity_filename = sys.argv[4]
    health_of_city_filename = sys.argv[5]

    health_centers = DataReader(health_centers_filename)
    population_metrics_census_tract = DataReader(population_metrics_census_tract_filename)
    population_metrics_citywide = DataReader(population_metrics_citywide_filename)
    citywide_disparity = DataReader(citywide_disparity_filename)
    health_of_city = DataReader(health_of_city_filename)

    data_processor = None
    try:
        data_processor = DataProcessor(health_centers, population_metrics_census_tract, population_metrics_citywide, citywide_disparity, health_of_city)
    except:
        print('Error: One or more of the provided files cannot be opened or read')

    #code to call method(s) to process data go here

if __name__ == '__main__':
    main()
