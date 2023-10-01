import requests

def handler(pd: "pipedream"):
  token = f'{pd.inputs["pipefy"]["$auth"]["token"]}'
  authorization = f'Bearer {token}'
  headers = {"Authorization": authorization}
  data = {"query": f'{{ me {{ name }} }}'}
  r = requests.post('https://api.pipefy.com/graphql', headers=headers, data=data)
  # Export the data for use in future steps
  return r.json()
