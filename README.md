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
  - Property price greater than median price region per season, selling price is added in 30%
  - Property price less than median price region per season, selling price is added in 10%
  - Porperty will be sold in season with the highest profit. 
- Dataset variables:

Variable     | Definition
------------ | -------------
|id          | Unique ID for each property available|
|date        | Date that the property was available|
|price       | Sale price of each property |
|bedrooms    | Number of bedrooms|
|bathrooms   | Number of bathrooms, where .5 accounts for a room with a toilet but no shower, and .75 or ¾ bath is a bathroom that contains one sink, one toilet and either a shower or a bath.|
|sqft_living | Square footage of the apartments interior living space|
|sqft_lot    | Square footage of the land space|
|floors      | Number of floors|
|waterfront  | A dummy variable for whether the apartment was overlooking the waterfront or not|
|view        | An index from 0 to 4 of how good the view of the property was|
|condition   | An index from 1 to 5 on the condition of the apartment|
|grade       | An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design.|
|sqft_above  | The square footage of the interior housing space that is above ground level|
|sqft_basement | The square footage of the interior housing space that is below ground level|
|yr_built      | The year the property was initially built|
|yr_renovated  | The year of the property’s last renovation|
|zipcode       | What zipcode area the property is in|
|lat           | Lattitude|
|long          | Longitude|
|sqft_living15 | The square footage of interior housing living space for the nearest 15 neighbors|
|sqft_lot15    | The square footage of the land lots of the nearest 15 neighbors|


# 3. Solution Strategy
# 4. Top 5 Data Insights
# 5. Business Results
# 6. Next Steps to Improve

## References:
- Seasons Impact Real Estate [Investopedia](https://www.investopedia.com/articles/investing/010717/seasons-impact-real-estate-more-you-think.asp)
- How Much Value Does Living the Lakefront Dream Add to a Property? [HomeLight](https://www.homelight.com/blog/how-much-value-does-a-lakefront-add-to-a-property/)
