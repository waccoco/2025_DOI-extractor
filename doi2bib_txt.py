import requests

def doi_to_bibtex(doi):
    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    response = requests.get(url, headers=headers)
    return response.text

pdrint(doi_to_bibtex("http://dx.doi.org/10.2139/ssrn.5209683",))

