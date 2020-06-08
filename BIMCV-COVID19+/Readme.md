# BIMCV COVID19 dataset

Thank you for your Interest in the BIMCV-COVID19 Dataset. You have been granted access to download it. We will keep you updated on new releases or improvements.

Please read distribution rights at [LICENSE.md](LICENSE.md).

MIRROR BSC (EUDAT): https://b2drop.bsc.es/index.php/s/BIMCV-COVID19

MIRROR OSF: https://osf.io/nh7g8/?view_only=7918f71e6e97440b865975884c948bc1


## Description

BIMCV-COVID19+ dataset is a large dataset with chest X-ray images CXR (CR, DX) and computed tomography (CT) imaging of COVID-19 patients along with their radiographic findings, pathologies, polymerase chain reaction (PCR), immunoglobulin G (IgG) and immunoglobulin M (IgM) diagnostic antibody tests and radiographic reports from Medical Imaging Databank in Valencian Region Medical Image Bank (BIMCV). The findings are mapped onto standard Unified Medical Language System (UMLS) terminology and they cover a wide spectrum of thoracic entities, contrasting with the much more reduced number of entities annotated in previous datasets. Images are stored in high resolution and entities are localized with anatomical labels in a Medical Imaging Data Structure (MIDS) format. In addition, 10 images were annotated by a team of expert radiologists to include semantic segmentation of radiographic findings. Moreover, extensive information is provided,including the patient’s demographic information, type of projection and acquisition parameters for the imaging study, among others. This first iteration of the database includes 1380 CX, 885 DX and 163 CT studies.

## Data Sources

This directory contains an anonymized dataset of torax Rx from COVID19 patients, prepared by the same authors as [PADCHEST dataset](http://bimcv.cipf.es/bimcv-projects/padchest) and described in the following preprint [arXiv:2006.01174](https://arxiv.org/abs/2006.01174).

* The dataset is spread over the 34 different tgz archives. For each one of the archives there is a corresponding `*.tar-tvf.txt` file with the list of files inside the archive.

* [bimcv_covid19_posi_head_iter1.tgz](bimcv_covid19_posi_head_iter1.tgz) is the tgz archive containing all the associated metadata related to the files comprising the dataset. It also includes some documentation. Additionally, you can find more details about the metadata at <http://bimcv.cipf.es/bimcv-projects/bimcv-covid19/> and <https://github.com/BIMCV-CSUSP/BIMCV-COVID-19>

* Files [sha1sums.txt](sha1sums.txt) and [sha1sums-b.txt](sha1sums-b.txt) have the SHA1 sums of all the archives and metadata in this dataset, as well as `*.tar-tvf.txt` and `LICENSE.md` files.

Please also see <https://github.com/BIMCV-CSUSP/BIMCV-COVID-19>
