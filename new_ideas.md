# Overview of possible research questions for different datasets
## LIDV_IDRI (Lung Cancer Imaging Dataset)
Link: https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI#f633413761b746ff9e49dd8f0d5b679d

**Possible research questions:**
* Which nodule characteristics (subtlety, internal structure, sphericity, ...) (as given by annotators) are predictive for the diagnosis of the patient and/or the malignancy of the tumor?
* Can we see a difference between the nodule characteristics of patients with a primary malignant lung tumor, and those with a cancer that has metastasized to the lungs?
* Does the number of nodules have an influence on the diagnosis of patients?
* How prevalent is inter-annotator disagreement on the characteristics? Is there a correlation with the malignancy or the diagnosis?

**Notes**
* These research questions can be done purely on the nodule characteristics present in the annotation files, and with the diagnosis information (although this is not needed for all questions, because diagnosis is not available for all patients if I understand correctly).
* Other research questions, like some included in our ML1 file, are heavily reliant on the images and/or annotation traces and analysis thereof and are therefore maybe not a good idea for this project.
* In general, I think we require quite a bit of domain knowledge to really understand what we're doing here, since it's all medical data, and no data which is more common-knowledge (like demographic data). This will maybe also make it more difficult to tell a story with this data that is well understood by the public.

## Cardiovascular diseases dataset
Link: https://www.kaggle.com/sulianova/cardiovascular-disease-dataset

**Possible research questions:**
* Is cardiovascular disease more prevalent in certain demographic groups? (age, gender, weight, ...).
* Which examination features (blood pressure, cholesterol, glucose) are most predictive for cardiovascular diseases?
* Are some of those features more important for certain demographic groups?
* Which behavioural features (smoking, alcohol, physicial activity) are predictive for cardiovascular diseases?
* Which combinations of behavioural features occur frequently, and do they reinforce each others link with cardiovascular diseases?
* Which (combinations of) behavioural features are more prevalent with certain demographics? Do they have differing effects on cardiovascular diseases for different demographics?

**Notes**
* This dataset contains information that can be interesting for us and for the public. We can ask quite a few research questions.
* I wonder whether we will really discover information here that is not already common knowledge. I can't really think of any more complicated or interesting research questions.
* It is rather limited in each of the feature categories (except for maybe demographics), as only three behavioural features are in the dataset for example, also no distinction is made between different cardiovascular diseases, and we don't have any information on mortality.

## Breast cancer datasets
Link: https://www.kaggle.com/yuqing01/breast-cancer and/or https://www.kaggle.com/hdza1991/breast-cancer-wisconsin-data-set

**Possible research questions:**
* Which characteristics are predictive for the diagnosis?
* Which charcterisics are correlated?

**Notes**
* This dataset is rather limited with regards to interesting labels and conclusions.
* It contains many features, but these again require extensive domain knowledge to draw interesting conclusions from them, and will probably not be very interesting to present to the public.

## Global Burden of Disease
Link: http://ghdx.healthdata.org/gbd-2017 (http://ghdx.healthdata.org/gbd-results-tool)

**Possible research questions:**
* In which countries are certain cancers/cardiovascular diseases/other diseases more prevalent? Why is this?
* Is the proportion of different cancers and cardiovascular diseases the same in every country or year, or does this differ? Why?
* Did this change over the years? (data from 1990 to 2017)
* Is there a link between higher prevalence of these diseases and certain risk factors? (e.g. diet, pollution, occupational hazards, ...)
* How many people are contracting cancer/a cardiovascular disease each year, how many are living with it in a controlled fashion, and how many are dying from it each year? Is there a difference in how long people live with cancer between countries? Has this changed over the years?

**Notes**
* This data set is extremely broad and contains very much information. I have restricted the research questions to cancer and cardiovascular diseases here, because I think we will have to restrict ourselves, but we can also change it to some other diseases or disabilities.
* See http://www.healthdata.org/sites/default/files/files/Data_viz/GBD_2017_Tools_Overview.pdf for more information about what is in this dataset.
* I think this information can be very interesting to present to the public. There are also many possibilities to expand our search, where the other datasets are (in my opinion) more limited.
* We can also try to link this information with other demographic information about countries (e.g. alcohol consumption, health budgets, ...), that is not necessarily included in this dataset.