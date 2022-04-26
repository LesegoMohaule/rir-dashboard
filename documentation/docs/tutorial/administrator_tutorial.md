# Administrator Tutorial

## Introduction

🧑‍🏫 The RIR (Risk Informed Response) platform is a situational awareness platform to monitor health, child protection, nutrition, wash, and education in a geographic region. This tutorial shows you how to manage the platform as an administrator.


### Working with this documentation

Whenever you see a phrase in **bold**, it refers to a link or button on the user interface that you can interact with.

### Important Links

* [RIR Platform](https://staging.rir.kartoza.com/ "RIR Platform")
* [RIR Full Documentation](https://kartoza.github.io/rir-dashboard/ "RIR Full Documentation")  
> 📒 **Note:** You can find all the **sample data** used in this tutorial here: [Data](../assets/tutorial_data/Training_Data.zip "Data")

## Session Outline

This session is divided into two parts:

1. **Part 1:** General Platform Administration
   * User Management: Creating and editing user profiles.
   * Managing Instances: Creating new and editing preexisting instances.
   * Managing Context Layers: Using layers that you have uploaded to GeoNode or GeoServer to create a context layer in the platform.
   * Geography management: Adding geography levels to your instance.

![image](https://user-images.githubusercontent.com/77841514/163354387-91e9ca4a-503b-4b23-b970-39b18d97cf79.png)

2. **Part 2:** Indicator Administration
   * Indicator management: Adding indicators to the dashboard.
   * Forms: used to manually capture indicator data by filling in forms.
   * Ingestors: Used to manually import data by uploading.
   * Harvesters: Automatic agents that fetch data and add it to indicators on a regular basis.


![Ingestor Types](../assets/screenshots/ingestor-types.png)

 
## Session Tutorial

### **Signing In**

In the top right-hand corner of the screen is the **Sign In** button. Here, you will sign in using your admin username and password. This process is the same for a staff user and an admin user.  

![Signing in](../assets/screencasts/login.gif "Signing in")

### **Users and Permissions**

Next, we will look at how to manage users. Go to site administration by clicking **Admin -> Django Admin**. Click on **+Add** in the same row as ‘Users’. You can now create a profile for someone by adding a username and password. Once you have created the user profile, click **Save**.

![New User](../assets/screencasts/new-user.gif "New User")

Once you have created the user account, go back to Site Administration and select the **User** option. Select the user you created, and then you can edit their personal information as well as select or deselect their permission status. Remember to **Save** your changes.

![Permissions](../assets/screencasts/permissions.gif "Permissions")

> 📒 **Note**: If you want to make a user an admin user so that they can carry out the activities described in this tutorial, you should assign them to the **Staff** group, the **Super User** group and the **Active** box should be checked.

![Groups](../assets/screencasts/permissions.gif "Groups")

### **Creating an instance**

🧑‍🏫 Once you’ve signed in as an admin user, you will be redirected back to the home page which contains various instances. To create a new instance, select the dropdown menu next to your username and click on **Django Admin**. Once you’re on the Site Administration page, scroll down until you find **Instances**.

👨‍🏫 Click on the **+Add** button on the right-hand side of the Instances screen. Add the name of the new instance that you would like to create, a description, as well as the icon file. The icon file in most cases would be a flag of the country for the instance. Once you have added all information, click **Save**.

![Creating a New Instance](../assets/screencasts/new-instance.gif "Creating a New Instance")

 For this tutorial, we will create a demonstrator instance for South Africa:

 ![SA flag](../assets/tutorial_data/sa-flag.png)

 > **Note:** You can find all the **sample data** used in this tutorial (including this flag image) [here](../assets/tutorial_data/RIRTrainingData.zip).

Once your new instance is created, you will be able to open it from the instance chooser. It will appear very empty, like this:

 ![New Instance](../assets/screenshots/newinstance.png)

### **Adding a new Context layer**

🧑‍🏫 In this section we will explain how to create and manage context layers. What is a context layer? Context layers are shown on the map to provide a sense of the conditions in the region. They can cover any topic - for example, security, food security, infrastructure, etc. Context layers do not have indicator data attached, they are a visual aid in the dashboard map. Context layers are normally hosted on another server e.g. ArcGIS Online, GeoServer, and GeoNode all provide ways to publish context layers.

To add a context layer to the RIR instance, you will need a link to an online layer. For this exercise will be adding a context layer showing homelands:

![Home Lands Data](../assets/screenshots/homelands.png)

👨‍🏫 To find the link to an online layer so that you can copy it over and create your layer in the RIR Dashboard, Right-click on the browser page, click on inspect, and then select network. Hard refresh your screen and look through the URL links until you see the layer URL. 
This is the URL that you need to copy.

For our example, we will use the URL below. Please copy it:

![Home Lands Data](../assets/screenshots/homelandsurl.png)

```
https://staging.osgs.rir.kartoza.com/geoserver/ows?access_token=SWMqWx64T5dOsNwPD72o4uIbtZ7FIA&LAYERS=geonode%3Aformer_homelands_polygon&TRANSPARENT=TRUE&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&STYLES=&FORMAT=image%2Fpng&SRS=EPSG%3A900913&BBOX=2504688.5425,-3757032.81375,3757032.81375,-2504688.5425&WIDTH=256&HEIGHT=256
```

👨‍🏫 Now we can create the context layer in the RIR platform.
Click on your account menu in the top right corner of the RIR platform and open **Django Admin**. Click on **+Add** on the Context layers line. Select the instance you would like to add the context layer to.

![Context Layers](../assets/screenshots/addcontextlayer.png "Context Layers")

We will use the instance that we have just created, South Africa. Also, paste the URL that you copied before to URL input.

Enter the information in the form as shown in the images below and save the form once you are happy with it.

![Context Layers](../assets/screenshots/context-layer.png "Context Layers")

Click on **View Site** to see your new layer. You will be able to see your new layer in the **Layers** menu. There is also an option to add other parameters to this layer.

![Context Layers](../assets/screencasts/context-layer.gif "Context Layers")

### Geography Management

#### **Adding a Geography level**

🧑‍🏫 Geography levels express the hierarchy between administrative boundaries. For example in South Africa we have the national boundary subdivided into provinces, which are in turn subdivided into districts, then municipalities. RIR uses these geography levels to provide a sense of the conditions in the region.

👨‍🏫 Let’s start in  **Site Administration**. Scroll down to **Geometry Level Instances** and click **+Add**. Set the name and description to your instance. Go back to the main page of your instance. Below the **Program Interventions** panel are three icons; **Indicator Management**, **Geography Management**, and **Instance Management**.

Click on the **Geography Management** icon. You will be redirected to the geography view map page, and you will see that in the top right corner there is an **+uploader** button. Select this button and start filling in the form. The first thing you need to do is add the data for the geography level. Once the data is uploaded, you will be able to fill in the rest of the form.  



> 📒 **Note:** You can find all the sample data used in this tutorial here: [Data](../assets/tutorial_data/Training_Data.zip "Data")


For a province level, the code column is 'code', the name column is 'name', and the parent code column is 'pcode'. The country does not need a parent, but we need the code for a country level. In this case, the country is ZA (under 'adm0_pcode')


### **Adding a New Indicator**

🧑‍🏫 Indicators are special layers in RIR that are linked to the situation in the region. Indicators are used to show the situation in the region. For example, in South Africa, there are indicators for the number of people living in poverty, the number of people living in extreme poverty, the number of people living in extreme poverty, and the number of people living in extreme poverty and the number of people living in extreme poverty and the number of people living in extreme poverty.

👨‍🏫 To add an indicator, click on **Indicator Management** on the main platform page for the instance and go to **Create New**. Fill in the necessary information about the indicator you would like to create.

👨‍🏫 Once you have filled out the form, scroll down to **Scenario Rules** and add the parameters to match the indicator. you can also change the color for each rule by clicking on the color block. Click **Submit** once you are happy with the added information and scenario rules. If you add a dashboard link, you will see a black dot in the center of the circle that represents the scenario case on that indicator in the Program Interventions panel. By clicking on the black dot, you will be redirected to the dashboard link.
 
![New Indicator](../assets/screencasts/new-indicator.gif "New Indicator")

🧑‍🏫 Once we have created an indicator, we need to populate it with data. There are three ways to do this.

1. We can manually add the data using the value manager form or map.
2. We can use an ingestor to import data from a spreadsheet.
3. We can use a harvester to automatically fetch the data from an online resource.

### **Value Manager Form**

🧑‍🏫 The value manager form is a table with cells and rows, one row per administrative boundary, and one cell per indicator.

👨‍🏫 Let's look at how to use the Value Manager Form. To access this form, go to **Indicator Management** and scroll to the indicator that you would like to add data to. On the right-hand side of the indicator's name, there will be a small **Settings** symbol.
Click on **Settings** for the desired indicator and then click on **Value Manager Form**. You will be redirected to a form that gives you all the geographic locations within the instance and spaces to add values. 

👨‍🏫 You can also add a file to fill in the data by clicking **Use File to Refill Form**. To check how to do it, check section _Spreadsheet Uploader_.

![Value Manager Form](../assets/screencasts/value-manager-form.gif "Value Manager Form")

### **Value Manager Map**

🧑‍🏫 The value manager map allows you to add data by directly clicking on the region of the map that you would like to add data to.

👨‍🏫 The second way to add data to an indicator is through the Value Manager Map option. Go to **Indicator Management** and scroll to the indicator that you would like to add data to. On the right-hand side of the indicator's name, there will be a small Settings symbol. Click on **Settings** for the desired indicator and then "click" on **Value Manager Map**. This will take you back to the map canvas. Now you will be able to click on any geographic location within the instance and a popup window will appear which will allow you to fill in value data for that location.

![Value Manager Map](../assets/screencasts/value-manager-map.gif "Value Manager Map")

### **Ingestors**

🧑‍🏫 The function of an ingestor is to manually populate data for an ingestor. 

There are three modalities for ingestors:

1. Spreadsheet uploader (for single indicators)
2. Meta Ingestor (for populating multiple indicators)
3. Push API (advanced, allows you to create programmes that push their data to an indicator)

We describe the workflow for each of these ingestors below.

#### Spreadsheet Uploader

👨‍🏫 Spreadsheet uploader is used for upload data of an indicator using one file. It is using _Value Manager Form_ without input value one by one.
We are going to use TrainingData/IngestorData/sa-population.xls.

👨‍🏫 For this example, we are going to use **population** indicator.
Before starts, we need to create the indicator first. (Check _Adding a New Indicator_ section)

🧑‍🏫 Go to **Indicator Management** and scroll to the indicator that you would like to add data to. On the right-hand side of the indicator's name, there will be a small **Settings** symbol.
Click on **Settings** for the desired indicator and then click on **Value Manager Form**. 

👨‍🏫 Click _Use File to Refill Form_ and the popup will show. After that select other inputs. 
> 📒 **Note:** Always select administrative code to _Choose area code column._

🧑‍🏫 After everything selected, click _import_, and the form will be autofilled. 
> 📒 **Note:** If it is still empty, check the administrative code that you have on spreadsheet and the forms. 
> Always use administrative code on the speadsheet value. On the form, the code is in brackets.                        

![Spreadsheet Ingestor](../assets/screencasts/spreadsheet-ingestor.gif "Spreadsheet Ingestor")

#### Meta Ingestor Uploader

👨‍🏫 We are going to create a Meta Ingestor. The goal for this ingestor is for uploading data for multiple indicator for one file.
We are going to use TrainingData/IngestorData/sa-gdp_unemployment.xls.
In there, there are **gdp** and **unemployment** columns that we need to save the data for **gdp** and **unemployment** indicator. 
Before starts, we need to create those indicators first. (Check _Adding a New Indicator_ section)

🧑‍🏫 To start the meta ingestor, go to **Indicator Management** and in the top right-hand corner of the page, there will be a **Meta Ingestor** option that you will 
need to click. 

🧑‍🏫 Select the file in TrainingData/IngestorData/sa-gdp_unemployment.xls from the sample data and the other inputs will be activate.

🧑‍🏫 Select _Sheet name_ and _Row number: header_ (It is row 1).

🧑‍🏫 Select _Column name: administration code_, and select other _Column name_ inputs (The indicator name) with the header on the Excel that reflects the indicator data. 
Then **Submit** your work, and wait until it says done. 
![Meta Ingestor](../assets/screencasts/meta-ingestor.gif "Meta Ingestor")


#### API Ingestor

> Note: This is for advanced users only.

👨‍🏫 To start, click on **Create Harvester** as you will also do for the harvester options. Change the type of harvester to **Harvested using exposed API by external client**. Add necessary notes and submit.


You will now be presented with an 'API URL' and a 'Token' that has been received from an external source. You now need to "push" the data from outside to the RIR dashboard. "Open" the API platform that you use to build and use API's. We used Postman. "Copy" over the URL and token to push the data to the RIR dashboard.

![Ingestor](../assets/screencasts/ingestor.gif "Ingestor")

### **Harvesters**

🧑‍🏫 Harvesters are fully automated software routines that periodically fetch data from third party sources and populate indicators.

👨‍🏫 Go to **Indicator Management** and if you haven't already created the indicator you want to work with, start by doing that. Once the necessary indicator exists,click on the little **Settings** icon on the right-hand side of the indicator name. Select the **Create Harvester** option. Pick the type of harvester you would like to create from the drop-down Harvester (you will be presented with three options: 'API With Geography Using Today's Date'; 'API With Geography And Date'; and 'Harvested Using Exposed API By External Client'). The first two options are for the harvester and the third one is for the ingestor. For the 'API With Geography Using Today's Date' and 'API With Geography And Date' options,  fill in the Attributes portion of the form and then a popup window with a list of 
keys will appear; **drag** the green labels to their corresponding criteria. Select **Harvest Now**. You can scroll down to the log to see if your harvest is running in the background. Go to **Indicator Management** and click on the little settings icon that you just created a harvester for and select **Value Manager Map** to view your progress.
 
![Harvester](../assets/screencasts/harvester.gif "Harvester")
