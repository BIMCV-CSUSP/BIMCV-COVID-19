<div class="clearfix" style="padding: 0px; padding-left: 100px; display: flex; flex-wrap: nowrap; justify-content: space-evenly; align-items:center">
<a href="http://bimcv.cipf.es/"><img src="https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/chestRx/logoinst.png?raw=true"</a><a href="http://ceib.san.gva.es"></a></div>

# Data Sources. [BIMCV-PadChest](http://ceib.bioinfo.cipf.es/covid19/padchest_neumonia.zip)
You can download the Raw images from this link --> http://ceib.bioinfo.cipf.es/covid19/padchest_neumonia.zip

You can download the resize images from  --> http://ceib.bioinfo.cipf.es/covid19/resized_padchest_neumo.tar.gz

You can download other resize images --> http://ceib.bioinfo.cipf.es/covid19/resized_padchest_neumo_32.tar.gz
# UPDATES

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
|TeamBioinformaticsAndArtificialInteligence|VGG16|---| 62.76%|62.44%|Resize 524x524 -> 224x224 with Transfer Learning and without Data Augmentation (Train 81.44%), dataBase=Resize_padchest_neumo(2.81GB)|
|   |   |   |   |   |   |

### 2 classes C versus [I,NI,N]
|  Participant | Model name  | Dev Accuracy | Test Accuracy  | Comments  |
|---|---|---|---|---|
| jonandergomez  | model2 | 78.39%  | ----  |  512x512 images |
|TeamBioinformaticsAndArtificialInteligence| Model5-Alzaheimer2D |79.05%|78.21%| Resize 524x524 -> 224x224 without Transfer Learning and Data Augmentation (Train 81.74%), dataBase=Resize_padchest_neumo(2.81GB)  |
|TeamBioinformaticsAndArtificialInteligence| VGG16  |82.84%|82.46%|  Resize 524x524 -> 224x224 with Transfer Learning and Data Augmentation (Train 85.04%), dataBase=Resize_padchest_neumo(2.81GB), Data augmentation with ImageDataGenerator TF+Keras)  |

### 2 classes {C,N}
|  Participant | Model name  | Dev Accuracy | Test Accuracy  | Comments  |
|---|---|---|---|---|
| jonandergomez | model2 | 83.69% | 81.70% | 512x512 images, useless model because of overfitting, 98.89% of accuracy on training partition. Now trying to improve it. | 
| rparedes  | model2_rp | 84.06%  | ----  | 512x512 images, numpy |
| rparedes  | model3_rp* | 88.08%  | ----  | loss: 0.0499 - acc: 0.9824 - val_loss: 0.4749 - val_acc: 0.8808   |
|   |   |   |   |   |

model3_rp = 300 epochs preraining without DA + 300 epochs with DA. Learning Rate Annealing. Bottleneck Model (non-residual). Images 512x512 first conv 7x7 stride=2, rest convs 3x3. + BN + MaxPool, 32+64+128+256+256 + GlobalMaxPool
