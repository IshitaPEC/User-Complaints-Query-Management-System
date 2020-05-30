from django import forms
from datetime import datetime
from myportfolio import models
from django.contrib.auth.models import User

class ApproveInput_DGP(forms.ModelForm):
    description=forms.CharField(
        disabled=True,
        required=False
    )

    Name=forms.CharField(
        disabled=True,
        required=False
    )

    Aadhar=forms.CharField(
        disabled=True,
        required=False
    )
    Contact_Number=forms.CharField(
        disabled=True,
        required=False
    )
    Email_id=forms.CharField(
        disabled=True,
        required=False
    )
    Address=forms.CharField(
        disabled=True,
        required=False
    )
    City=forms.CharField(
        disabled=True,
        required=False
    )
    State=forms.CharField(
        disabled=True,
        required=False
    )

    PIN_Code=forms.CharField(
        disabled=True,
        required=False
    )
    title=forms.CharField(
        disabled=True,
        required=False
    )

    up_files=forms.FileField(
        disabled=True,
        required=False
    )

    comments=forms.CharField(
        disabled=True,
        required=False
    )

    comments_aig=forms.CharField(
        disabled=True,
        required=False
    )

    action_taken=forms.CharField(
        disabled=True,
        required=False
    )


    reconsider_aig=forms.CharField(
        disabled=True,
        required=False
        )

    reconsider_dgp=forms.CharField(
        required=False
        )

    to_user=forms.ModelChoiceField(queryset=User.objects.filter(username='AIG1')|User.objects.filter(username='AIG2')|User.objects.filter(username='AIG3')|User.objects.filter(username='Complainant'))
    class Meta:
        #specify the Model to be used in this form
        #model = ModelClassName

        model = models.Message
        fields = ['to_user','Name','Aadhar','Contact_Number','Email_id','Address','City','State','PIN_Code','title','description','up_files','comments','comments_aig','action_taken','is_approved_dgp','is_reconsider_dgp','reconsider_aig','reconsider_dgp','is_actiontaken']



class Reconsider_AIG(forms.ModelForm):
    description=forms.CharField(
        disabled=True,
        required=False
        )

    Name=forms.CharField(
        disabled=True,
        required=False
        )

    Aadhar=forms.CharField(
        disabled=True,
        required=False
        )
    Contact_Number=forms.CharField(
        disabled=True,
        required=False
        )
    Email_id=forms.CharField(
        disabled=True,
        required=False
        )
    Address=forms.CharField(
        disabled=True,
        required=False
        )
    City=forms.CharField(
        disabled=True,
        required=False
        )
    State=forms.CharField(
        disabled=True,
        required=False
        )

    PIN_Code=forms.CharField(
        disabled=True,
        required=False
        )
    title=forms.CharField(
        disabled=True,
        required=False
        )

    up_files=forms.FileField(
        disabled=True,
        required=False
        )

    comments=forms.CharField(
        disabled=True,
        required=False
        )

    comments_aig=forms.CharField(
        disabled=True,
        required=False
        )

    action_taken=forms.CharField(
        disabled=True,
        required=False
        )


    is_approved_dgp=forms.BooleanField(
        disabled=True,
        required=False
        )

    is_reconsider_dgp=forms.BooleanField(
        disabled=True,
        required=False
        )

    reconsider_dgp=forms.CharField(
        disabled=True,
        required=False
        )

    reconsider_aig=forms.CharField(
        required=False
    )

    to_user=forms.ModelChoiceField(queryset=User.objects.filter(username='SHO1')|User.objects.filter(username='SHO2')|User.objects.filter(username='SHO3'))


    class Meta:
            #specify the Model to be used in this form
            #model = ModelClassName

        model = models.Message
        fields = ['to_user','Name','Aadhar','Contact_Number','Email_id','Address','City','State','PIN_Code','title','description','up_files','comments','comments_aig','action_taken','is_approved_dgp','is_reconsider_dgp','reconsider_dgp','is_reconsider_aig','is_approved_aig','reconsider_aig','is_actiontaken']


class Reconsider_SHO(forms.ModelForm):
    description=forms.CharField(
        disabled=True,
        required=False
        )

    Name=forms.CharField(
        disabled=True,
        required=False
        )

    Aadhar=forms.CharField(
        disabled=True,
        required=False
        )
    Contact_Number=forms.CharField(
        disabled=True,
        required=False
        )
    Email_id=forms.CharField(
        disabled=True,
        required=False
        )
    Address=forms.CharField(
        disabled=True,
        required=False
        )
    City=forms.CharField(
        disabled=True,
        required=False
        )
    State=forms.CharField(
        disabled=True,
        required=False
        )

    PIN_Code=forms.CharField(
        disabled=True,
        required=False
        )
    title=forms.CharField(
        disabled=True,
        required=False
        )

    up_files=forms.FileField(
        disabled=True,
        required=False
        )

    comments=forms.CharField(
        disabled=True,
        required=False
        )

    comments_aig=forms.CharField(
        disabled=True,
        required=False
        )




    reconsider_dgp=forms.CharField(
        disabled=True,
        required=False
        )

    reconsider_aig=forms.CharField(
        disabled=True,
        required=False
        )

    is_reconsider_aig=forms.BooleanField(
        disabled=True,
        required=False
        )

    is_approved_aig=forms.BooleanField(
        disabled=True,
        required=False
        )


    is_actiontaken=forms.BooleanField(
        required=True
            )


    to_user=forms.ModelChoiceField(User.objects.filter(username='AIG1')|User.objects.filter(username='AIG2')|User.objects.filter(username='AIG3'))
    class Meta:
            #specify the Model to be used in this form
            #model = ModelClassName

        model = models.Message
        fields = ['to_user','Name','Aadhar','Contact_Number','Email_id','Address','City','State','PIN_Code','title','description','up_files','comments','comments_aig','reconsider_dgp','is_reconsider_aig','is_approved_aig','reconsider_aig','is_actiontaken','action_taken']



class ApproveInput_AIG(forms.ModelForm):
    description=forms.CharField(
        disabled=True,
        required=False
    )

    Name=forms.CharField(
        disabled=True,
        required=False
    )

    Aadhar=forms.CharField(
        disabled=True,
        required=False
    )
    Contact_Number=forms.CharField(
        disabled=True,
        required=False
    )
    Email_id=forms.CharField(
        disabled=True,
        required=False
    )
    Address=forms.CharField(
        disabled=True,
        required=False
    )
    City=forms.CharField(
        disabled=True,
        required=False
    )
    State=forms.CharField(
        disabled=True,
        required=False
    )

    PIN_Code=forms.CharField(
        disabled=True,
        required=False
    )
    title=forms.CharField(
        disabled=True,
        required=False
    )

    up_files=forms.FileField(
        disabled=True,
        required=False
    )

    comments=forms.CharField(
        disabled=True,
        required=False
    )

    comments_aig=forms.CharField(
        disabled=True,
        required=False
    )

    action_taken=forms.CharField(
        disabled=True,
        required=False
    )

    reconsider_aig=forms.CharField(
        required=False
    )

    to_user=forms.ModelChoiceField(queryset=User.objects.filter(username='DGP_PUNJAB')|User.objects.filter(username='SHO1')|User.objects.filter(username='SHO2')|User.objects.filter(username='SHO3'))


    class Meta:
        #specify the Model to be used in this form
        #model = ModelClassName

        model = models.Message
        fields = ['to_user','Name','Aadhar','Contact_Number','Email_id','Address','City','State','PIN_Code','title','description','up_files','comments','comments_aig','action_taken','is_approved_aig','is_reconsider_aig','reconsider_aig','is_actiontaken']



class MessageInput(forms.ModelForm):
    description=forms.CharField(
        disabled=True,
        required=False
    )

    Name=forms.CharField(
        disabled=True,
        required=False
    )
    Aadhar=forms.CharField(
        disabled=True,
        required=False
    )
    Contact_Number=forms.CharField(
        disabled=True,
        required=False
    )
    Email_id=forms.CharField(
        disabled=True,
        required=False
    )
    Address=forms.CharField(
        disabled=True,
        required=False
    )
    City=forms.CharField(
        disabled=True,
        required=False
    )
    State=forms.CharField(
        disabled=True,
        required=False
    )

    PIN_Code=forms.CharField(
        disabled=True,
        required=False
    )
    title=forms.CharField(
        disabled=True,
        required=False
    )

    up_files=forms.FileField(
        disabled=True,
        required=False
    )


    to_user=forms.ModelChoiceField(queryset = User.objects.filter(username='AIG1')|User.objects.filter(username='AIG2')|User.objects.filter(username='AIG3'))


    class Meta:
        #specify the Model to be used in this form
        #model = ModelClassName

        model = models.Message
        fields = ['to_user','Name','Aadhar','Contact_Number','Email_id','Address','City','State','PIN_Code','title','description','up_files','comments']



#Form for aig->forwarding
class MessageInput_AIG(forms.ModelForm):
    description=forms.CharField(
        disabled=True,
        required=False
    )

    comments=forms.CharField(
        disabled=True,
        required=False,

    )

    Name=forms.CharField(
        disabled=True,
        required=False
    )
    Aadhar=forms.CharField(
        disabled=True,
        required=False
    )
    Contact_Number=forms.CharField(
        disabled=True,
        required=False
    )
    Email_id=forms.CharField(
        disabled=True,
        required=False
    )
    Address=forms.CharField(
        disabled=True,
        required=False
    )
    City=forms.CharField(
        disabled=True,
        required=False
    )
    State=forms.CharField(
        disabled=True,
        required=False
    )

    PIN_Code=forms.CharField(
        disabled=True,
        required=False
    )
    title=forms.CharField(
        disabled=True,
        required=False
    )

    up_files=forms.FileField(
        disabled=True,
        required=False
    )


    to_user=forms.ModelChoiceField(queryset = User.objects.filter(username='SHO1')|User.objects.filter(username='SHO2')|User.objects.filter(username='SHO3'))

    class Meta:
        #specify the Model to be used in this form
        #model = ModelClassName

        model = models.Message
        fields = ['to_user','Name','Aadhar','Contact_Number','Email_id','Address','City','State','PIN_Code','title','description','up_files','comments','comments_aig']


class MessageInp(forms.ModelForm):
    description=forms.CharField(
        disabled=True
    )


    class Meta:
        model = models.Message
        widgets = {'from_user': forms.HiddenInput(),'to_user':forms.HiddenInput()}
        fields = ['to_user','from_user','description','action_taken']


class ArchivedForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['is_archived']


#Form for SHO->Reply
class MessageInput_SHO(forms.ModelForm):
    description=forms.CharField(
        disabled=True,
        required=False
    )

    comments=forms.CharField(
        disabled=True,
        required=False
    )

    Name=forms.CharField(
        disabled=True,
        required=False
    )
    Aadhar=forms.CharField(
        disabled=True,
        required=False
    )
    Contact_Number=forms.CharField(
        disabled=True,
        required=False
    )
    Email_id=forms.CharField(
        disabled=True,
        required=False
    )
    Address=forms.CharField(
        disabled=True,
        required=False
    )
    City=forms.CharField(
        disabled=True,
        required=False
    )
    State=forms.CharField(
        disabled=True,
        required=False
    )

    PIN_Code=forms.CharField(
        disabled=True,
        required=False
    )
    title=forms.CharField(
        disabled=True,
        required=False
    )

    up_files=forms.FileField(
        disabled=True,
        required=False
    )

    is_actiontaken=forms.BooleanField(
         required=True
    )

    to_user=forms.ModelChoiceField(queryset=User.objects.filter(username='AIG1')|User.objects.filter(username='AIG2')|User.objects.filter(username='AIG3'))

    # from_user = forms.CharField(
    #     disabled=True,
    #     required=False,
    #
    # )

    class Meta:
        #specify the Model to be used in this form
        #model = ModelClassName

        model = models.Message
        fields = ['to_user','Name','Aadhar','Contact_Number','Email_id','Address','City','State','PIN_Code','title','description','up_files','comments','comments_aig','action_taken','is_actiontaken']
