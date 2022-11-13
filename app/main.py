import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv_dict('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x:x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  
  country = input('Type Country => ')
  country_data = utils.get_data_country(data, country)
  
  if len(country_data) > 0:
    new_data_country = utils.get_new_data_country(country_data)
    population_data = utils.format_key(new_data_country)
    labels = population_data.keys()
    values = population_data.values()
    charts.generate_bar_chart(country, labels, values)

if __name__ == '__main__':
  run()

