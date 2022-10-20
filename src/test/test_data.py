import unittest
from src.read_data import GetCvData
from config import get_path

# Get path first
file = get_path()

# Instantiate GetCvData
data = GetCvData(file)


class TestIfDataIsValid(unittest.TestCase):

    def test_open_and_read(self):
        expected_output = [{'name': 'Bogdan Avram', 'education': [
            {'school': 'University Vasile Alecsandri', 'degree': "Bachelor's degree", 'start_date': 'oct-2009',
             'end_date': 'jul-2012'}], 'personal': [
            'I am a software development professional with over 5 years of experience in designing, implementing and testing software solutions.\n\nMy area of expertise includes developing solutions for business domains such as telecom solutions, sensor data gathering and aggregation, ERP, and educational tools.\n\nFrom a technical perspective my experience is focused on Python language, technologies and frameworks, mostly from a back-end perspective.'],
                            'experience': [
                                {'id': 1, 'company_name': 'Endava', 'location': 'Bucharest', 'start_date': 'oct-2020',
                                 'end_date': 'jul-2022', 'industry': 'IT Services', 'description': [
                                    '\nResponsibilities:\n•\tDevelop the microservices that were necessary for the system, create and update the database structure using Alembic and performing manual tests to ensure that they work on the client’s development environment.\n•\tCreated REST API using Django and Django Rest Framework and Flask\n•\tEstablished CI/CD pipeline using GitHub and CircleCI\n•\tDeveloped Python package using Flask/Django\n•\tImplemented Unit Testing for multiple Python projects\n•\tManaged and set up Linux servers\n\n\nTechnologies: Python, PostgreSQL, Docker, Ansible, RESTful API, Linux, Network tunneling.\n\nLanguages & Databases:\nPython – 3.5 years\nJava – 6 months\nMySQL – 3 years\nPostgreSQL – 3 years\nBash – 2 years\nMongoDb - 2 years\n\n\nTools:\nPyCharm – 3 years\nVisual Studio Code – 4 years\nGit – 2 years\nDocker – 2 years\nFlask – 3 years\nJenkins – 2 years\nLinux – 3 years\nStop Light Studio – 4 months\nRestful API – 2 years\nAnsible – 2 years\nAlembic – 4 months\nEclipse – 1 year\nDjango – 2 years\n\n\nTechniques & Methods:\tAgile (Scrum) – 2 years\n\n\nTechnical skills: \nSoftware design, Software development, Testing'],
                                 'headline': 'Software Developer'},
                                {'id': 2, 'company_name': 'Upwork', 'location': 'USA', 'start_date': 'january-2019',
                                 'end_date': 'present', 'industry': 'Freelance Platform', 'description': [
                                    'Experienced in writing and testing code, debugging programs and integrating applications with third-party web services. Specialized in programming and development of a variety of applications (program scripting, big data manipulation, web servers). \n\nProjects description: \n-\tImplement CRM/Sales/HR module with basic and special operations\n-\tGame statistics: using modules, conforming to test requirements, filtering data, working with external files, handling errors.\n-\tPassword checker project: I’ve used Python with Visual Studio Code, hashlib, request library.\n-\tStrong experience in integrating user-facing elements into applications, writing effective, clean code and developing back-end components to improve responsiveness and overall performance.\n\n\nTools: Python (Pandas, pygame, numpy, sklearn), CSS, HTML, JavaScript, Python web framework (Django, Flask)\nText editors: Visual Studio Code, Jupyter Notebook, Sublime text, Atom.\nIDE: Pycharm'],
                                 'headline': 'Python developer'}]}]
        read_all_data = data.open_and_read()
        self.assertEqual(expected_output, read_all_data)

    def test_get_education(self):

        expected_output = [{'school': 'University Vasile Alecsandri', 'degree': "Bachelor's degree", 'start_date': 'oct-2009', 'end_date': 'jul-2012'}]
        education = data.get_education()
        self.assertEqual(expected_output, education)

    def test_get_candidate_name(self):

        expected_output = 'Bogdan Avram'
        candidate_name = data.get_candidate_name()
        self.assertEqual(expected_output, candidate_name)

    def test_get_experience(self):

        expected_output = [{'id': 1, 'company_name': 'Endava', 'location': 'Bucharest', 'start_date': 'oct-2020', 'end_date': 'jul-2022', 'industry': 'IT Services', 'description': ['\nResponsibilities:\n•\tDevelop the microservices that were necessary for the system, create and update the database structure using Alembic and performing manual tests to ensure that they work on the client’s development environment.\n•\tCreated REST API using Django and Django Rest Framework and Flask\n•\tEstablished CI/CD pipeline using GitHub and CircleCI\n•\tDeveloped Python package using Flask/Django\n•\tImplemented Unit Testing for multiple Python projects\n•\tManaged and set up Linux servers\n\n\nTechnologies: Python, PostgreSQL, Docker, Ansible, RESTful API, Linux, Network tunneling.\n\nLanguages & Databases:\nPython – 3.5 years\nJava – 6 months\nMySQL – 3 years\nPostgreSQL – 3 years\nBash – 2 years\nMongoDb - 2 years\n\n\nTools:\nPyCharm – 3 years\nVisual Studio Code – 4 years\nGit – 2 years\nDocker – 2 years\nFlask – 3 years\nJenkins – 2 years\nLinux – 3 years\nStop Light Studio – 4 months\nRestful API – 2 years\nAnsible – 2 years\nAlembic – 4 months\nEclipse – 1 year\nDjango – 2 years\n\n\nTechniques & Methods:\tAgile (Scrum) – 2 years\n\n\nTechnical skills: \nSoftware design, Software development, Testing'], 'headline': 'Software Developer'}, {'id': 2, 'company_name': 'Upwork', 'location': 'USA', 'start_date': 'january-2019', 'end_date': 'present', 'industry': 'Freelance Platform', 'description': ['Experienced in writing and testing code, debugging programs and integrating applications with third-party web services. Specialized in programming and development of a variety of applications (program scripting, big data manipulation, web servers). \n\nProjects description: \n-\tImplement CRM/Sales/HR module with basic and special operations\n-\tGame statistics: using modules, conforming to test requirements, filtering data, working with external files, handling errors.\n-\tPassword checker project: I’ve used Python with Visual Studio Code, hashlib, request library.\n-\tStrong experience in integrating user-facing elements into applications, writing effective, clean code and developing back-end components to improve responsiveness and overall performance.\n\n\nTools: Python (Pandas, pygame, numpy, sklearn), CSS, HTML, JavaScript, Python web framework (Django, Flask)\nText editors: Visual Studio Code, Jupyter Notebook, Sublime text, Atom.\nIDE: Pycharm'], 'headline': 'Python developer'}]
        experience = data.get_experience()
        self.assertEqual(expected_output, experience)


if __name__ == '__main__':
    unittest.main()
