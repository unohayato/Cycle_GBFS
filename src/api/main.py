from typing import Dict, Any
import requests
import pandas as pd

def get_api(url: str) -> Dict[str, Any]:
  """
  指定されたURLからAPIを呼び出し、JSON形式でデータを取得する。

  Args:
      url (str): APIのエンドポイントURL。

  Returns:
      Dict[str, Any]: APIから取得したデータを含む辞書。
  """
  response = requests.get(url)
  json = response.json()
  return json

def main() -> Dict[str, Any]:
  """
  主要な実行関数。特定のURLからAPIを呼び出し、データを取得する。

  Returns:
    Dict[str, Any]: 'get_api'関数から取得したデータ。
  """

  url = "https://api-public.odpt.org/api/v4/gbfs/hellocycling/station_information.json"
  response = get_api(url)
  return response

if __name__ == "__main__":
  response = main()
  print(response["data"]["stations"][0])