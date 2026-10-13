from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import Http404
from django.views.decorators.http import require_http_methods
from .models import Enquiry

BUSINESSES = [
 {"number":"01","slug":"construction-engineering","name":"Construction & Engineering","category":"Construction, engineering and project management","capabilities":["Construction","Engineering","Project management"]},
 {"number":"02","slug":"real-estate","name":"Real Estate & Property","category":"Real estate and property services","capabilities":["Real estate services","Property services"]},
 {"number":"03","slug":"technology-it-solutions","name":"Technology & IT Solutions","category":"Technology and IT solutions","capabilities":["Technology solutions","IT solutions"]},
 {"number":"04","slug":"automobile","name":"Automobile Services","category":"Automobile services","capabilities":["Automobile services"]},
 {"number":"05","slug":"logistics","name":"Logistics & Supply Chain","category":"Logistics and supply chain","capabilities":["Logistics","Transportation","Import and export"]},
 {"number":"06","slug":"manufacturing","name":"Manufacturing & Industrial","category":"Manufacturing and industrial operations","capabilities":["Manufacturing","Industrial operations"]},
 {"number":"07","slug":"healthcare","name":"Healthcare Services","category":"Healthcare support services","capabilities":["Healthcare support","Pharmaceutical distribution","Medical supply services"]},
 {"number":"08","slug":"retail-agriculture","name":"Retail & Agriculture","category":"Retail trading and agribusiness","capabilities":["Retail trading","Agriculture","Agribusiness"]},
 {"number":"09","slug":"consultancy","name":"Consultancy Services","category":"Consultancy services","capabilities":["Consultancy"]},
 {"number":"10","slug":"investments","name":"Investments & Venture Development","category":"Investment and venture development","capabilities":["Investment","Venture development"]},
]
COMPANY = {"name":"NUVAIX GROUP","legal_name":"NUVAIX SOLUTIONS LTD","rc":"9597904","tagline":"INNOVATE • BUILD • DELIVER • GROW"}
def common(**kwargs):
    return {"company": COMPANY, "businesses": BUSINESSES, **kwargs}

def home(request):
    return render(request, "core/home.html", common(title="A diversified group. A shared ambition.", active="home"))

def businesses(request):
    return render(request, "core/businesses.html", common(title="Our business ecosystem", active="businesses"))

def business_detail(request, slug):
    business = next((item for item in BUSINESSES if item["slug"] == slug), None)
    if business is None:
        raise Http404("Business division not found")
    return render(request, "core/business_detail.html", common(title=business["name"], business=business, active="businesses"))

def about(request):
    return render(request, "core/about.html", common(title="Built on purpose. Focused on progress.", active="about"))

def technology(request):
    return render(request, "core/technology.html", common(title="Technology that moves business forward.", active="technology"))

def paint(request):
    return render(request, "core/paint.html", common(title="Colour your world with confidence.", active="paint"))

def projects(request):
    return render(request, "core/empty_section.html", common(title="Projects", active="projects", eyebrow="Our work", description="Project stories will be published here as approved project information becomes available.", section="projects"))

def insights(request):
    return render(request, "core/empty_section.html", common(title="Insights", active="insights", eyebrow="Ideas and perspectives", description="Articles and company updates will appear here when approved for publication.", section="insights"))

def careers(request):
    return render(request, "core/empty_section.html", common(title="Build what comes next.", active="careers", eyebrow="Careers", description="There are no verified open positions published at this time. Contact us to make a general enquiry.", section="careers"))

def partnerships(request):
    return render(request, "core/empty_section.html", common(title="Let's build meaningful partnerships.", active="partnerships", eyebrow="Partnerships", description="We welcome thoughtful enquiries from organizations aligned with our areas of work.", section="partnerships"))

@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        enquiry_type = request.POST.get("enquiry_type", "general")
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()
        errors = []
        if not name or len(name) > 120: errors.append("Please enter your name.")
        try: validate_email(email)
        except ValidationError: errors.append("Please enter a valid email address.")
        if enquiry_type not in dict(Enquiry.ENQUIRY_TYPES): errors.append("Please choose a valid enquiry type.")
        if not subject or len(subject) > 180: errors.append("Please enter a subject.")
        if not message or len(message) > 5000: errors.append("Please enter a message (up to 5,000 characters).")
        if errors:
            for error in errors: messages.error(request, error)
            return render(request, "core/contact.html", common(title="Start a conversation", active="contact", form_data=request.POST, enquiry_choices=Enquiry.ENQUIRY_TYPES))
        Enquiry.objects.create(name=name, email=email, phone=phone[:40], enquiry_type=enquiry_type, subject=subject, message=message)
        messages.success(request, "Thank you. Your enquiry has been received.")
        return redirect("contact")
    return render(request, "core/contact.html", common(title="Start a conversation", active="contact", form_data={}, enquiry_choices=Enquiry.ENQUIRY_TYPES))

def legal(request, kind):
    title = "Privacy notice" if kind == "privacy" else "Terms of use"
    description = ("This site collects the information you submit through the contact form to respond to your enquiry. Contact the company for questions about data handling. This starter notice should be reviewed by qualified counsel before launch." if kind == "privacy" else "Use this website lawfully and do not attempt to disrupt, misuse, or gain unauthorized access to its systems. These terms require legal review before production launch.")
    return render(request, "core/legal.html", common(title=title, active=kind, description=description))
