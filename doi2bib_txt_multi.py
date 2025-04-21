from pathlib import Path
import bibtexparser

def doi_to_bibtex(doi):
    import requests

    # 處理 DOI 開頭含有 https:// 的情況
    if doi.startswith("http"):
        doi = doi.split("doi.org/")[-1].strip()

    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 若請求失敗則拋出例外
    return response.text

# print(doi_to_bibtex("http://dx.doi.org/10.2139/ssrn.5209683",))


# 讀取 DOI 清單 (每行一個 DOI)
# # DOI 清單直接指定
# doi_list = [
#     "https://doi.org/10.1007/s11837-019-03704-4",
#     "https://doi.org/10.1016/j.matdes.2024.113326",
# ]

# DOI 清單外部讀取
with open("doi_list.txt", "r") as f:
    doi_list = [line.strip() for line in f if line.strip()]

# 儲存 BibTeX 條目的字串清單
bibtex_entries = []

for doi in doi_list:
    try:
        bib_entry = doi_to_bibtex(doi)
        bibtex_entries.append(bib_entry)
        print(f"✔️ Success: {doi}")
    except Exception as e:
        print(f"❌ Failed to fetch {doi}: {e}")
        bibtex_entries.append(f"% Failed to fetch {doi}\n")

# Save to bib files
output_path = Path("Rreferences_list.bib")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("".join(bibtex_entries))

print(f"✔️ BibTeX entries saved to: {output_path.resolve()}")


# Save to txt files
# 直接將 bibtex_entries 合併為字串
bibtex_data = "".join(bibtex_entries)

# 使用 bibtexparser 處理 bibtex 字串（不需從檔案讀取）
bib_database = bibtexparser.loads(bibtex_data)

# 格式化成參考文獻文字
formatted_refs = []
for i, entry in enumerate(bib_database.entries, start=1):
    print(entry)
    try:
        authors = entry.get('author', 'N/A').replace('\n', ' ')
        title = entry.get('title', 'N/A').strip('{}')
        journal = entry.get('journal', 'N/A')
        volume = entry.get('volume', 'N/A')
        year = entry.get('year', 'N/A')
        pages = entry.get('pages', 'N/A')
        doi = entry.get('doi', '')
        url = f"https://doi.org/{doi}" if doi else ""
        print()
        ref = f"[{i}] {authors}, \"{title},\" {journal}, {volume} ({year}), {pages}. {url}"
        formatted_refs.append(ref)
    except Exception as e:
        formatted_refs.append(f"[{i}] Failed to parse entry. Error: {e}")

# 儲存格式化參考文獻到 .txt
output_txt_path = Path("Rreferences_list.txt")
with open(output_txt_path, "w", encoding="utf-8") as f:
    f.write("\n".join(formatted_refs))

print(f"📄 References saved to: {output_txt_path.resolve()}")