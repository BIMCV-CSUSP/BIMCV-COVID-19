<div class="clearfix" style="padding: 0px; padding-left: 100px; display: flex; flex-wrap: nowrap; justify-content: space-evenly; align-items:center">
<a href="http://bimcv.cipf.es/"><img src="https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/Images/logoinst.png?raw=true"</a><a href="http://ceib.san.gva.es"></a></div>

# [New BIMCV-COVID-19 1st + 2nd iteration](http://bimcv.cipf.es/bimcv-projects/bimcv-covid19)

# BIMCV COVID19 iterations 1 + 2 Dataset is ready

Thank you for your Interest in the BIMCV-COVID19 iterations Dataset.

Please read distribution rights at [LICENSE.md](https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/BIMCV-COVID19%2B/LICENSE.md).

## Description

BIMCV-COVID19+ dataset is a large dataset with chest X-ray images CXR (CR, DX) and computed tomography (CT) imaging of COVID-19 patients along with their radiographic findings, pathologies, polymerase chain reaction (PCR), immunoglobulin G (IgG) and immunoglobulin M (IgM) diagnostic antibody tests and radiographic reports from Medical Imaging Databank in Valencian Region Medical Image Bank (BIMCV). The findings are mapped onto standard Unified Medical Language System (UMLS) terminology and they cover a wide spectrum of thoracic entities, contrasting with the much more reduced number of entities annotated in previous datasets. Images are stored in high resolution and entities are localized with anatomical labels in a Medical Imaging Data Structure \([MIDS](https://bimcv.cipf.es/bimcv-projects/mids/)\) format. In addition, 10 images were annotated by a team of expert radiologists to include semantic segmentation of radiographic findings. Moreover, extensive information is provided, including the patient’s demographic information, type of projection and acquisition parameters for the imaging study, among others. This first iteration of the database includes 1380 CX, 885 DX and 163 CT studies.

## Data Sources

This directory contains an anonymized dataset of torax Rx from COVID19 patients, prepared by the same authors as [PADCHEST dataset](http://bimcv.cipf.es/bimcv-projects/padchest) and described in the following preprint [arXiv:2006.01174](https://arxiv.org/abs/2006.01174).

* The dataset is spread over the 81 different tgz archives. For each one of the archives there is a corresponding `*.tar-tvf.txt` file with the list of files inside the archive.

* There are also three additional archives corresponding to: the metadata and several scripts \([covid19_posi_subjects.tar.gz](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=covid19_posi_subjects.tar.gz)\); the one corresponding to the header description of the datasets \([covid19_posi_head.tar.gz](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=covid19_posi_head.tar.gz)\); and another one to the sessions \([covid19_posi_sessions_tsv.tar.gz](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=covid19_posi_sessions_tsv.tar.gz)\). Additionally, you can find more details about the metadata at <https://bimcv.cipf.es/bimcv-projects/bimcv-covid19/#1590859488150-148be708-c3f3> and <https://github.com/BIMCV-CSUSP/BIMCV-COVID-19>

* Files [sha1sums.txt](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=sha1sums.txt) and [sha1sums-b.txt](https://b2drop.bsc.es/index.php/s/BIMCV-COVID19-cIter_1_2/download?path=%2F&files=sha1sums-b.txt) have the SHA1 sums of all the archives and metadata in this dataset, as well as `*.tar-tvf.txt` and `LICENSE.md` files.

* NOTICE (20th October 2020): Due to the high demand of these datasets, it is recommended downloading the data through WebCAV protocol (please, see more details in each dataset webpage).


[BIMCV-COVID19+ 1st+2nd iteration](https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/tree/master/BIMCV-COVID19%2B)

[The Padchest-pneumonia dataset, here](https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/tree/master/padchest-covid#data-sources-bimcv-padchest)

## [FYI, the content on BIMCV COVID-19 github space is subject to daily updates.](https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/tree/master/padchest-covid) Note: please do not claim diagnostic performance of a model without a clinical study! This is not a kaggle competition dataset.

Following common strategies and initiatives emerged from the scientific community at international level, a series of actions are being carried out within the Valencia Region Image Bank (BIMCV) that combines data from the [PadChest dataset](http://bimcv.cipf.es/bimcv-projects/padchest) with future datasets based on COVID-19 pathology to provide the open scientific community with data of clinical-scientific value that helps early detection of COVID-19.

The team that is working on this project is made up of: FISABIO, Miguel Hernandez University, University of Alicante and staff from Hospital San Juan de Alicante with the colabortion of MedBravo, GE and CIPF.

Our thanks to multiple teams that are providing relevant information and help to improve procedures. Among them we can highlight the PRHLT, ITI, IFIC-CSIC, HGV, BSC, Transbionet network and BioinformaticsAnd_AI.

Medical Imaging Example of COVID-19 Rx from [medRxiv preprint doi](https://doi.org/10.1101/2020.02.14.20023028)
![ChestRX-COVID](https://github.com/BIMCV-CSUSP/BIMCV-COVID-19/blob/master/Images/deepChest-covid.png)

## Goal
Collect and publish chest X-ray images, coming from hospitals affiliated to the BIMCV, to which data that allows their identification will be erased for the purpose of training Deep Learning (DL) models. Such training is meant to obtain an early detection of infection and pneumonia by Covid from a simple chest X-ray. 
In order to achieve this, these images will be structured into subgroups of images coming from the PadChest dataset with differential diagnosis related to COVID-19’s radiological semiology, allowing to develop the first models based on Artificial Intelligence to better predict and understand the infection. 
## Immediate actions to do
Our investigation group “Unidad Mixta de Imagen Biomédica FISABIO-CIPF” is working towards launching these models using the FISABIO’s BIMCV (Openmind) platform that is shared with the computational resources from CIPF. It is a series of shared computational resources to face these challenges through the TransBioNet net.
While waiting for official authorization for an extraction of a new COVID-19’s X-ray data set from the competent authorities, the next tasks/actions are being carried out, using PadChest images as basis:

* Reorganization of PadChest data set related to COVID-19’s pathology course. 
* Extraction or data organization into subgroups coming from PadChest (known in AI as Data Curation) starting with pneumonia, infiltrated and controls. 
* Effective and well-adjusted partitioning (see figure 1).
* Preprocessing. Basically, the images are gonna be stored both in cluster and Kaggle and distributed into three groups: training or (Tr) 60%, validation or (Val) 20% and test or (Te) 20%. 

Various models will be trained and the ones which obtain better accuracy will be available as open source code in order to when the new BIMCV-COVID-19 data set is acquired, enable Transfer-Learning in new computational models.
