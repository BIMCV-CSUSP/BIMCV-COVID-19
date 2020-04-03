<div class="clearfix" style="padding: 0px; padding-left: 100px; display: flex; flex-wrap: nowrap; justify-content: space-evenly; align-items:center">
<a href="http://bimcv.cipf.es/"><img src="https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/chestRx/logoinst.png?raw=true"</a><a href="http://ceib.san.gva.es"></a></div>

# Data Sources. [BIMCV-PadChest](http://ceib.bioinfo.cipf.es/covid19/padchest_neumonia.zip)

Mirrow from BSC-[TranBioNet](https://inb-elixir.es/transbionet) --> https://b2drop.bsc.es/index.php/s/BIMCV-PadChest

You can download the Raw images from this link --> http://ceib.bioinfo.cipf.es/covid19/padchest_neumonia.zip

You can download the resize images from  --> http://ceib.bioinfo.cipf.es/covid19/resized_padchest_neumo.tar.gz

You can download other resize images --> http://ceib.bioinfo.cipf.es/covid19/resized_padchest_neumo_32.tar.gz
# UPDATES

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
