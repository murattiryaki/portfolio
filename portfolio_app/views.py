from django.shortcuts import render

def home(request):
    bio = {
        'background': 'xxxx',
        'career_goals': 'My goal is to leverage my skills in Python and Django to build scalable web applications and grow as a developer.'
    }
    skills = ['Python', 'Django', 'JavaScript', 'HTML/CSS', 'Git', 'Teamwork', 'Problem Solving']
    job_history = [
        {
            'job_title': 'xxxx',
            'company': 'Apple Maps Project',
            'description': 'Working on enhancing mapping solutions and implementing new features.'
        },
        {
            'job_title': 'xxxxx',
            'company': 'xxxx',
            'description': 'Developed and maintained web applications using Django and React.'
        }
    ]
    education = [
        {
            'degree': 'TUD',
            'institution': 'xxxx',
            'description': 'Focused on software development and data structures.'
        }
    ]
    projects = [
        {
            'title': 'Project 1',
            'description': 'A description of Project 1.',
            'github_url': 'https://github.com/yourusername/project1'
        },
        {
            'title': 'Project 2',
            'description': 'A description of Project 2.',
            'github_url': 'https://github.com/yourusername/project2'
        }
    ]
    contact_links = {
        'email': 'murat.dublin@gmail.com',
        'linkedin': 'https://linkedin.com/in/murattiryaki',
        'github': 'https://github.com/murattiryaki'
    }
    return render(request, 'portfolio_app/home.html', {
        'projects': projects,
        'bio': bio,
        'skills': skills,
        'job_history': job_history,
        'education': education,
        'contact_links': contact_links
    })
