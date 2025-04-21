import requests

def doi_to_bibtex(doi):
    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    response = requests.get(url, headers=headers)
    return response.text

input_doi = "http://dx.doi.org/10.2139/ssrn.5209683"
pdrint(doi_to_bibtex(input_doi,))

