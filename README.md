
# SQLAlchemy Query Objects Lab

In this lab we will use the `query()` method with a `session` to create Query objects and pull data from the database.

## Objectives

1.  Become comfortable working with `query` objects to pull information from a database using SQLAlchemy
2.  Use `filter` and `filter_by` to pull data that meets certain criteria
3.  Use `order_by` to order resulting data and use `desc` to order from highest to lowest
4.  Use an index range to limit the number of results of a query

## Dow Jones Industrials Table 2.0

We will once again query from the table of companies making up the Dow Jones Industrial Average index.  However, this time we will use SQLAlchemy to write SQL commands for us.  Write your SQLAlchemy queries in the methods defined in the `queries.py` file.  A sample from the `companies` table is featured below:

company         |exchange|symbol|industry                         |date_added|enterprise_value|
----------------|--------|------|---------------------------------|----------|----------------|
3M              |NYSE    |MMM   |Conglomerate                     |1976-08-09|133.31          |
American Express|NYSE    |AXP   |Financial services               |1982-08-30|98.08           |
Apple           |NASDAQ  |AAPL  |Technology                       |2015-03-19|954.8           |
Boeing          |NYSE    |BA    |Manufacturing                    |1987-03-12|196.37          |
Caterpillar     |NYSE    |CAT   |Manufacturing                    |1991-05-06|118.42          |
Chevron         |NYSE    |CVX   |Oil & gas                        |2008-02-19|264.51          |

* `return_apple`

Write a qeury that returns a Company object for Apple.  We can get the Company object from the Query object by chaining `[0]` to the end of the query.

* `return_disneys_industry`

Write a query that return a Company object for Disney.  Return the company's industry from this object.

* `return_list_of_company_objects_ordered_alphabetically_by_symbol`

Write a query that returns a list of Company objects for all the companies in the Dow.  The list should be ordered alphabetically by `symbol`.

* `return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending`

Write a query that returns a list of dictionaries for all the technology companies in the DJIA.  Each dictionary will have keys of `'company'` and `EV` that point to the respective company name and enterprise value for each company.  The list should be ordered by enterprise value from greatest to least.

* `return_list_of_consumer_products_companies_with_EV_above_225`

Write a query that returns a those consumer products companies with an enterprise value over $225 billion.  The query should return a list of dictionaries.  Each dictionary will have a key of `name` that points to the company's full name.

* `return_conglomerates_and_pharmaceutical_companies`

Write a query that returns all companies in the conglomerates or pharmaceuticals industries.  The query will return a list of all the company names that match this criteria.

* `test_return_name_and_industry_of_top_three_EV_companies`

Write a query returns the a list of the three companies with the highest enterprise values.  The list will contain dictionaries with keys of `'name'` and `'industry'` that point to each company's respective name and industry.  The list will be ordered descending from the highest enterprise value.
