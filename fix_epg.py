#  fix_epg.py  17.02.26
#  basic program to set subtitle for title
#  if title = Movie or empty.
#  Input is local epg.xml
#  The result is fixed_epg.xml
#  which contains all EPG records.
#####################


import xml.etree.ElementTree as ET

tree = ET.parse('epg.xml')
root = tree.getroot()


for programme in root.findall('programme'):
    # Get the channel attribute from the <programme> tag
    channel_id = programme.get('channel', '')
    title = programme.find('title')
    subtitle = programme.find('sub-title')
    if title is not None and title.text == "Movie" and subtitle is not None:
        title.text = subtitle.text  # Move the movie name to the Title
        print(f"Fixed [{channel_id}]:  {title.text}")
    else:
        print(f"Non Fixed [{channel_id}]:{title.text}")

tree.write('fixed_epg.xml', encoding='utf-8', xml_declaration=True)
