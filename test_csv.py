import os
import xml.etree.ElementTree as ET
import csv

# Directory paths
image_dir = 'data/images/test'
xml_dir = 'data/images/test'
csv_file = 'data/annotations/test_labels.csv'

# CSV column headers
csv_columns = ['image_path', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

# Open the CSV file for writing
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()

    # Iterate over all XML files
    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_dir, xml_file)
            
            # Parse the XML file
            tree = ET.parse(xml_path)
            root = tree.getroot()
            
            # Find the image file name and derive its path
            image_file = root.find('filename').text
            image_path = os.path.join(image_dir, image_file)
            size = root.find('size')

            # Iterate over all object elements in the XML
            for member in root.findall('object'):
                # Extract bounding box coordinates and class label
                bbox = member.find('bndbox')
                
                width = int(size.find('width').text)
                height = int(size.find('height').text)
                xmin = int(bbox.find('xmin').text)
                ymin = int(bbox.find('ymin').text)
                xmax = int(bbox.find('xmax').text)
                ymax = int(bbox.find('ymax').text)
                class_label = member.find('name').text

                # Write the data to the CSV file
                writer.writerow({
                    'image_path': image_path,
                    'width': width,
                    'height': height,
                    'class': class_label,
                    'xmin': xmin,
                    'ymin': ymin,
                    'xmax': xmax,
                    'ymax': ymax,
                    
                })

print(f"CSV file created: {csv_file}")