import  utils 

def main():

  keys , values =  utils.get_population()
  print (f" Keys : {keys} , Values : {values}" )

def run():

  countries = utils.countries

  result = utils.population_by_country( countries  )

  print (f"print in run() { result } ")




if __name__ == '__main__':
  run()