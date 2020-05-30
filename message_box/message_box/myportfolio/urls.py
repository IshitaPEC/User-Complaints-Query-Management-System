from django.contrib import admin
from django.urls import path
from myportfolio import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from myportfolio.views import UserViewSet


router = DefaultRouter()
router.register(r'user', UserViewSet)


app_name='mess'
urlpatterns= [
    path('',views.homepage,name=''),
    path('login/',views.login,name='login'),
    path('lodge_your_complaint',views.lodgeyourcomplaint,name='lodge_complaint'),
    path('action_status',views.ActionStatus,name='ss'),
    path('actionpending_aig',views.ActionPending_AIG.as_view(),name='actionpendingaig'),
    path('actionpending_dgp',views.ActionPending_DGP.as_view(),name='actionpendingdgp'),
    path('logout',views.userlogout,name='userlogout'),
    path('dgpinbox',views.dgpinbox.as_view(),name='dgpoffice'),
    path('aignbox',views.aiginbox.as_view(),name='aigoffice'),
    path('shonbox',views.shoinbox.as_view(),name='shooffice'),
    path('Action_taken_aig',views.action_taken_aig.as_view(),name='action_taken_aig'),
    path('Action_taken_dgp',views.action_taken_dgp.as_view(),name='action_taken_dgp'),
    path('Reconsider',views.reconsider_aig.as_view(),name='reconsider_aig'),
    path('ReconsiderSHO',views.reconsider_sho.as_view(),name='reconsider_sho'),
    path('<int:pk>',views.MessageDetail.as_view(),name='detail'),
    path('<int:pk>/aig',views.MessageDetail_aig.as_view(),name='detailing'),
    path('<int:id>/update/',views.ForwardMessage.as_view(),name='forwarded'),
    path('<int:id>/update_aig/',views.ForwardMessageAIG.as_view(),name='forwardedaig'),
    path('<int:id>/update_approve/aig',views.ApproveMessage_AIG.as_view(),name='approve_aig'),
    path('<int:id>/update_approve/dgp',views.ApproveMessage_DGP.as_view(),name='approve_dgp'),
    path('<int:id>/reply/',views.ReplyMessage.as_view(),name='reply'),
    path('delete/<int:pk>',views.MessageDeleteView.as_view(), name='message_delete'),
    path('archivedmess',views.ArchivedMessage.as_view(),name='ap'),
    path('<int:pk>/archive',views.Archived_MessageDetail.as_view(),name='arch_detail'),
    path('<int:id>/update_archive/',views.Archive.as_view(),name='archived'),
    path('<int:id>/take_Action/',views.TakeAction.as_view(),name='take_action'),
    path('<int:id>/update_reconsider/aig',views.Reconsider.as_view(),name='reconsider'),
    path('<int:id>/update_reconsider/sho',views.Retakeaction.as_view(),name='reconsider'),
    #path('<int:pk>',views.forwardedteacher.as_view(), name='pf')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
