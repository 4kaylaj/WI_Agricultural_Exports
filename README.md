
![alt text](https://media.istockphoto.com/photos/farm-silo-during-fall-with-background-colors-picture-id1169284385?k=20&m=1169284385&s=612x612&w=0&h=ozA-U4GG_GfuGqBDmF8CnmAP5MWwqUDK0tneE_BLi74= "Picture of a WI Farm")

__Analyzing The Impact of U.S.-China Trade Wars on Wisconsin Agricultural Exports__
=====
## __Background__
On July 6th, 2018 the U.S.-China trade wars were initiated when the United States imposed a 25% tariff on $34billion worth of Chinese imports. China responded by also imposing a 25% tariff on $34billion worth of U.S. imports. Trade tension continued to escalate and hit a peak at the end of 2019 with the United States having imposed tariffs on more than $360 billion worth of Chinese goods and China having imposed duties worth $110 billion on US products. Many of China’s retaliatory tariffs were targeted at U.S. agricultural products.

Wisconsin has a strong agricultural industry and ranks 13th among U.S. states in food, forestry, and agricultural exports.  In general, the state relies heavily on exports as a source of economic development and was the 19th largest state exporter of goods in 2018. In 2018 good exports accounts for 6.7% of Wisconsin GDP and employment data estimates that in 2016 111,000 were supported by good Wisconsin good exports. However, Wisconsin trade has relied heavily on Canada, Mexico, and China, its largest markets.  

## __Objectives__
This project seeks to examine how the U.S-China trade wars impacted Wisconsin agricultural exports. Specifically, it will outline an impact visualization on key Wisconsin agricultural commodities including milk, whey, ginseng, corn, soybean flour/meal, and soybeans.

## __Input Data__
All data came from the U.S. Census Bureau’s USA Trade® Online. Specifics about how this data was collected will be discussed below.

## __Data Handeling and Processing__
This project used Python 3.9 for data handling and visualization. It uses 4 main scripts:

1. _collect.py:_ This script is used to pull export data from the U.S. Census Bureau’s USA Trade® Online.  It uses the Census API to retrieve export commodities by Harmonized System (HS) code and then stores the commodity data in CSV files. Although this project examines several commodities, exporting data into a CSV file allows the functions defined in this script to be useful for anyone seeking to retrieve general export data from USA Trade® Online. It is important to note that when doing API calls to USA Trade® Online, there are different endpoints for different variables. This project used two different endpoints to get export commodities’ values and quantities by HS code. The International Trade Data API User Guide can be found here for more details about their API system.

2. _join.py:_ The join script joins together CSV files by product or family of products. In this way, all quantity and value information for a 6-digit HS commodity is stored in one CSV file.

3. _sort.py:_ The sort.py script takes the joined CSV files from join.py and organizes them into DataFrames by sorting, dropping unnecessary columns, and renaming columns. For some commodities, there are multiple quantity values that need to be aggregated to match the value variable. This script sums quantities together so that the quantity value matches the value variable. Due to some quantities being in different units, this script also handles unit conversion so that the quantity values can be summed together. After the cleaning process is complete, the DataFrames are written into CSV files by commodity.

4. _figure.py:_   The figure.py starts by backing out quantity values for Wisconsin exports. Given that USA Trade® Online does not provide export quantity values by state, this script takes national export values and divides them by national export quantities to find national pricing levels for a given commodity. Assuming that national pricing is similar to Wisconsin pricing, the script then finds quantity values for Wisconsin exports by dividing Wisconsin export values by national pricing. The rest of the script creates figures to outline export quantities for a given commodity at both the national and state level.

## __Results__
Overall, the results demonstrate an association between the U.S.-China trade war and a decline in Wisconsin agricultural exports. 

### __Milk__
![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Milk.png?raw=true "Milk Exports")

### __Whey__
![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Whey.png?raw=true "Whey Exports")

### __Ginseng__
![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Ginseng.png?raw=true "Ginseng Exports")

### __Ginseng__
![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Ginseng.png?raw=true "Ginseng Exports")

### __Corn__
![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Corn.png?raw=true "Corn Exports")

### __Soybean Flour__
![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/SoybeanFM.png?raw=true "Soybean Flour Exports")

## __References__

