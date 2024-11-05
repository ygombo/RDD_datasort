import json
import os 

directory = 'test'

for root, dirs, files in os.walk(directory):
    for filename in files:

        # print(filename)

        with open(os.path.join(root, filename), "r", encoding="utf8") as read_file:
            input_file_dict = json.load(read_file)

        a = input_file_dict["objects"]
        b = input_file_dict["size"]
        height = b["height"]
        width = b["width"]
        bblist = []
        for i in range(0,len(a)):
            dispName = a[i]["classTitle"]
            xmin_val = a[i]["points"]["exterior"][0][0]
            ymin_val = a[i]["points"]["exterior"][0][1]
            xmax_val = a[i]["points"]["exterior"][1][0]
            ymax_val = a[i]["points"]["exterior"][1][1]
            bbox = {
                    "displayName": dispName,
                    "xMin": xmin_val/width,
                    "yMin": ymin_val/height,
                    "xMax": xmax_val/width,
                    "yMax": ymax_val/height 
            }
            bblist.append(bbox)
        splitname = os.path.splitext(filename)[0]
        # print(splitname)
        imageURI = os.path.join("gs://data_jalan_rusak/test/img",splitname)
        output_dict = {
            "imageGcsUri": imageURI,
            "boundingBoxAnnotations": bblist,
            "dataItemResourceLabels":{"aiplatform.googleapis.com/ml_use": "test"}
        }
        # out_folder = "output/test"
        out_folder = os.path.join("output/",directory)
        with open(os.path.join(out_folder,filename + '.gcp.json'), 'w') as output_json_file:
            json.dump(output_dict, output_json_file)

