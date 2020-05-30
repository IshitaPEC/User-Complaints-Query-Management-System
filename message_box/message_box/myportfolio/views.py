from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.template import RequestContext
from myportfolio.models import UserProfileInfo,Message
from django.views.generic import ListView,DetailView
from myportfolio.forms import MessageInput,MessageInp,ArchivedForm,ApproveInput_AIG,ApproveInput_DGP,MessageInput_AIG,Reconsider_AIG,MessageInput_SHO,Reconsider_SHO
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import CreateView, DeleteView, UpdateView,FormMixin
from django.shortcuts import get_list_or_404, get_object_or_404
from datetime import datetime
from rest_framework import viewsets
from myportfolio.serializers import ToUserSerializer
from django.core.paginator import Paginator

import uuid

def homepage(request):
    return render(request,'myportfolio/homepage.html')

def login(request):
    #check if the form has been submitted
    if request.method == 'POST':

        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(username=uname, password=passw)
        if user:
            #user is authenticated
            #check if the user is an active user
            if user.is_active:
                auth_login(request, user)
                #After this step login has taken place, so which page do we redirect to page decided later depending on the user type
                a=UserProfileInfo.objects.get(user=user)
                #Based on the user type, we redirect to the following types:
                #If usre is of type 'DGP_PUNJAB', we redirect to its inbox etc
                print(a.user_type)
                k=a.user_type
                print(type(k))
                if a.user_type.name=='DGP OFFICE PUNJAB':
                    return HttpResponseRedirect(reverse('mess:dgpoffice'))
                elif a.user_type.name=='AIG':
                    return HttpResponseRedirect(reverse('mess:aigoffice'))
                elif a.user_type.name=='SHO':
                    return HttpResponseRedirect(reverse('mess:shooffice'))
            else:
                return HttpResponse("<h1>User Inactive!</h1>")
        else:

            return HttpResponse("<h1>User Unauthenticated!</h1>")
    else:
        return render(request,'myportfolio/login.html')


def lodgeyourcomplaint(request):
    #We lodge the complaint and assign the complaiant an id for his complaint
    #We input his complaint in a form
    if request.method == 'POST':
        name=request.POST.get('Name')
        Aadhar_Card=request.POST.get('Aadhar')
        Contact_Number=request.POST.get('Contact_Number')
        Email_id=request.POST.get('Email_id')
        Address=request.POST.get('Address')
        City=request.POST.get('City')
        State=request.POST.get('State')
        PIN_Code=request.POST.get('PIN_Code')
        title=request.POST.get('title')
        description=request.POST.get('description')
        to_user_name=request.POST.get('reciever')
        from_user=User.objects.filter(username='Complainant')[0]
        to_user=User.objects.filter(username=to_user_name)[0]
        filename=request.FILES.get('myfile')

        #Create an instance out of it and then save it in the model
        b=Message.objects.create(from_user= from_user, Name=name, Aadhar=Aadhar_Card,
        Contact_Number=Contact_Number, Email_id=Email_id, Address=Address, City=City,
         State=State, PIN_Code=PIN_Code, is_archived=False,to_user=to_user,title=title,description=description,
         up_files=filename, release_date=datetime.now())
        b.save()

        #After the form has been submitted, returnto this page
        mess="Your complaint has been registered. Kindly note that your complaint-ID is "+ str(b.pk)
        return render(request,'myportfolio/lodgeyourcomplaint.html',{'message':mess})
    #Else return over here
    return render(request,'myportfolio/lodgeyourcomplaint.html')


def ActionStatus(request):
    #The purpose of this is that the complainant sees the status of his complaint.
    #If the complaint has been approved by the DGP, then only will the action taken be viewed by the complainant
    if request.method=='POST':
        #In a form, we input the complaint_id and his email.
        complaint_id=request.POST.get('complaint_id')
        email=request.POST.get('Email_id')
        #We assign the remaining fields into variables based on that object of the model
        message=Message.objects.filter(pk=complaint_id)[0]
        print(message)
        name=message.Name
        Aadhar_Card=message.Aadhar
        Contact_Number=message.Contact_Number
        Address=message.Address
        City=message.City
        State=message.State
        PIN_Code=message.PIN_Code
        title=message.title
        description=message.description
        up_files=message.up_files
        Action_taken=message.action_taken
        is_approved_dgp=message.is_approved_dgp

        if(email==message.Email_id):

            if(is_approved_dgp==True):
                #If apaproved by DGP, we return the various parameters of the form and present it on the template
                if up_files!='':
                    #If the file has been uploaded then we pass up_files
                    return render(request,'myportfolio/action_status.html',{'complaint_id':complaint_id,'name':name,'Aadhar_Card':Aadhar_Card,
                    'Contact_Number':Contact_Number,'Email_id':email, 'Address':Address,'City':City,'State':State, 'PIN_Code':PIN_Code,
                    'title':title,'description':description,'Action_taken':Action_taken,'up_files':up_files})
                else:
                    #up_files has not been passed
                    return render(request,'myportfolio/action_status.html',{'complaint_id':complaint_id,'name':name,'Aadhar_Card':Aadhar_Card,
                    'Contact_Number':Contact_Number,'Email_id':email, 'Address':Address,'City':City,'State':State, 'PIN_Code':PIN_Code,
                    'title':title,'description':description,'Action_taken':Action_taken})
            else:
                return render(request,'myportfolio/action_status.html',{'mess':'No action Taken'})
        else:
            return render(request,'myportfolio/action_status.html',{'mess':'No such Complaint Exists'})
    return render(request,'myportfolio/action_status.html')

@login_required
def userlogout(request):
    logout(request)
    #redirect the user
    return HttpResponseRedirect(reverse('mess:'))

@method_decorator(login_required, name='dispatch')
class dgpinbox(ListView):
    #This is a list of all the messages which have the to_user as DGP_PUNJAB from_user=Complainant
    #Note that the message can have to_user as DGP only from the complainant or from the AIG after his approval
    #And hence to restrict this to the first case only, is_approved_aig=FALSE
    #is_archived=False
    model=Message
    paginate_by = 10
    context_object_name='messages'
    template_name='myportfolio/dgpinbox.html'


    def get_queryset(self):
        queryset = super(dgpinbox, self).get_queryset()
        queryset = queryset.filter(to_user=self.request.user,is_archived=False,is_actiontaken=False,is_approved_aig=False)
        return queryset


@method_decorator(login_required, name='dispatch')
class MessageDetail(DetailView):
    #This is the detail view for the message shown to the DGP_PUNJAB
    #Note the url for detail view is generated from the list view when the list view uses {{get_absolute_url}} function to generate id of the particular object
    model=Message
    context_object_name='Message_detail'
    template_name='myportfolio/yourmessage.html'

    def get_context_data(self, **kwargs):
        user=self.request.user
        a=UserProfileInfo.objects.get(user=user)
        print(a)
        context = super(MessageDetail, self).get_context_data(**kwargs)
        if a.user_type.name=='DGP OFFICE PUNJAB':
            context['dgp'] = self.request.user.username
        elif a.user_type.name=='AIG':
            context['aig'] = self.request.user.username
        elif a.user_type.name=='SHO':
            context['sho'] = self.request.user.username

        return context


@method_decorator(login_required, name='dispatch')
class MessageDetail_aig(DetailView):
    # This the detail of the message that would be displayed to the AIG for where ever he chooses to click on the 'Show Detail'
    #We know the model now and template
    model=Message
    context_object_name='Message_detail'
    template_name='myportfolio/yourmessageaig.html'

    #The function of the get_context_data allows you to pass any context if you want to in the generic view.
    def get_context_data(self, **kwargs):
        context = super(MessageDetail_aig, self).get_context_data(**kwargs)
        print(self.request.user.username)
        if self.request.user.username=='DGP_PUNJAB':
            context['dgp'] = self.request.user.username
        elif self.request.user.username=='AIG1':
            context['aig'] = self.request.user.username
        elif self.request.user.username=='SHO1':
            context['sho'] = self.request.user.username
        return context

class ForwardMessage(UpdateView):
    #The purpose of this is to forward a message to the AIG, it follows update view protocol
    #The form_class suited to updation is MessageInput
    #The template name for the same is as fllows
    form_class=MessageInput
    template_name='myportfolio/forward.html'
    queryset=Message.objects.all()

    def get_object(self):
        #Method to get id from the url
        complaint_id=self.kwargs.get('id')
        print(complaint_id)
        mess=Message.objects.get(complaint_id=complaint_id)
        mess.from_user=self.request.user
        print(mess.from_user)
        mess.release_date=datetime.now()
        mess.description=mess.description
        mess.is_archived=mess.is_archived

        mess.save()
        return get_object_or_404(Message,complaint_id=complaint_id)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        return redirect ('dgpoffice')





class Archive(UpdateView):
    #We donot want to delete our complaint rather save it for future use and hence we simply archive it
    #This is an update view with an additional feature of is_archived to be marked as true
    #This will happen once the DGP_PUNJAB has approved of the action, he will archive the message
    form_class=ArchivedForm
    template_name='myportfolio/archive.html'
    queryset=Message.objects.all()

    def get_object(self):
        complaint_id=self.kwargs.get('id')
        mess=Message.objects.get(complaint_id=complaint_id)
        mess.from_user=mess.from_user
        mess.description=mess.description
        mess.comments=mess.comments
        mess.action_taken=mess.action_taken
        mess.is_archived=True
        mess.save()
        return get_object_or_404(Message, complaint_id=complaint_id)

        def form_valid(self,form):
            print(form.cleaned_data)
            return super().form_valid(form)


class ArchivedMessage(ListView):
    #This is a list for us to show the archived messages, is_approved_dgp=true, is_archived=true
    #Also we have an option to delete it-> See Delete View for that
    model=Message
    paginate_by=10;
    context_object_name='messages'
    template_name='myportfolio/archived.html'


    def get_queryset(self):
        queryset = super(ArchivedMessage, self).get_queryset()
        queryset = queryset.filter(is_approved_dgp=True)
        return queryset


@method_decorator(login_required, name='dispatch')
class Archived_MessageDetail(DetailView):
    #Just to show the detail of the message archived
    model=Message
    context_object_name='Message_detail'
    template_name='myportfolio/archivedmessage.html'



@method_decorator(login_required, name='dispatch')
class ActionPending_DGP(ListView):
    #For any message till is_actiontaken=False and is_approved_aig=False, Message would be in action pending stage
    model=Message
    paginate_by=10
    context_object_name='messages'
    template_name='myportfolio/actionpending_dgp.html'

    def get_queryset(self):
        queryset = super(ActionPending_DGP, self).get_queryset()
        queryset = queryset.filter(is_actiontaken= False,is_approved_aig=False)
        return queryset



@method_decorator(login_required, name='dispatch')
class ActionPending_AIG(ListView):
    #This is a list of all those objects of the model have been sent to the SHO, action by the SHO has not been tken yet(is_actiontaken=False)
    #And since no action has been taken, the aig has not approved of it either (is_approved_aig=False)
    model=Message
    paginate_by=10
    context_object_name='messages'
    template_name='myportfolio/actionpending_aig.html'

    def get_queryset(self):
        queryset = super(ActionPending_AIG, self).get_queryset()
        queryset = queryset.filter(is_actiontaken= False, is_approved_aig=False)
        return queryset


@method_decorator(login_required, name='dispatch')
class action_taken_aig(ListView):
    #This is a list of all those objects of the model in which the SHO has taen action (is_actiontaken=True)
    #Now it is upto the aig to either send it back to the SHO for recondideration(i.e. mark the is_reconsider_aig=True and at the same time mark is_actiontaken=False)
    #Incase the aig approves of it (s/he must mark the is_approved_aig=True it would go to the DGP)
    model=Message
    paginate_by=10
    context_object_name='messages'
    template_name='myportfolio/action_taken_aig.html'


    def get_queryset(self):
        queryset = super(action_taken_aig, self).get_queryset()
        #So if is_actiontaken=True and is_approved_aig=False and is_approved_dgp=False
        #Note that the AIG might be shown the messages which have been snet in the first go by the SHO, after an attempt of reconsideration
        #In either case the SHO just has mark is_actiontaken.
        #Both of these kind of messages are recieved here
        #Also those messages having is_reconsider_dgp=True must not be recieved here, for that to happen is_actiontaken would be False and hence it has been aken care of
        queryset = queryset.filter(is_actiontaken=True,is_approved_dgp=False,is_approved_aig=False)
        return queryset

@method_decorator(login_required, name='dispatch')
class reconsider_aig(ListView):
    #This is a list of all the messages which have been told by the DGP to reconsider, hence he will mark is_reconsider_dgp=True and is_actiontaken=False
    #Now the AIG will further send it to the SHO to take actions
    model=Message
    paginate_by=10
    context_object_name='messages'
    template_name='myportfolio/reconsider_aig.html'


    def get_queryset(self):
        queryset = super(reconsider_aig, self).get_queryset()
        queryset = queryset.filter(is_reconsider_dgp=True, is_approved_dgp=False,is_approved_aig=True,is_actiontaken=False)
        return queryset

@method_decorator(login_required, name='dispatch')
class reconsider_sho(ListView):
    #This includes all the messages which have been sent to the SHO to further retake his action as they werent
    #After retaking action, he needs to update the action and mark is_actiontaken as true.
    #hence is_reconsider_aig must be true and is_actiontaken must be false.

    model=Message
    paginate_by=10
    context_object_name='messages'
    template_name='myportfolio/reconsider_sho.html'


    def get_queryset(self):
        queryset = super(reconsider_sho, self).get_queryset()
        queryset = queryset.filter(is_reconsider_aig=True,is_actiontaken=False)
        return queryset

class Reconsider(UpdateView):
    #This is the update view for the form where in the AIG sends the reconsideration to the SHO
    #S/he needs to follow the same process-> either mark is_approved_aig as True
    #Or s/he must mark is_reconsider_aig=True and is_actiontaken=False
    form_class=Reconsider_AIG
    template_name='myportfolio/reconsider.html'
    queryset=Message.objects.all()

    def get_object(self):
        complaint_id=self.kwargs.get('id')
        print(complaint_id)
        mess=Message.objects.get(complaint_id=complaint_id)
        print(mess.from_user)
        mess.to_user=mess.from_user
        mess.from_user=self.request.user
        print(mess.to_user)
        print(mess.from_user)
        mess.release_date=datetime.now()
        mess.description=mess.description
        mess.is_archived=mess.is_archived
        mess.save()
        return get_object_or_404(Message,complaint_id=complaint_id)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        return redirect ('dgpoffice')

class Retakeaction(UpdateView):
    #here sho retakes the action. updates the form by taking the action.note that this is after aig as sent for reconsideration, hence this is update view
    form_class=Reconsider_SHO
    template_name='myportfolio/reconsideredmessage.html'
    queryset=Message.objects.all()

    def get_object(self):
        complaint_id=self.kwargs.get('id')
        print(complaint_id)
        mess=Message.objects.get(complaint_id=complaint_id)
        mess.from_user=self.request.user
        print(mess.from_user)
        mess.release_date=datetime.now()
        mess.description=mess.description
        mess.is_archived=mess.is_archived
        mess.save()
        return get_object_or_404(Message,complaint_id=complaint_id)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        return redirect ('shooffice')



@method_decorator(login_required, name='dispatch')
class action_taken_dgp(ListView):
    #This has messages which have been approved by aig, action has been taken by the SHO and now it tis upto the DGP to approve it, send for reconsideration
    #Also is_approved_dgp must be false
    model=Message
    paginate_by=10
    context_object_name='messages'
    template_name='myportfolio/action_taken_dgp.html'


    def get_queryset(self):
        queryset = super(action_taken_dgp, self).get_queryset()
        queryset = queryset.filter(is_actiontaken=True,is_approved_dgp=False,is_approved_aig=True)
        return queryset




class ApproveMessage_AIG(UpdateView):
    #This is the update view for the AIG to update the form by approving or reconsidering the form
    #if s/he chooses to reconsider s/he must unmark action_taken.
    #Whichever fields we want to show or allow for updation are decided in the form class corresponding to ApproveInput_AIG
    #Basically we allow is_approved_aig, (is_reconsider_aig and is_actiontaken)
    form_class=ApproveInput_AIG
    template_name='myportfolio/approve_aig.html'
    queryset=Message.objects.all()

    def get_object(self):
        complaint_id=self.kwargs.get('id')
        print(complaint_id)
        mess=Message.objects.get(complaint_id=complaint_id)
        print(mess.from_user)
        mess.to_user=mess.from_user
        mess.from_user=self.request.user
        print(mess.to_user)
        print(mess.from_user)
        mess.release_date=datetime.now()
        mess.description=mess.description
        mess.is_archived=mess.is_archived

        mess.save()

        return get_object_or_404(Message,complaint_id=complaint_id)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        return redirect ('dgpoffice')

class ApproveMessage_DGP(UpdateView):
    #For The DGP, s/he can either approve it or send for reconsideration
    #Incase s/he approves it well and good, if s/he choosed to reconsider, make sure that you mark the action_taken as false and is_approved_aig as false
    #It is basically part of the update view protocol
    form_class=ApproveInput_DGP
    template_name='myportfolio/approve_dgp.html'
    queryset=Message.objects.all()

    def get_object(self):
        complaint_id=self.kwargs.get('id')
        print(complaint_id)
        mess=Message.objects.get(complaint_id=complaint_id)
        print(mess.from_user)
        mess.to_user=mess.from_user
        mess.from_user=self.request.user
        print(mess.to_user)
        print(mess.from_user)
        mess.release_date=datetime.now()
        mess.description=mess.description
        mess.is_archived=mess.is_archived
        if(mess.is_reconsider_dgp==True):
            mess.is_approved_aig=False
        mess.save()
        return get_object_or_404(Message,complaint_id=complaint_id)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        return redirect ('dgpoffice')



@method_decorator(login_required, name='dispatch')
class aiginbox(ListView):
    #When I talk about the inbox over here
    #we get access to the model, context_object_nam3
    #Note that inside template we can access the list using message_list
    model=Message
    paginate_by=10
    context_object_name='messages'
    template_name='myportfolio/aiginbox.html'


    def get_queryset(self):
        queryset = super(aiginbox, self).get_queryset()
        #The inbox has all the objects in whish the SHO has not taken action (is_actiontaken=False), it has not been sent to him, The AIG hasnot aproved it yet(is_approved_aig=False),
        #If the dgp is sending it for the first time (not for the purpose of reconsideration), then it will be present in the inbox.
        #If it is sent for reconsideration, it will be present in the reconsider part\
        #So is_reconsider_dgp=FALSE
        #This is what we have to pass
        #Note that is_actiontaken will also be false when DGP has sent for reconsideration, hence over here ,we have an additional check of is_reconsider_dgp=False
        queryset = queryset.filter(to_user=self.request.user,is_archived=False,is_actiontaken=False,is_approved_aig=False,is_reconsider_dgp=False)
        return queryset


@method_decorator(login_required, name='dispatch')
class shoinbox(ListView):
    #This considers the messages which have been sent by the AIG in the first go, The SHO takes the required action
    model=Message
    paginate_by=10
    context_object_name='messages'
    template_name='myportfolio/shoinbox.html'


    def get_queryset(self):
        queryset = super(shoinbox, self).get_queryset()
        queryset = queryset.filter(to_user=self.request.user,is_actiontaken=False,is_reconsider_aig=False)
        return queryset


class TakeAction(UpdateView):
    #This is where The sho TAKES THE ACTION.
    #He writes his action taken and marks is_actiontaken as true
    form_class=MessageInput_SHO
    template_name='myportfolio/reply.html'
    queryset=Message.objects.all()

    def get_object(self):
        complaint_id=self.kwargs.get('id')
        print(complaint_id)
        mess=Message.objects.get(complaint_id=complaint_id)
        mess.from_user=self.request.user
        mess.save()
        return get_object_or_404(Message,complaint_id=complaint_id)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        return redirect ('shooffice')


class ForwardMessageAIG(UpdateView):
    #Basically we are forwarding, so whatever the DGP has sent to the AIG, if he wants to further forward it to the SHO
    #He can simply update the form that had been sent by the DGP,
    #So basicallly update form would show the existing values of the form but at the same time, it would allow us to update all the fields
    #So whichever fields  I donot want to update, I mark them as disable in the forms.py form class.
    form_class=MessageInput_AIG
    template_name='myportfolio/forward_aig.html'
    queryset=Message.objects.all()

#getobect returns the object of the model in which we have to make changes, which is precisely based on the 'id' of the complainant
#self.kwargs.get('id') helps us extract the id from the url-> The url in this case is of the form /id/update_aig
#id can also be extracted if we had used dynamic url and then passed id as an argument in the function view
#So whatever is the current value of the field will be displayed
    def get_object(self):
        complaint_id=self.kwargs.get('id')
        return get_object_or_404(Message,complaint_id=complaint_id)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        return redirect ('aigoffice')



class ReplyMessage(UpdateView):
    form_class=MessageInp
    template_name='myportfolio/reply.html'
    queryset=Message.objects.all()


    def get_object(self):
        id=self.kwargs.get("id")
        print(id)
        mess=Message.objects.get(id=id)
        a=mess.to_user
        mess.to_user=mess.from_user
        mess.from_user=a
        mess.release_date=datetime.now()
        mess.description=mess.description
        mess.save()
        print(mess.from_user)
        print(mess.to_user)
        return get_object_or_404(Message, id=id)


    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    #specify the model
    model = Message
    success_url = reverse_lazy('mess:dgpoffice')



class UserViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = User.objects.all()
    serializer_class = ToUserSerializer
