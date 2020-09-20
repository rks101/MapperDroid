# MapperDroid
MapperDroid : Reconciling App Capabilities from Description to Permissions and API Calls

Abstract: 
Android Applications (Apps) are usually accompanied by a text description and a permissions manifest that are expected to describe the app behaviour. However, an app may request or use more permissions than what is described by the developer. Therefore, the permissions declared in the application manifest alone can not be interpreted as the ground truth for required permissions. Recent literature reported that malicious apps under-report permissions. In this work, to discover such instances, we establish a correspondence from the application description to the permissions manifest to the Android API calls of the app. After experimentation on more than 25,000 random apps from Google Play Store over 19 different Android permissions, we show that a vast majority of apps understate at least one permission. This phenomenon raises data privacy and security concerns due to over-privileged application binaries. The correspondence is of significance because each additional permission corresponds to one or more sensitive or protected API calls made by the app and not explicitly stated to the user. We use state-of-the-art AXPLORER mappings available between API calls and permissions for app analysis. We created a data set for our investigative work that contains app metadata from which different permission sets are obtained. Our approach to detect under-reporting of permissions is scalable with respect to the number of apps under study. 

Note: The work has been submitted to Journal of Future Generation Computer Systems (September 2020). 

The complete data set will be available soon in near future. 
