import os

import requests


def github_request(url):
  """
  sample github api endpoint @ repo tag
  #      https://api.github.com/repos/:owner/:repo/git/tags/   WRONG
  #      https://api.github.com/repos/:owner/:repo/tags        CAUTION no / attheend
  # url = 'https://api.github.com/repos/pyenv/pyenv/tags'
  """

  # load_dotenv()
  GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')

  header = {
    #TODO below header NOT effective ie it seems github now allow to call endpoint without a github api key
    'Authorization'        : f'Bearer {GITHUB_API_KEY}',
    'Accept'               : 'application/vnd.github+json',
    'X-GitHub-Api-Version' : '2022-11-28',
  }

  res = requests.get(url, header)
  return res.json(), res.status_code
