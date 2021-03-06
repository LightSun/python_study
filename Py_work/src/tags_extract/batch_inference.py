#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# fnames = ["C0076.MP4","C0077.MP4","C0078.MP4","C0079.MP4","C0080.MP4","C0081.MP4","C0082.MP4","C0083.MP4","C0084.MP4","C0085.MP4","C0086.MP4","C0087.MP4","C0088.MP4","C0089.MP4","C0090.MP4","C0091.MP4","C0092.MP4","C0093.MP4","C0094.MP4","C0095.MP4","C0096.MP4","C0097.MP4","C0098.MP4","C0099.MP4","C0100.MP4","C0101.MP4","C0103.MP4","C0104.MP4","C0105.MP4","C0106.MP4","C0107.MP4","C0108.MP4","C0109.MP4","C0110.MP4","C0111.MP4","C0112.MP4","C0113.MP4","C0114.MP4","C0115.MP4","C0116.MP4","C0117.MP4","C0118.MP4","C0119.MP4","C0120.MP4","C0121.MP4","C0122.MP4","C0123.MP4","C0124.MP4","C0125.MP4","C0126.MP4","C0127.MP4","C0128.MP4","C0129.MP4","C0130.MP4","C0131.MP4","C0132.MP4","C0133.MP4","C0134.MP4","C0135.MP4","C0136.MP4","C0137.MP4","C0138.MP4","C0139.MP4","C0140.MP4","C0141.MP4","C0142.MP4","C0143.MP4","C0144.MP4","C0145.MP4","C0146.MP4","C0147.MP4","C0148.MP4","C0149.MP4","C0150.MP4","C0151.MP4","C0152.MP4","C0153.MP4","C0154.MP4","C0155.MP4","C0156.MP4","C0157.MP4","C0158.MP4","C0159.MP4","C0160.MP4","C0161.MP4","C0162.MP4","C0163.MP4","C0164.MP4","C0165.MP4","C0166.MP4","C0167.MP4","C0168.MP4","C0169.MP4"]
fnames =["character_01.mp4"]

for fname in fnames:
	prefix = fname.split(".")[0]
	input_file = "%s_output.tfrecord" % prefix
	output_file = "%s_predictions.csv" % prefix
	cmd = "python D:\\tensorflow\\youtube-8m\\inference.py --output_file=D:\\tmp\\frame_level_logistic_model\\%s --input_data_pattern=\"D:\\%s\" --train_dir=D:\\tmp\\frame_level_logistic_model --frame_features=True --model=FrameLevelLogisticModel --feature_names=\"rgb\" --feature_sizes=\"1024\"" % (output_file, input_file)
	print(cmd)
	print("\n")
	os.system(cmd)
