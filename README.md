
![alt text](https://media.istockphoto.com/photos/farm-silo-during-fall-with-background-colors-picture-id1169284385?k=20&m=1169284385&s=612x612&w=0&h=ozA-U4GG_GfuGqBDmF8CnmAP5MWwqUDK0tneE_BLi74= "Picture of a WI Farm")

__Analyzing The Impact of U.S.-China Trade Wars on Wisconsin Agricultural Exports__
=====
## __Background__
On July 6th, 2018 the U.S.-China trade wars were initiated when the United States imposed a 25% tariff on $34billion worth of Chinese imports.[^1] China responded by also imposing a 25% tariff on $34billion worth of U.S. imports. Trade tension continued to escalate and hit a peak at the end of 2019 with the United States having imposed tariffs on more than $360 billion worth of Chinese goods and China having imposed duties worth $110 billion on US products.[^2] Many of China’s retaliatory tariffs were targeted at U.S. agricultural products.

Wisconsin has a strong agricultural industry and ranks 13th among U.S. states in food, forestry, and agricultural exports.[^3] In general, the state relies heavily on exports as a source of economic development and was the 19th largest state exporter of goods in 2018.[^4] In 2018 good exports accounts for 6.7% of Wisconsin GDP and employment data estimates that in 2016 111,000 were supported by good Wisconsin good exports. [^5] However, Wisconsin trade has relied heavily on Canada, Mexico, and China, its largest markets. [^6]

## __Objectives__
This project seeks to examine how the U.S-China trade wars impacted Wisconsin agricultural exports. Specifically, it will outline an impact visualization on key Wisconsin agricultural commodities including milk, whey, ginseng, corn, soybean flour/meal, and soybeans.

## __Input Data__
All data came from the U.S. Census Bureau’s USA Trade® Online. Specifics about how this data was collected will be discussed below.

## __Data Handeling and Processing__
This project used Python 3.9 for data handling and visualization. It uses 4 main scripts:

1. _collect.py:_ This script is used to pull export data from the U.S. Census Bureau’s USA Trade® Online. It uses the Census API to retrieve export commodities by Harmonized System (HS) code and then stores the commodity data in CSV files. Although this project examines several commodities, exporting data into a CSV file allows the functions defined in this script to be useful for anyone seeking to retrieve general export data from USA Trade® Online. It is important to note that when doing API calls to USA Trade® Online, there are different endpoints for different variables. This project used two different endpoints to get export commodities’ values and quantities by HS code. The International Trade Data API User Guide can be found here for more details about their API system.

2. _join.py:_ The join script joins together CSV files by product or family of products. In this way, all quantity and value information for a 6-digit HS commodity is stored in one CSV file.

3. _sort.py:_ The sort.py script takes the joined CSV files from join.py and organizes them into DataFrames by sorting, dropping unnecessary columns, and renaming columns. For some commodities, there are multiple quantity values that need to be aggregated to match the value variable. This script sums quantities together so that the quantity value matches the value variable. Due to some quantities being in different units, this script also handles unit conversion so that the quantity values can be summed together. After the cleaning process is complete, the DataFrames are written into CSV files by commodity.

4. _figure.py:_   The figure.py starts by backing out quantity values for Wisconsin exports. Given that USA Trade® Online does not provide export quantity values by state, this script takes national export values and divides them by national export quantities to find national pricing levels for a given commodity. Assuming that national pricing is similar to Wisconsin pricing, the script then finds quantity values for Wisconsin exports by dividing Wisconsin export values by national pricing. The rest of the script creates figures to outline export quantities for a given commodity at both the national and state level.

## __Results__
Overall, the results demonstrate an association between the U.S.-China trade war and a decline in Wisconsin agricultural exports. 

### __Milk__: 
This figure demonstrates the impact of the trade wars on milk exports with less than 1% fat content. Although missing data is problematic, the decrease in milk exports at the height of the trade wars is clearly seen.

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Milk.png?raw=true "Milk Exports")

### __Whey__
This figure demonstrates the impact of the trade wars on whey exports. Although there is a clear decrease in exports, the decline is not as drastic as other commodities. 

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Whey.png?raw=true "Whey Exports")

### __Ginseng__
While there is a decline in Wisconsin ginseng exports, the results are not as clear as other commodities. Although the U.S.-China trade wars played a role in decreasing ginseng exports, the pandemic also could have played a role in this decrease as many people give Ginseng a gift when they travel over the holidays. 

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Ginseng.png?raw=true "Ginseng Exports")

### __Corn__
Missing data is problematic when it comes to assessing the impact of the trade wars on Wisconsin corn exports. Although there was a decrease in national corn exports from 2018-2019. This also could have been part of a larger trend that seemed to have started in 2017. Further analysis is needed to fully understand the impact of the trade wars on corn exports. 

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/Corn.png?raw=true "Corn Exports")

### __Soybean Flour__
This figure demonstrates the impact of the trade wars on soybean flour exports. Compared with other assessed commodities, the impact of the trade wars on Wisconsin soybean flour seems to have been most stark with no rebound. 

![alt text](https://github.com/4kaylaj/WI_Agricultural_Exports/blob/main/SoybeanFM.png?raw=true "Soybean Flour Exports")

## __Footnotes__

[^1]: “What Is the US-China Trade War?,” South China Morning Post, May 28, 2021, https://www.scmp.com/economy/china-economy/article/3078745/what-us-china-trade-war-how-it-started-and-what-inside-phase.

[^2]: Ibid.

[^3]: “Export Statistics,” DATCP Home Export Statistics, accessed May 3, 2022, https://datcp.wi.gov/Pages/AgDevelopment/ExportStatistics.aspx.

[^4]: “State Benefits of Trade: Wisconsin.” United States Trade Representative. Accessed May 3, 2022. https://ustr.gov/map/state-benefits/wi. 

[^5]: Ibid.

[^6]: Ibid.