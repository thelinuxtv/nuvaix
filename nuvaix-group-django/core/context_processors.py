from .models import Enquiry
def site_choices(request):
    return {"enquiry_choices": Enquiry.ENQUIRY_TYPES}
