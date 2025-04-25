import pandas as pd
from scholarly import scholarly

# Fungsi untuk mencari dan mengambil data dari Google Scholar
def search_scholar(query, max_results=700):
    search_query = scholarly.search_pubs(query)
    results = []
    print("Mencari data...")
    pub = next(search_query)
    print(pub)

    # for i in range(max_results):
    #     try:
    #         pub = next(search_query)
    #         title = pub['bib'].get('title', 'Title not found')
    #         abstract = pub['bib'].get('abstract', 'Abstract not found')
    #         results.append({'title': title, 'abstract': abstract})
    #     except StopIteration:
    #         print("No more results available.")
    #         break
    #     except Exception as e:
    #         print(f"Error occurred: {e}")
    #         continue

    # return results

# File Excel yang sudah ada
# file_path = 'bersih.xlsx'

# Baca data yang sudah ada di bersih.xlsx
# existing_data = pd.read_excel(file_path)

# Ambil data baru dari Google Scholar
query = "sistem informasi"
print(f"Mencari data baru untuk query: {query}")
new_data_results = search_scholar(query, max_results=1)

# Konversi data baru ke DataFrame
