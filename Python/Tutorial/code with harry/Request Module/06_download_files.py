import requests
from tqdm import tqdm

url = "https://www.imf.org/external/pubs/ft/fandd/2008/03/pdf/cline.pdf"
response = requests.get(url, stream=True)

# Get the total size of the file
total_size = int(response.headers.get('Content-Length', 0))

# Define the chunk size
chunk_size = 128

# Open a file to write the downloaded content
with open('file.pdf', 'wb') as fd:
    # Create a tqdm progress bar
    with tqdm(total=total_size, unit='B', unit_scale=True, desc='Downloading') as pbar:
        for chunk in response.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
            pbar.update(len(chunk))

print("Download completed successfully!")
