import os
import gzip
import xml.etree.ElementTree as ET
import requests

save_as_gz = False  # Set to True to save an additional .gz version

# Use the same directory as the script for saving files
tvg_ids_file = os.path.join(os.path.dirname(__file__), 'tvg-ids.txt')
output_file = os.path.join(os.path.dirname(__file__), 'epg.xml')
output_file_gz = output_file + '.gz'

def fetch_and_extract_xml(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    if url.endswith('.gz'):
        try:
            decompressed_data = gzip.decompress(response.content)
            return ET.fromstring(decompressed_data)
        except Exception as e:
            print(f"Failed to decompress and parse XML from {url}: {e}")
            return None
    else:
        try:
            return ET.fromstring(response.content)
        except Exception as e:
            print(f"Failed to parse XML from {url}: {e}")
            return None

def filter_and_build_epg(urls):
    with open(tvg_ids_file, 'r', encoding='utf-8') as file:
        valid_tvg_ids = set(line.strip() for line in file)

    root = ET.Element('tv')

    for url in urls:
        epg_data = fetch_and_extract_xml(url)
        if epg_data is None:
            continue

        for channel in epg_data.findall('channel'):
            tvg_id = channel.get('id')
            if tvg_id in valid_tvg_ids:
                root.append(channel)

        for programme in epg_data.findall('programme'):
            tvg_id = programme.get('channel')
            if tvg_id in valid_tvg_ids:
                root.append(programme)

    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"New EPG saved to {output_file}")

    if save_as_gz:
        with gzip.open(output_file_gz, 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
        print(f"New EPG saved to {output_file_gz}")

#m3u4u_epg = os.getenv("M3U4U_EPG")

urls = [
    'https://www.dropbox.com/scl/fi/7r7h1jdufwoplnhhxkism/m3u4u-103216-593044-EPG.xml?rlkey=606vswc00na76l51otnz116ed&st=q273qocn&dl=1',
    'https://www.dropbox.com/scl/fi/tsj8796ea6krin4pv4t32/m3u4u-103216-595541-EPG.xml?rlkey=tu42144366j5w0n2s8fc1ogvp&st=2gg7ylx2&dl=1',
		'https://epgshare01.online/epgshare01/epg_ripper_US1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_US_LOCALS2.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_CA1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_IE1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_DE1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_ZA1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_CL1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_BR1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_BG1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_DK1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_GR1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_IL1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_IT1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_MY1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_MX1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_NL1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_NZ1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_CZ1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_SG1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_PK1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_RO1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_CH1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_PL1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_SE1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_UY1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_CO1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_PT1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_ES1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_TR1.xml.gz',
		'https://epgshare01.online/epgshare01/epg_ripper_FANDUEL1.xml.gz',
		'https://epg.pw/api/epg.xml?channel_id=8486',
		'https://epg.pw/api/epg.xml?channel_id=12358',
		'https://epg.pw/api/epg.xml?channel_id=9206',
]

if __name__ == "__main__":
    filter_and_build_epg(urls)
