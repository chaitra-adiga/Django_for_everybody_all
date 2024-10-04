from django.forms import ModelForm
from autos.models import Make


# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'

'''This code defines a Django form for the Make model using ModelForm. Here's a step-by-step explanation:

1.Import Statements:
from django.forms import ModelForm: Imports the ModelForm class from Django's forms module.
ModelForm is a helper class that creates a form from a Django model.
from autos.models import Make: Imports the Make model from the autos app's models module.

2.Form Class Definition:
class MakeForm(ModelForm):: Defines a new form class named MakeForm that inherits from ModelForm.
Meta Class:

3.class Meta:: Defines an inner Meta class to specify metadata options for the form.
model = Make: Specifies that this form is associated with the Make model.
fields = '__all__': Indicates that all fields from the Make model should be included in the form.

4.Summary
This MakeForm class will automatically generate form fields for all the fields in the Make model,
making it easy to create and validate forms based on the Make model.

'''