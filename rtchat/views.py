from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

login_required
def chat_view(request):
    chat_group=get_object_or_404(ChatGroup,group_name='public-chats')
    chat_messages=chat_group.chat_messages.all()[:30]
    form=ChatMessagesCreateForm()
    if request.htmx:
        form=ChatMessagesCreateForm(request.POST)
        if form.is_valid:
            message=form.save(commit=False)
            message.author=request.user
            message.group=chat_group
            message.save()
            context={'user':request.user,
                     'message':message}
            return render(request,'rtchat/partials/chat_messages_p.html',context)

    return render(request,'rtchat/chat.html',{'chat_messages':chat_messages,'form':form})