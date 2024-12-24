from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects_show=[

        {"title":"Recruitment System API", 
         "path":"images/recruitment-system-img.jpeg",
         "url": "https://github.com/hrutikas2002/Recruitment_System_FastAPI/tree/main"},

         {"title":"Audio Transcription and Summarization System", 
         "path":"images/audio-trans-img.jpeg",
         "url": "https://github.com/hrutikas2002/Audio-Transcription-and-Summarization-with-FastAPI"},


         {"title":"To Do Web App", 
         "path":"images/todo-img.jpg",
        "url": "https://github.com/hrutikas2002/To-Do-Hub"},

    ]
    return render(request, 'projects.html',{"projects_show":projects_show})

def experiences(request):

    experiences = [
        {"company":"CentraLogic Consultancy, pune",
         "role":"Python/AIML Trainee",
         "duration":"June 2024 – July 2024",
         "outcome":"Gained experience in Python and foundational knowledge in AIML during a 2-month traineeship. \n Strengthened Python programming skills with focusing on writing efficient code. \n Developed backend development skills using FastAPI"
         },

         {"company":"Celebal Technologies, Jaipur",
         "role":"Web-Developer Intern",
         "duration":"June 2023 – Aug 2023",
         "outcome":"Gained experience in web development during an internship at Celebal Technologies. \n Strengthened skills in frontend development using HTML, CSS, JavaScript. \n Developed interactive web application, focusing on user-friendly designs"

         },

         {"company":"TheResolvedTech, India",
         "role":"Web-Developer Intern",
         "duration":"Feb 2023 - Mar 2023",
         "outcome":"Gained practical knowledge of utilizing HTML, CSS, and JavaScrip. \n Gained experience in web development. \n  Designed and developed an interactive web application"

         }
    ]
    return render(request, "experiences.html",{"experiences":experiences})

def certifications(request):
    certificates = [
        {
            "title":"Campus to Technical Careers Training program",
            "organization": "TNS India Foundation",
            "issue_date": "February 2024",
            "description": "Completed training in MySQL, Core Java, Hibernate, Spring Boot, and web development (HTML, CSS, JavaScript), with added focus on soft skills enhancement.",
            "link":"https://drive.google.com/file/d/12GrhGqhDrUFA1M5hgVCkE0kZPCpEvng0/view?usp=sharing"
        },

        {
            "title":"Google Data Analytics",
            "organization": "Google via Coursera",
            "issue_date": "February 2023",
            "description": "Gained foundational knowledge in data analytics, including data cleaning, analysis, and visualization using tools like Excel, SQL, and Tableau.",
            "link":"https://drive.google.com/file/d/1GLU6E1W6hAfxGPH16xEkn0EL5Pu3m63_/view?usp=sharing"
        },

        {
            "title": "Basics of Python",
            "organization": "Infosys Springboard",
            "issue_date": "November 2022",  
            "description": "Earned a certification in Basics of Python, covering foundational concepts like data types, loops, and functions.",
            "link":"https://drive.google.com/file/d/1yftmr3G3BNZBVtNGRFiJJtDGgegqeemG/view?usp=sharing"
        }
    ]
    return render (request, "certifications.html",{"certificates" : certificates})

def contact(request):
    return render(request, "contact.html")

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def send_email(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Email content
        subject = f"New Contact Form Submission from {name}"
        email_message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        # Send email
        try:
            send_mail(
                subject,
                email_message,
                'your-email@gmail.com',  # Your Gmail address
                ['your-email@gmail.com'],  # Recipient email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "An error occurred while sending your message. Please try again.")

        return redirect('/')  # Redirect to home or success page
    return redirect('/')

def resume(request):
    return render(request,"resume.html")