from typing import Callable, List, Dict

def get_population():
  keys = ["col", "bol"]
  values = [10000, 2000]
  return keys, values


PopulationList = List[Dict[str, int]]
PopulationFunction = Callable[[PopulationList, str], PopulationList]

# country can be undefined
#

def population_by_country(data: PopulationList, country: str = None ) -> PopulationList:
  country : str = input("Enter a country: ")
  result = list(filter(lambda x : x['country'] == country, data))
  return result

countries = [
  {
    'country': 'Colombia',
    'population': 50
  },
  {
    'country': 'Bolivia',
    'population': 100
  },
  {
    'country': 'Peru',
    'population': 30
  }
]
# types for population_by_country and country




