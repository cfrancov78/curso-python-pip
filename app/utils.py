def get_population():
  keys= ['col','bol']
  values = [300,400]
  return keys, values

def population_by_country(data,country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result

def get_data_country(data, country):
  country_data = list(filter(lambda item: item['Country/Territory'] == country, data))
  return country_data

def get_new_data_country(country_data):
  new_data_country = dict(filter(lambda item: 'Population' in item[0] and 'Percentage' not in item[0], country_data[0].items()))
  return new_data_country

def format_key(new_data_country):
  new_data = new_data_country.copy()
  new_data = {k[0:4]: int(v) for k, v in new_data.items()}
  return new_data