import os
from linkedin_api import Linkedin

def search_company():
    
    company_name='nearsecure'
    # Authenticate with LinkedIn API
    api = Linkedin(
        os.environ.get('beloudha@gmail.com'),
        os.environ.get('Blue360@1999'),
        refresh_cookies=True
    )
    
    # Search for the company by name
    companies = api.search_company(company_name)
    
    # Get the company ID of the first result
    company_id = companies[0]['entityUrn'].split(':')[3]
    
    # Get the employees of the company
    employees = api.get_company_employees(company_id)
    
    # Format the employee data as text
    employee_text = ''
    for employee in employees:
        name = employee['firstName'] + ' ' + employee['lastName']
        job_title = employee['headline']
        employee_text += f'{name} - {job_title}\n'
    
    return employee_text
