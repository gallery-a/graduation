import cv2
import os
def makedirifnoExist(path):
    if(not os.path.exists(path)):
        os.makedirs(path)
    else:
        os.system("rm -r "+path)


com1 = "python3 export_inference_graph.py --input_type image_tensor --pipeline_config_path /root/workspace/models/research/object_detection/samples/configs/faster_rcnn_resnet101_coco_xuelang.config --trained_checkpoint_prefix /root/workspace/models/research/object_detection/output/models/faster_rcnn12"

com2s = ["23","24","_copy"]


for com2 in com2s:
	path = "/root/workspace/models/research/object_detection/output/models/faster_rcnn12"+com2+"/checkpoint"

	f = open(path)
	lines = f.readlines()
	for line in lines:
		com3 = line.split("\"")[1]
		com = com1+com2+com3
		print(com)