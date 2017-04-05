Title: How to use EP postprocessing tool
Date: 2017-01-29 22:00
Category: EPpostprocessing
Tags: help
Slug: first-post
Author: obakatsu
Summary: This page is showing how to use EPpostprocessing

##Step1. Set idf file before running simulation
Once you set all the setting for energy simulation, set following setting to the idf file.   
	1. In Output:Table:SummaryReports chapter, set Report 1 Name to AllSummary   
	![images/instruction1.png]({filename}/images/instruction1.png){:width="400px"}   
	2. In OutputControl:Table:Style chapter, set Column Separator to CommaAndHTML and Unit Conversion to JtoKWH   
	![images/instruction2.png]({filename}/images/instruction2.png){:width="400px"}     

##Step2. Run the simulation 

##Step3. Upload the simulation result 
Once you finished the simulation, go to the upload page[link] and input all the information and upload html file from the simulation result.
![images/instruction3.png]({filename}/images/instruction3.png){:width="400px"}  

##Step4. Investigate visualized data
Once application finished to process the data, project list page will be shown. You can investigate the data reading through the [many kinds of visualized data]({filename}/17013010.md)

