
![alt text](https://media.istockphoto.com/photos/farm-silo-during-fall-with-background-colors-picture-id1169284385?k=20&m=1169284385&s=612x612&w=0&h=ozA-U4GG_GfuGqBDmF8CnmAP5MWwqUDK0tneE_BLi74= "Picture of a WI Farm")

__Analyzing The Impact of U.S.-China Trade Wars on Wisconsin Agricultural Exports__
=====
## __Background__
On July 6th, 2018 the U.S.-China trade wars were initiated when the United States imposed a 25% tariff on $34billion worth of Chinese imports.[^1] China responded by also imposing a 25% tariff on $34billion worth of U.S. imports. Trade tension continued to escalate and hit a peak at the end of 2019 with the United States having imposed tariffs on more than $360 billion worth of Chinese goods and China having imposed duties worth $110 billion on US products.[^2] Many of China’s retaliatory tariffs were targeted at U.S. agricultural products.

Wisconsin has a strong agricultural industry and ranks 13th among U.S. states in food, forestry, and agricultural exports.[^3] In general, the state relies heavily on exports as a source of economic development and was the 19th largest state exporter of goods in 2018.[^4] In 2018 good exports accounts for 6.7% of Wisconsin GDP and employment data estimates that in 2016 111,000 were supported by good Wisconsin good exports. [^5] However, Wisconsin trade has relied heavily on Canada, Mexico, and China, its largest markets. [^6]

## __Objectives__
This project seeks to examine how the U.S-China trade wars impacted Wisconsin agricultural exports. Specifically, it will outline an impact visualization on key Wisconsin agricultural commodities including milk, whey, ginseng, corn, soybean flour/meal, and soybeans.

## __Input Files__
All data came from the U.S. Census Bureau’s USA Trade® Online. Specifics about how this data was collected will be discussed below.

## __Output Files__
This project produces two types of deliverables: CSV files and figures. 

_CSV Files:_ Outline key variables needed to assess the impact of the trade wars for a given commodity. Varialbes include: National Quantity, Quantity Unit of Measurement, National Value, Wisconsin Quantity, Wisconsin Value, National Annual Quantity Average,Wisconsin Annual Quantity Average. 
1. Master_SoybeanFM.csv
2. Master_Soybean.csv
3. Master_Whey.csv
4. Master_Gin.csv
5. Master_Corn.csv
6. Master_Milk.csv

_Figures:_ visualize key statistics captured in the CSV files.
1. SoybeanFM.png
2. Soybean.png
3. Whey.png
4. Ginseng.png
5. Corn.png
6. Milk.png

## __Data Handeling and Processing__
This project used Python 3.9 for data handling and visualization. It uses 4 main scripts:

1. _collect.py:_ This script is used to pull export data from the U.S. Census Bureau’s USA Trade® Online. It uses the Census API to retrieve export commodities by Harmonized System (HS) code and then stores the commodity data in CSV files. Although this project examines several commodities, exporting data into a CSV file allows the functions defined in this script to be useful for anyone seeking to retrieve general export data from USA Trade® Online. It is important to note that when doing API calls to USA Trade® Online, there are different endpoints for different variables. This project used two different endpoints to get export commodities’ values and quantities by HS code. The International Trade Data API User Guide can be found [here](https://www.census.gov/foreign-trade/reference/guides/Guide%20to%20International%20Trade%20Datasets.pdf) for more details about their API system.

2. _join.py:_ The join script joins together CSV files by product or family of products. In this way, all quantity and value information for a 6-digit HS commodity is stored in one CSV file.

3. _sort.py:_ The sort.py script takes the joined CSV files from join.py and organizes them into DataFrames by sorting, dropping unnecessary columns, and renaming columns. For some commodities, there are multiple quantity values that need to be aggregated to match the value variable. This script sums quantities together so that the quantity value matches the value variable. Due to some quantities being in different units, this script also handles unit conversion so that the quantity values can be summed together. After the cleaning process is complete, the DataFrames are written into CSV files by commodity.

4. _figure.py:_   The figure.py starts by backing out quantity values for Wisconsin exports. Given that USA Trade® Online does not provide export quantity values by state, this script takes national export values and divides them by national export quantities to find national pricing levels for a given commodity. Assuming that national pricing is similar to Wisconsin pricing, the script then finds quantity values for Wisconsin exports by dividing Wisconsin export values by national pricing. Next, this script also calculates annual averages so it is easier to visualize quantity change. The rest of the script creates figures to outline export quantities for a given commodity at both the national and state level. The blue line is plotted monthly exports and the orange line is the plotted annual export averages. There is also a red reference line that marks the start of the U.S.-China trade wars.

## __Results__
Overall, the results do not clearly demonstrate an association between the U.S.-China trade war and a decline in Wisconsin agricultural exports. However, certain commodities do see a decrease in exports at the time of the trade wars, which would seem indicative of the negative impact. Further analysis, such as analyzing China-bound export trends and/or evaluating the effect on commodity valuation, is needed to better understand the impact of the trade wars of Wisconsin agricultural commodities. 

### __1% Milk__: 
This figure plots monthly 1% milk exports (in blue) and annual export averages (in orange). Although the Wisconsin annual average does not change at the start of the trade war, there is a visable drop in 2019. This decrease could be attributed to the escalation of the trade wars in 2019. The 2019 drop is also visable at the national level, which could demonstrate that the decrease in annual average exports at the state level is part of a larger trend. However, variation does seem to be normal for this commodity so further analysis is needed to assess the impact of the trade wars on 1% milk.

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Milk.png?raw=true "Milk Exports")

### __Whey__
This figure plots monthly whey exports (in blue) and annual export averages (in orange). At the start of the trade wars, there is a clear decrease in exports. This decline continues through the peak of the trade wars in 2019. Thus, whey seems to be one of the Wisconsin agiricultural commodities negatively impacted by the U.S.-China trade wars.

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Whey.png?raw=true "Whey Exports")

### __Ginseng__
This figure plots monthly ginseng exports (in blue) and annual export averages (in orange). Looking only at quantity exported, the U.S.-China trade wars do not seem to have impacted ginseng at the national or state level. 

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Ginseng.png?raw=true "Ginseng Exports")

### __Corn__
This figure plots monthly corn exports (in blue) and annual export averages (in orange). Missing data is problematic when it comes to assessing the impact of the trade wars on Wisconsin corn exports. Although there was a decrease in national corn exports from 2018-2019, this decrease does not seem differnt from yearly variation. Thus,further analysis and data is needed to fully understand the impact of the trade wars on corn exports. 

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Corn.png?raw=true "Corn Exports")

### __Soybeans__ 
This figure plots monthly soybean exports (in blue) and annual export averages (in orgnage). Again missing, data is problamatic for assessing the impact of the trade wars at the state level. However at the start of the trade wars there does seem to be an increase in soybean exports at the national level. Nonetheless, at the height of the trade wars in 2019, there is an annaula average decrease in soybean exports. This decrease could be attributed to an increase in retalitory actions taken by China. Further analysis and data is needed to fully understand the impact of the trade wars on soybean exports.  

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Soybean.png?raw=true=true "Soybean Exports")


### __Soybean Flour__
This figure plots monthly soybean flour exports (in blue) and annual export averages (in orange). At the height of the trade wars in 2019, Wisconsin soybean flour exports plummet. Compared with other assessed commodities, the impact of the trade wars on Wisconsin soybean flour seems to have been most stark with no rebound. 

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/SoybeanFM.png?raw=true "Soybean Flour Exports")

## __Footnotes__

[^1]: “What Is the US-China Trade War?,” South China Morning Post, May 28, 2021, https://www.scmp.com/economy/china-economy/article/3078745/what-us-china-trade-war-how-it-started-and-what-inside-phase.

[^2]: Ibid.

[^3]: “Export Statistics,” DATCP Home Export Statistics, accessed May 3, 2022, https://datcp.wi.gov/Pages/AgDevelopment/ExportStatistics.aspx.

[^4]: “State Benefits of Trade: Wisconsin.” United States Trade Representative. Accessed May 3, 2022. https://ustr.gov/map/state-benefits/wi. 

[^5]: Ibid.

[^6]: Ibid.