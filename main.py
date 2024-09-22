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

    data_processor = DataProcessor(health_centers, population_metrics_census_tract, population_metrics_citywide, citywide_disparity, health_of_city)

    #code to call method(s) to process data go here
    print(data_processor.health_centers)
    print(data_processor.population_metrics_census_tract)
    print(data_processor.population_metrics_citywide)
    print(data_processor.citywide_disparity)
    print(data_processor.health_of_city)

if __name__ == '__main__':
    main()
