import requests
import sys

def download_file(url, file_path):
    # if not url:
    #     raise ValueError("URL is required")
    # if not file_path:
    #     raise ValueError("File path is required")
    # response = requests.get(url)
    # response.raise_for_status()
    # with open(file_path, 'wb') as f:
    #     f.write(response.content)
    # print(f"Downloaded {url} to {file_path}")
    print("in download_file!")

if __name__ == '__main__':
    print("in __main__!")
    url = sys.argv[1] if len(sys.argv) > 1 else None
    file_path = sys.argv[2] if len(sys.argv) > 2 else None
    download_file(url, file_path)