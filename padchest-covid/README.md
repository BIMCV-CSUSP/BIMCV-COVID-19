<div class="clearfix" style="padding: 0px; padding-left: 100px; display: flex; flex-wrap: nowrap; justify-content: space-evenly; align-items:center">
<a href="http://bimcv.cipf.es/"><img src="https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/chestRx/logoinst.png?raw=true"</a><a href="http://ceib.san.gva.es"></a></div>

# Data Sources. [BIMCV-PadChest](http://ceib.bioinfo.cipf.es/covid19)
You can download the images from this link --> http://ceib.bioinfo.cipf.es/covid19

The tables that will be used to carry out the required model training are stored in one folder that contain the images. There are a total of 10 tables called "pneumo_dataset_balanced_x.tsv" where x takes values from 0 to 9. 
These files contain different partitions of the images and can be used individually or together if a "10-fold cross validation" is required. 

The most important data to take into account for the training phase are:

**Image ID:** name of the image file.

**StudyID:** study identifier.

**Patient ID:** patient identifier.

**Projection:** patient’s position when taking the radiography.

**Tags:** radiological findings found in the image.

**Group:** label of the class to which the image belongs. These labels can be:

* C - Control
* N - Pneumonia
* I - Infiltration
* NI - Pneumonia and infiltration

Partition: partition to which the image belongs. These values are:
* tr - Training
* dev - Development
* te - Test
## Run the code

To train the model example, you need to execute the following instruction:

python3 pneumo_cnn_classifier_training.py «FILE_TSV_BALANCED»
