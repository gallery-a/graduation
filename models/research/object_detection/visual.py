import numpy as np
import tensorflow as tf
import cv2 
from datetime import datetime 

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

 
# Read the graph.
with tf.gfile.FastGFile('/root/workspace/models/research/object_detection/output/frozenmodel/fasterrcnn1224/frozen_inference_graph.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
 
save_path = "/root/workspace/models/research/object_detection/output/boxes/fasterrcnn12_copy_272744/fasterrcnn1224_678495_2.txt"

f = open(save_path,"w")

with tf.Session() as sess:
    # Restore session
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='')
 
    # Read and preprocess an image.
    path = "/root/workspace/Cascade-RCNN_Tensorflow/data/xuelang1/testJPEGImages"
    l = len(os.listdir(path))
    begin = datetime.now()
    for imgname in os.listdir(path):
        imgpath = os.path.join(path,imgname)
        img = cv2.imread(imgpath)
        inp = img #cv2.resize(img, (300, 300))
        inp = inp[:, :, [2, 1, 0]]  # BGR2RGB

        # Run the model
        out = sess.run([sess.graph.get_tensor_by_name('num_detections:0'),
                        sess.graph.get_tensor_by_name('detection_scores:0'),
                        sess.graph.get_tensor_by_name('detection_boxes:0'),
                        sess.graph.get_tensor_by_name('detection_classes:0')],
                       feed_dict={'image_tensor:0': inp.reshape(1, inp.shape[0], inp.shape[1], 3)})
        

        num_detections = int(out[0][0])
        for i in range(num_detections):
            classId = int(out[3][0][i])
            score = float(out[1][0][i])
            bbox = [float(v) for v in out[2][0][i]]
            f.write(imgname[:-4]+" "+str(score)+" "+str(bbox[1] * img.shape[1])+" "+str( bbox[0] * img.shape[0])+" "+str(bbox[3] * img.shape[1])+" "+ str(bbox[2] * img.shape[0])+"\n")
        
        
print("per:%s"% (str(l/(datetime.now()-begin).seconds)) )
f.close()