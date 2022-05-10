# MapperDroid
Data set repository for MapperDroid : Reconciling Android Application (App) Capabilities from Description to Permissions and API Calls. 

The complete data set will be available soon in near future. To report any issue, or to collaborate further on this work, please contact the repo owner. 

You should read the [README](https://github.com/rks101/MapperDroid/blob/master/data/README_data.txt) first before getting started with the data set. 

<!--
Please cite our [paper](https://doi.org/10.1016/j.cose.2021.102493) published in Computers and Security if you find this work useful or if you are using the data set. 
-->

## How to cite the paper?  

Please, use the follwoing BibTeX entry:   

```
@article{SOLANKI2021102493,
title = {MapperDroid: Verifying app capabilities from description to permissions and API calls},
journal = {Computers & Security},
volume = {111},
pages = {102493},
year = {2021},
issn = {0167-4048},
doi = {https://doi.org/10.1016/j.cose.2021.102493},
url = {https://www.sciencedirect.com/science/article/pii/S0167404821003175},
author = {Rajendra Kumar Solanki and Vijay Laxmi and Bruhadeshwar Bezawada and Manoj Singh Gaur},
keywords = {Android applications, Permissions, API calls, Privacy, Over-privilege, Risk assessment, Deceptive apps},
abstract = {Android Applications (Apps) are usually accompanied by a text description and a permissions manifest which are expected to describe the app behaviour. However, an app may request or use more permissions than what has been described. Therefore, the permissions declared in the application manifest alone can not be interpreted as the ground truth. Recent literature reported that malicious apps under-report permissions. Such a scenario is a security and privacy risk. In this work, to discover such instances, we establish a correspondence from the application description to the permissions manifest leading to the Android API calls of the app. After experimentation on more than 25,000 random apps from Google Play Store over 19 different Android permissions, we show that a vast majority of apps understate at least one permission. This phenomenon raises data privacy and security concerns due to over-privileged application binaries. The correspondence is of significance because each additional permission corresponds to one or more sensitive or protected API calls made by the app which is not explicitly known to the user. We created a data set for our work which contains app metadata from where different permission sets are obtained. Our approach to detect under-reporting of permissions is scalable with respect to the number of apps.}
}
```
