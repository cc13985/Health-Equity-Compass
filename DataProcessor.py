class DataProcessor(object):

    def __init__(self, health_centers, population_metrics_census_tract, population_metrics_citywide, citywide_disparity, health_of_city):
        self.health_centers = health_centers.read()
        self.population_metrics_census_tract = population_metrics_census_tract.read()
        self.population_metrics_citywide = population_metrics_citywide.read()
        self.citywide_disparity = citywide_disparity.read()
        self.health_of_city = health_of_city.read()

    # methods to process data go here