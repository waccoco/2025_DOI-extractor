# 2025_DOI-extractor
input doi to get full information

# DOI to BibTeX Converter

A simple Python script to convert a list of DOIs into BibTeX entries and export them as both `.bib` and `.txt` files for academic referencing.

## 📌 Features

- Fetch BibTeX entries from DOIs using the [doi.org](https://doi.org/) API
- Output to `.bib` file and save as `.bib` and `.txt` (IEEE-like style)
- Supports batch processing from a plain text file (doi_list.txt)

## 🛠️ Requirements

- Python 3.7+
- `requests`
- `bibtexparser`

Install dependencies:
```bash
pip install requests bibtexparser
```

🚀 Usage
1. Prepare DOI list
Prepare a text file doi_list.txt with one DOI per line:
10.1007/s11837-019-03704-4
10.1016/j.matdes.2024.113326
...
2. Run the script
python doi_to_bibtex.py

3. Output files
After execution, the following files will be generated:
 - References_list.bib — raw BibTeX entries for LaTeX
 - References_list.txt — nicely formatted references (for Word, PDF, etc.)

📄 Example Output (References_list.txt)
[1] J. Smith, "Machine learning in materials science," Materials Today, 45 (2024), 112-120. https://doi.org/10.1016/j.matdes.2024.113326

📄 Example Output (References_list.bib)
@article{Chang_2019, title={Prediction of the Composition and Hardness of High-Entropy Alloys by Machine Learning}, volume={71}, ISSN={1543-1851}, url={http://dx.doi.org/10.1007/s11837-019-03704-4}, DOI={10.1007/s11837-019-03704-4}, number={10}, journal={JOM}, publisher={Springer Science and Business Media LLC}, author={Chang, Yao-Jen and Jui, Chia-Yung and Lee, Wen-Jay and Yeh, An-Chou}, year={2019}, month=jul, pages={3433–3442} }


📂 Repository Structure
├── doi_list.txt               # Your input list of DOIs
├── doi_to_bibtex.py          # The main script
├── output_references.bib     # BibTeX output
└── formatted_references.txt  # Formatted output

🔗 License
This project is licensed under the MIT License.
Feel free to use, modify, or contribute.
