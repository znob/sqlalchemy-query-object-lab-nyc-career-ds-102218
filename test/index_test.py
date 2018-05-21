import unittest, sqlite3, sys
sys.path.insert(0, '..')
from queries import *

class TestQueries(unittest.TestCase):
    def test_return_apple(self):
        apple = return_apple()
        result = 'Apple'
        self.assertEqual(apple.company, result)

    def test_return_disneys_industry(self):
        disney = return_disneys_industry()
        result = 'Broadcasting\xa0and\xa0entertainment'
        self.assertEqual(disney, result)

    def test_return_list_of_company_objects_ordered_alphabetically_by_symbol(self):
        companies = return_list_of_company_objects_ordered_alphabetically_by_symbol()
        def format():
            result_arr = []
            for company in companies:
                result_arr.append(company.company)
            return result_arr

        result = ['Apple', 'American Express', 'Boeing', 'Caterpillar', 'Cisco Systems', 'Chevron', 'Walt Disney', 'DowDuPont', 'General Electric', 'Goldman Sachs', 'The Home Depot', 'IBM', 'Intel', 'Johnson & Johnson', 'JPMorgan Chase', 'Coca-Cola', "McDonald's", '3M', 'Merck', 'Microsoft', 'Nike', 'Pfizer', 'Procter & Gamble', 'Travelers', 'UnitedHealth Group', 'United Technologies', 'Visa', 'Verizon', 'Walmart', 'ExxonMobil']

        self.assertEqual(format(), result)

    def test_return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending(self):
        tech = return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending()

        result = [{'company': 'Apple', 'EV': 954.8}, {'company': 'Microsoft', 'EV': 708.61}, {'company': 'Intel', 'EV': 244.6}, {'company': 'IBM', 'EV': 178.63}, {'company': 'Cisco Systems', 'EV': 174.31}]
        self.assertEqual(tech, result)

    def test_return_list_of_consumer_products_companies_with_EV_above_225(self):
        cos = return_list_of_consumer_products_companies_with_EV_above_225()
        result = [{'name': 'The Home Depot'}, {'name': 'Walmart'}]
        self.assertEqual(cos, result)

    def test_return_conglomerates_and_pharmaceutical_companies(self):
        conglomerceuticals = return_conglomerates_and_pharmaceutical_companies()
        result = ['3M', 'General Electric', 'Johnson & Johnson', 'Merck', 'Pfizer', 'United Technologies']
        self.assertEqual(conglomerceuticals, result)

    def test_return_name_and_industry_of_top_three_EV_companies(self):
        largest = return_name_and_industry_of_top_three_EV_companies()
        result = [{'name': 'Apple', 'industry': 'Technology'}, {'name': 'Microsoft', 'industry': 'Technology'}, {'name': 'ExxonMobil', 'industry': 'Oil & gas'}]
        self.assertEqual(largest, result)
