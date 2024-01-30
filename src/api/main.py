import requests
import pandas as pd

def main():
  url = "https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_information.json"
  response = requests.get(url)
  json = response.json()
  return json

if __name__ == "__main__":
  response = main()
  print(response[0])