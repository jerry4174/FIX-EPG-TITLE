#  fix_epg1.py  17.02.26
#  basic program to set subtitle for title
#  if title = Movie or empty.
#  Repair only for HBO channels.
#  Input is local epg.xml
#  The result is fixed_epg1.xml
#  which contains all EPG records.
#
#####################



import xml.etree.ElementTree as ET

tree = ET.parse('epg.xml')
root = tree.getroot()

for programme in root.findall('programme'):
    # Get the channel attribute from the <programme> tag
    channel_id = programme.get('channel', '')

    # Check if 'HBO' is in the channel ID (case-insensitive check)
 #   if "HBO" in channel_id.upper():
    title = programme.find('title')
    subtitle = programme.find('sub-title')

    if title is not None and title.text == "Movie" and subtitle is not None:
            title.text = subtitle.text  # Move the movie name to the Title
            print(f"Fixed [{channel_id}]: {title.text}")

tree.write('fixed_epg1.xml', encoding='utf-8', xml_declaration=True)