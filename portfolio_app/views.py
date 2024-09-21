from django.shortcuts import render

def home(request):
    objective = {
        'objective': 'Motivated and detail-oriented software developer with a passion for building scalable, user-friendly web applications using Python and Django. Eager to contribute to innovative projects and further enhance my coding skills in a professional setting. Currently, focusing on improving my algorithm skills using LeetCode and contributing to open-source projects, while continuing to learn Python and Django through online courses.'
    }
    skills = [
        'Python', 'HTML', 'CSS', 'JavaScript', 'C#', 'Azure', 'AWS', 
        'MySQL', 'Data Analysis', 'Speech Recognition', 'Artificial Intelligence', 'Data Processing', 
        'Natural Language Processing', 'Linguistic Modeling'
    ]
    job_history = [
        {
            'job_title': 'Data Quality Controller',
            'company': 'TELUS International',
            'dates': 'Jan 2019 - Present'
        },
        {
            'job_title': 'Customer Service and Business Data Technician',
            'company': 'Moravia (Outsourced to Apple)',
            'dates': '04/2018 – 12/2018 - Cork, Ireland'
        },
        {
            'job_title': 'Sales Engineer',
            'company': 'Henkel',
            'dates': '05/2015 – 01/2017 - Istanbul, Turkey'
        },
        {
            'job_title': 'Sales Engineer',
            'company': 'Forbo Movement Systems',
            'dates': '03/2013 – 04/2015 - Istanbul, Turkey'
        },
        {
            'job_title': 'Customer Service Technical Specialist',
            'company': 'Fiat Turkey',
            'dates': '05/2010 - 03/2013'
        }
    ]
    education = [
        {
            'degree': 'Postgraduate Diploma in International Business (NFQ Level 9)',
            'institution': 'Griffith College Dublin',
            'dates': '2018'
        },
        {
            'degree': 'Mechanical Engineering',
            'institution': 'Istanbul University',
            'dates': '2004'
        },
        {
            'degree': 'Higher Diploma in Science in Computing',
            'institution': 'Technological University Dublin',
            'dates': 'Expected Graduation: September 2024'
        }
    ]
    certifications = [
        {
            'name': 'AWS Certified Cloud Practitioner',
            'issuer': 'Amazon Web Services (AWS)',
            'date': 'August 2024',
            'credential_id': '0e5bc7e8e06145f59b33b2dc362ea2c2',
            'url': 'https://cp.certmetrics.com/amazon/en/public/verify/credential/0e5bc7e8e06145f59b33b2dc362ea2c2'
        },
        {
            'name': 'Elements of Artificial Intelligence',
            'issuer': 'University of Helsinki',
            'date': 'September 2019',
            'credential_id': 'b998vw59sho',
            'url': 'https://certificates.mooc.fi/validate/b998vw59sho'
        },
        {
            'name': 'Cloud Computing Sales',
            'issuer': 'Udemy',
            'date': 'September 2019',
            'credential_id': 'UC-085QTO8R',
            'url': 'https://udemy-certificate.s3.amazonaws.com/pdf/UC-085QTO8R.pdf'
        }
    ]
    
    projects = [
        {
            'title': 'Football Match Day Travel Planning App',
            'description': 'Designed and developed a full-stack web app allowing users to search for football teams, venues, and fixtures, and plan their match day travel. Integrated Google Maps API for directions and nearby points of interest. Implemented user authentication, reviews, and ratings features. Deployed on Azure with Azure SQL Database for user-generated content.',
            'github_url': 'https://github.com/murattiryaki/Final_Project_Football_App',
            'live_demo': 'https://football-app.azurewebsites.net/'
        },
        {
            'title': 'Personal Portfolio Website',
            'description': 'Created a personal portfolio to display software development projects, resume, and GitHub repositories. Implemented a clean, responsive design using Bootstrap and managed the backend with Django for dynamic content management.',
            'github_url': 'https://github.com/murattiryaki/portfolio',
            'live_demo': 'https://muratportfolio.azurewebsites.net/'
        },
        {
            'title': 'Project 3',
            'description': '',
            'github_url': 'https://github.com/murattiryaki/ecommerce-prototype',
            'live_demo': 'https://ecommerce-prototype.herokuapp.com'
        }
    ]
    
    return render(request, 'portfolio_app/home.html', {
        'projects': projects,
        'objective': objective,
        'skills': skills,
        'job_history': job_history,
        'education': education,
        'certifications': certifications
    })
