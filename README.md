# MapperDroid
MapperDroid : Verifying App Capabilities from Description to Permissions and API Calls

Abstract: 
Android Applications (Apps) are usually accompanied by a text description and a permissions manifest which are expected to describe the app behaviour. However, an app may request or use more permissions than what has been described. Therefore, the permissions declared in the application manifest alone can not be interpreted as the ground truth. Recent literature reported that malicious apps under-report  permissions. Such a scenario is a security and privacy risk. In this work, to discover such instances, we establish a correspondence from the application description to the permissions manifest leading to the Android API calls of the app. After experimentation on more than 25,000 random apps from Google Play Store over 19 different Android permissions, we show that a vast majority of apps understate at least one permission. This phenomenon raises data privacy and security concerns due to over-privileged application binaries. The correspondence is of significance because each additional permission corresponds to one or more sensitive or protected API calls made by the app which is not explicitly known to the user. We created a data set for our work which contains app metadata from where different permission sets are obtained. Our approach to detect under-reporting of permissions is scalable with respect to the number of apps. 

Note: The work has been submitted to Journal of Future Generation Computer Systems (December 2020). 

The complete data set will be available soon in near future. You should read the [README](https://github.com/rks101/MapperDroid/blob/master/data/README_data.txt) first. 
