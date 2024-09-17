from django.shortcuts import render

def home(request):
    bio = {
        'background': 'I am a software developer with a passion for learning and building meaningful projects.',
        'career_goals': 'My goal is to leverage my skills in Python and Django to build scalable web applications and grow as a developer.'
    }
    skills = ['Python', 'Django', 'JavaScript', 'HTML/CSS', 'Git', 'Teamwork', 'Problem Solving']
    job_history = [
        {
            'job_title': 'Software Developer',
            'company': 'Apple Maps Project',
            'description': 'Working on enhancing mapping solutions and implementing new features.'
        },
        {
            'job_title': 'Junior Developer',
            'company': 'XYZ Tech',
            'description': 'Developed and maintained web applications using Django and React.'
        }
    ]
    education = [
        {
            'degree': 'B.Sc. in Computer Science',
            'institution': 'University of XYZ',
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
        'email': 'your-email@example.com',
        'linkedin': 'https://linkedin.com/in/yourprofile',
        'github': 'https://github.com/yourusername'
    }
    return render(request, 'portfolio_app/home.html', {
        'projects': projects,
        'bio': bio,
        'skills': skills,
        'job_history': job_history,
        'education': education,
        'contact_links': contact_links
    })
