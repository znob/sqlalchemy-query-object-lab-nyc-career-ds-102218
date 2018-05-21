from sqlalchemy import create_engine
from seed import Company
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dow_jones.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def return_apple():
    apple = session.query(Company).filter(Company.company=='Apple')[0]
    return apple

def return_disneys_industry():
    disney = session.query(Company).filter(Company.company=='Walt Disney')[0]
    return disney.industry

def return_list_of_company_objects_ordered_alphabetically_by_symbol():
    companies = session.query(Company).order_by(Company.symbol).all()
    return companies

def return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending():
    tech = session.query(Company).filter_by(industry='Technology').order_by(Company.enterprise_value.desc())
    arr = []
    for co in tech:
        obj = {'company': co.company, 'EV': co.enterprise_value}
        arr.append(obj)
    return arr

def return_list_of_consumer_products_companies_with_EV_above_225():
    arr = []
    for company in session.query(Company).filter(Company.industry=='Consumer products', Company.enterprise_value>225).all():
        arr.append({'name': company.company})
    return arr

def return_conglomerates_and_pharmaceutical_companies():
    from sqlalchemy import or_
    arr = []
    for company in session.query(Company).filter(or_(Company.industry=='Conglomerate', Company.industry=='Pharmaceuticals')):
        arr.append(company.company)
    return arr

def return_name_and_industry_of_top_three_EV_companies():
    largest = session.query(Company).order_by(Company.enterprise_value.desc())[0:3]
    arr = []
    for co in largest:
        arr.append({'name': co.company, 'industry': co.industry})
    return arr
