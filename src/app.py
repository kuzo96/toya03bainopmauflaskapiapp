"""
00 fork this replit to your replit 

01a do your code!
01b your final goal is to hit Run and have all tests PASS IN GREEN

02a git commit push to github repo - view guide https://drive.google.com/file/d/1PZZ2xIlamM0pPtLlbpDodseCKcIVhTzW/view?usp=sharing
02b get url to your git repo in 02a above - we call it :gitrepourl

03 paste :gitrepourl into this google form and submit it
   https://forms.gle/cuxhb8cbYaJLHRYz5
   ma_debai = toya03bainopmauflaskapiapp

---
python -m pip install --upgrade pip pipenv ; python -m pipenv --version
python -m pipenv install  # install packages in Pipfile
python -m pipenv --venv
  # eg /home/namgivu/Desktop/nam/toya04bainopmauflaskapiapp/.venv/bin/python
  # eg /home/namgivu/Desktop/nam/toya04bainopmauflaskapiapp/.venv/Script/python.exe
"""
import os
from flask import Flask, jsonify
from src.helper import github_request
app = Flask(__name__)

@app.route('/')
def index():
  return jsonify({})


@app.route('/release')
def release():
  (dataList, retCode
   ) = github_request('https://api.github.com/repos/pyenv/pyenv/releases')
  #print(f"retCode = {retCode}")
  outList = []
  if retCode == 200:
    for r in dataList:
      js = dict(r)
      created_at = js['created_at']
      tag_name = js['tag_name']
      body = js['body']
      #create a dict from param created_at, tag_name, body
      d = {'created_at': created_at, 'tag_name': tag_name, 'body': body}
      outList.append(d)

  return outList, retCode


@app.route('/most_3_recent/release')
def most_3_recent__release():
  (releaseList, retCode) = release()
  if retCode == 200:
    return releaseList[:3], retCode
  else:
    return [], retCode


if __name__ == '__main__':
  app.run(debug=True, port=os.environ.get('PORT', 5000))
