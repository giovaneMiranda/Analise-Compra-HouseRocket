# House Rocket 
This repository contains analysis and data of a real estate company.
All information below is fiction. 

## House Rocket buy and sell analysis

![](giphy.gif)

# 1. Business Problem. 

House Rocket is a digital platform whose bunisses model is the purchase and sale of real estate using technology.
House Rocket's CEO would lice to maximize the company's revenue by finding good business opportunities. 

The maind strategy is to buy good houses in great locations at low prices and then resell them later at highter prices. The greater the difference between buying and selling, the greater the company's profit and therefore the greater its revenue. 

- Which houses should the CEO of House Rocket buy and what purchase price?
- Once the house is owned by the company, what is the best time to sell them and what would be the sale price?

# 2. Business Assumptions.
The assumptions about the business problem is as follows:
- Seasonality impact real state demand. 
- Seasons: 
  - Winter starts on December
  - Spring starts on March
  - Summer starts on June
  - Fall starts on September

- Houses near lakes areas have higher prices.
- Criteria to determine wether a property is suitable for purchase. 
  - The proprerty must have condition greater or iqual than 3. 
  - The property price must be smaller than the median price on the region. 
- Criteria to determine a property sale. 
  - Property price greater than median region price per season, selling price is added in 30%
  - Property price less than median region price per season, selling price is added in 10%
  - Porperty will be sold in season with the highest profit. 
- Bathrooms will not be distinguished by their contents.
- Dataset variables:

Variable     | Definition
------------ | -------------
|id          | Unique ID for each property available|
|date        | Date that the property was available|
|price       | Sale price of each property |
|bedrooms    | Number of bedrooms|
|bathrooms   | Number of bathrooms|
|sqft_living | Square footage of the apartments interior living space|
|sqft_lot    | Square footage of the land space|
|floors      | Number of floors|
|waterfront  | A dummy variable for whether the apartment was overlooking the waterfront or not|
|view        | An index from 0 to 4 of how good the view of the property was|
|condition   | An index from 1 to 5 on the condition of the apartment|
|grade       | An index from 1 to 13, where 1-3 small buildings, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design.|
|sqft_above  | The square footage of the interior housing space that is above ground level|
|sqft_basement | The square footage of the interior housing space that is below ground level|
|yr_built      | The year the property was initially built|
|yr_renovated  | The year of the property’s last renovation|
|zipcode       | What zipcode(region) area the property is in|
|lat           | Lattitude|
|long          | Longitude|
|sqft_living15 | The square footage of interior housing living space for the nearest 15 neighbors|
|sqft_lot15    | The square footage of the land lots of the nearest 15 neighbors|


# 3. Solution Strategy
My strategy to solve this challenge was:


# 4. Top 3 Data Insights
**Hypothesis 01:** Properties that have a view of the water are 20% more expensive on average

**True:** As observed, properties that have a view of the water are more expensive on average with 95% confidence. Property are up to 77% more expensive.

**Hypothesis 02:** Properties with a construction date less than 1955 are 50% cheaper on average. 

**False:** As observed, properties with a construction date less than 1955 are ~15% cheaper. 

**Hypothesis 03:** Properties without basement are 40% larger than properties with basement

**False:** As observed, properties without basement are ~25% larger than properties with basement

# 5. Business Results
Our full original data set contains the records of 21,613 propertys, among them 10,502 are valid for purchase. Suppose we were to purchase and sell all propertys valid at the highest profit season. Thus, translating it to business numbers.

 Selling Season | Fall                | Spring            | Summer          | Winter        | Total Year          | 
--------------- | ------------------- | ----------------- | --------------- |-------------- |-----------------    |
Profit          | US$1,094,528,917.80 | US$125,757,524.10 | US$2,100,642.00 | US$585,000.00 | US$1,222,972,142.90 |
 
# 6. Next Steps to Improve

## References:
- Seasons Impact Real Estate [Investopedia](https://www.investopedia.com/articles/investing/010717/seasons-impact-real-estate-more-you-think.asp)
- How Much Value Does Living the Lakefront Dream Add to a Property? [HomeLight](https://www.homelight.com/blog/how-much-value-does-a-lakefront-add-to-a-property/)
