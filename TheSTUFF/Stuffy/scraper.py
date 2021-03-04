
from multipledispatch import dispatch 
import urllib.request	

git_raw = ['https://raw.githubusercontent.com/C-A-Oliveira/{repo}/{file}',
            'https://raw.githubusercontent.com/C-A-Oliveira/{path}']

## Reads the raw code of a given repo from the author of the project... AKA me

def get_file_from(repo, file):
    request = urllib.request.urlopen(git_raw[0].format(repo = repo, file = file))
    return request.read().decode("utf8")



# print(get_file_from('Hub/master/TheSTUFF', 'main.py'))