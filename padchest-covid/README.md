<div class="clearfix" style="padding: 0px; padding-left: 100px; display: flex; flex-wrap: nowrap; justify-content: space-evenly; align-items:center">
<a href="http://bimcv.cipf.es/"><img src="https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/chestRx/logoinst.png?raw=true"</a><a href="http://ceib.san.gva.es"></a></div>

# Data Sources. [BIMCV-PadChest](http://ceib.bioinfo.cipf.es/covid19/padchest_neumonia.zip)

Mirrow at [BSC](https://www.bsc.es/)-[TranBioNet](https://inb-elixir.es/transbionet) --> https://b2drop.bsc.es/index.php/s/BIMCV-PadChest

You can download the Raw images from this link --> http://ceib.bioinfo.cipf.es/covid19/padchest_neumonia.zip

You can download the resize images from  --> http://ceib.bioinfo.cipf.es/covid19/resized_padchest_neumo.tar.gz

You can download other resize images --> http://ceib.bioinfo.cipf.es/covid19/resized_padchest_neumo_32.tar.gz
# UPDATES

**Updates 04/04/2020**

Good proposals to improve dataset partition from [JC Perez](https://github.com/jcperez-iti-upv) --> https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/padchest-covid/README.md#pretrained-models

**Updates 03/04/2020**

The mirror at Barcelona Supercomputing Center is ready to distribute this dataset. Thanks to Salva, Eva and Paco Garcia

**Updates 01/04/2020**

Great, new models from Jon Ander, Thanks.

**Updates 30/03/2020**

Good, MIT news --> https://www.technologyreview.es/s/12049/una-nueva-ia-podria-detectar-el-covid-19-en-una-radiografia-de-torax?fbclid=IwAR3rsZKlqjtFO54ToAyV1pT4DNxRUneTg4RcUeaeA_eJiqm0nn93LUB-lD8

**Updates 29/03/2020**

Other pneumonia dataset --> https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

Interesting COVID-Net --> https://github.com/lindawangg/COVID-Net

**Updates 28/03/2020**

Don't miss this topic  --> https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/issues/14#issue-589542523

**Updates 27/03/2020**

Don't miss this news from MIT Tech. --> https://www.technologyreview.com/s/615399/coronavirus-neural-network-can-help-spot-covid-19-in-chest-x-ray-pneumonia/?utm_medium=tr_social&utm_campaign=site_visitor.unpaid.engagement&utm_source=Twitter#Echobox=1585319560

**New updates 26/03/2020**

Don't miss the next video from ESR --> https://www.youtube.com/watch?v=QFW8CmZ0cyM&feature=youtu.be

new data_augmentation_simplified.py from Roberto Paredes's contribution

**New updates 24/03/2020**

Following Roberto Paredes's suggestions we have resized the dataset 

**New updates 23/03/2020**

Following Roberto's suggestions we will leave a single partition, it will be easier.

**---**

## One example for helping to test
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


## RESULTS

### 4 classes {C,N,I,NI}

|  Participant | Model name  | Train Accuracy|Dev Accuracy | Test Accuracy  | Comments  |
|---|---|---|---|---|---|
| rparedes  | model1 | --- | 67.97%  | ----  |  512x512 images, numpy |
|TeamBioinformaticsAnd_AI|VGG16| 81.44% | 62.76%|62.44%|Resize 524x524 -> 224x224 with Transfer Learning and without Data Augmentation, dataBase=Resize_padchest_neumo(2.81GB)|
|   |   |   |   |   |   |

### 2 classes C versus [I,NI,N]
|  Participant | Model name | Train Accuracy|Dev Accuracy | Test Accuracy  | Comments  |
|---|---|---|---|---|---|
| jonandergomez@prhlt  | model2 | 99.63% | 83.96%  | ----  |  512x512 images (useless model, too overfitting) |
| jonandergomez@prhlt  | model2b | 100.0% | 84.89%  | ----  |  512x512 images (useless model, too overfitting) |
|TeamBioinformaticsAnd_AI| Model5-Alzaheimer2D |81.74%|79.05%|78.21%| Resize 524x524 -> 224x224 without Transfer Learning and Data Augmentation (Train 81.74%), dataBase=Resize_padchest_neumo(2.81GB)  |
|TeamBioinformaticsAnd_AI| VGG16 |85.04% |82.84%|82.46%|  Resize 524x524 -> 224x224 with Transfer Learning and Data Augmentation, dataBase=Resize_padchest_neumo(2.81GB), Data augmentation with ImageDataGenerator TF+Keras)  |

### 2 classes C versus [NI,N]
|  Participant | Model name | Train Accuracy|Dev Accuracy | Test Accuracy  | Comments  |
|---|---|---|---|---|---|
| jonandergomez@prhlt  | model5a | 84.92% | 85.72%  | ----  |  512x512 images (details will be published soon) |
| jonandergomez@prhlt  | model7b | 91.90% | 87.52%  | ----  |  512x512 images (details will be published soon) |
| jonandergomez@prhlt  | model7c | 88.25% | 87.01%  | ----  |  512x512 images (details will be published soon) |


### 2 classes {C,N}
|  Participant | Model name| Train Accuracy | Dev Accuracy | Test Accuracy  | Comments  |
|---|---|---|---|---|---|
| jonandergomez@prhlt | model2 | 98.89% | 83.69% | 81.70% | 512x512 images (details will be published soon) | 
| jonandergomez@prhlt | model5b | 87.12% | 86.62% | ---- | 512x512 images (details will be published soon) | 
| jonandergomez@prhlt | model5c | 87.80% | 86.52% | ---- | 512x512 images (details will be published soon) | 
| jonandergomez@prhlt | model7b | 90.40% | 88.42% | ---- | 512x512 images (details will be published soon) | 
| jonandergomez@prhlt | model7c | 93.12% | 88.84% | ---- | 512x512 images (details will be published soon) | 
|TeamBioinformaticsAnd_AI |VGG16|87.09% |86.14%|86.16%|Resize 524x524 -> 224x224 with Transfer Learning and Data Augmentation, dataBase=Resize_padchest_neumo(2.81GB), Data augmentation with ImageDataGenerator TF+Keras), 100 Epochs  |
| rparedes  | [model3.h5](https://www.dropbox.com/s/xr83ppor975dl5a/model3.h5) |98.83% | 88.54%  | **87.52%** | details [here](https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/issues/14)   |

# Pretrained Models

First pretrained CoVid-19 models --> https://github.com/lindawangg/COVID-Net#pretrained-models

|Type|Pneumonia Sensitivity|Model|
|---|---|---|
|   |   |   |


**Proposal of an agreement about datasets and evaluation metrics**

 To adequately compare the results reported by the different experiments, we find necessary:

1) to use the same dataset partitions (training, evaluation, and test) and identical classification tasks
2) to report the results using the same performance metrics


PROPOSAL FOR DATASETS
---------------------

**Background**

The balanced-one-partition dataset (https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/tree/master/padchest-covid/balanced-one-partition) has been proposed as a starting point, where training, validation and test sets are well defined.

After the application of a number of data preparation and quality assessment algorithms, the following issues were detected:

(1) 2499 rows in the 'neumo-dataset.tsv' file were duplicated.
(2) 229 images were duplicated with different file names.
(3) A number of rotated images were detected.
(4) A number of blurry, completely black or completely white images were detected.

**Proposal**

Instead of "neumo_dataset.tsv", we propose that "pneumo_dataset_ITI_rev.tsv" , where the following actions were taken to deal with the aforementioned issues:

(1) The 2499 duplicated rows from the "neumo-dataset.tsv" have been deleted.
(2, 4) A new column called "Valid" has been added. The valid entries have a "1" in this column while invalid entries have a "0". One of the images that were identical, under different names, has been taken as their representative and has a "1" in this column, while the rest have a "0". Those images that were detected as entirely black or white, or too blurry have been also marked with a "0" in this column. Besides, a new column named "Repeat" has been added. The "Repeat" column has "-1" if there is no other identical image in the set, and else an integer >0 that is shared by those images that are identical. Finally, the new column "Observations" holds textual information with the reasons for the non-validity of the image.
(3) A new column called "Rotation_needed" contains the rotation angle in degrees needed to have the image in upright position.

We propose to use from now as the dataset for the experiments the images indexed in the rows of "pneumo_dataset_ITI_rev.tsv" file with a "1" in the "Valid" column after a rotation of the degrees specified in the "Rotation_needed" column.

Additionally, for convenience, the meaning of the columns of the dataset has been summarized in the file "dataset_columns.pdf".


PROPOSAL FOR EVALUATION METRICS
----------------------

**Background**

- According to the results reported in [1], the diagnostic agreement between radiologists in the assessment of the presence/absence of pneumonia on chest X-ray images is relatively weak. In that study, four practicing academic radiologists annotated a test set and the F1-score of the agreement of each individual radiologist against other 4 labels (the ones reported by the remaining 3 radiologists plus one more reported by a CNN) were computed. The results show a radiologist average of F1 = 0.387 ([0.330, 0.442] 95% CI). That value can be used as a baseline to interpret the results.

- The objective of this project should be to implement a system that relieves the radiologists under the pressure of a pandemic from reviewing as many images as possible, incurring in as few false negatives as possible, while providing extra help in detecting cases.

**Proposal**

- To report results for binary classifications: C-N, C-I, and C-NI according to the labels in column "group" of the dataset (assuming that the final task will be training a binary classifier C-Covid19)
- Not to use the classifier accuracy as evaluation metric, as it does not reflect well the performance target of the final task.
- To report the area under the ROC curve (AUC) and the F1 metric as general and consolidated measures for evaluating binary classifiers in the field.
- To report and take as the preferred reference value the ratio of images that could be filtered, considered negative to save human effort, at a maximum of 5% of False Negative Rate FNR=FN/(TP+FN) in the test set, since that could be a reasonable operating point of the system in practice (assuming that the test set is representative of a final real world scenario).


[1] P. Rajpurkar et al. CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning.  arXiv: Computer Vision and Pattern Recognition. 2017
