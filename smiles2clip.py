import requests, bs4, pyperclip

# smiles2clip.py scrapes wikipedia for the smiles code of a given compound and copies it to your clipboard.

print('input compound name')
compound = input()

res = requests.get('https://en.wikipedia.org/wiki/'+ compound)
res.raise_for_status()
wikiSoup = bs4.BeautifulSoup(res.text, "lxml")
elems = wikiSoup.select('li div')
SMILES = elems[0].getText()
pyperclip.copy(SMILES)
print(SMILES)
