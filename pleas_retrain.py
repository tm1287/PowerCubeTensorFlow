python tensorflow/examples/label_image/label_image.py \
--graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt \
--input_layer=Mul \
--output_layer=final_result \
--input_mean=128 --input_std=128 \
--image=$HOME/Top-25-Most-Beautiful-Daisy-Flowers.jpg
