from bfstpw.models import ForumThread, ForumPost
from datetime import datetime
from django.conf import settings
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context
import django.utils.timezone
from markdown import markdown

def threadlist(request):
    c = Context({"threadlist" :
        [{"id":t.id
         ,"name":t.thread_title
         ,"poster":t.getOriginalPost().poster
         ,"replycount":t.postcount
         ,"lastpage":(t.postcount / getattr(settings, 'BFSTPW_MAX_POSTS_PER_PAGE', 20))+1
         ,"date":t.mostrecent
         ,"lastposter":t.getLatestPost().poster
         } for t in
            ForumThread.objects.sortByLastPost().annotate(postcount=Count('forumpost'))]})

    return render(request, 'bfstpw/threadlist.html', c)

def thread(request, thread_id, message=''):
    current_thread = get_object_or_404(ForumThread, id=thread_id)
    max_posts_per_page = getattr(settings, 'BFSTPW_MAX_POSTS_PER_PAGE', 20)
    paginator = Paginator(current_thread.forumpost_set.order_by('date_posted'), max_posts_per_page)
    c = Context(
            {"threadlist" :
                [{"id":t.id
                 ,"name":t.thread_title
                 } for t in ForumThread.objects.sortByLastPost()],
             "thread" : current_thread,
             "posts" : paginator.page(request.GET.get('page',1)),
             "pages" : paginator.page_range,
             "message" : message
            })
           
    return render(request, 'bfstpw/thread.html', c)

def post(request, thread_id):
    t = get_object_or_404(ForumThread, id=thread_id)

    posts = t.forumpost_set
    """
    # TODO: don't let users post too quickly
    session = request.session
    current_time = time()
    if (session.get('lastposttime',0) + 10) < current_time:
        message_html = markdown(request.POST['message'], safe_mode='escape')
        posts.create(poster=request.POST['name'],message_body=message_html,date_posted=datetime.now())

        msg = ''

        session['lastposttime'] = current_time
    else:
        msg = "Error: you must wait 10 seconds before posting"
    """
    message_html = markdown(request.POST['message'], safe_mode='escape')
    posts.create(poster=request.POST['name'], message_body=message_html,
            date_posted=django.utils.timezone.now())
    pagenum = (posts.count() / getattr(settings, 'BFSTPW_MAX_POSTS_PER_PAGE', 20))+1
    return HttpResponseRedirect(reverse('bfstpw-thread', args=(t.id,))+'?page=%d' % pagenum)

def newthreadmake(request):
    t = ForumThread(thread_title=request.POST['threadname'])
    t.save()
    message_html = markdown(request.POST['message'], safe_mode='escape')
    t.forumpost_set.create(poster=request.POST['name'],
            message_body=message_html,
            date_posted=django.utils.timezone.now())

    return HttpResponseRedirect(reverse('bfstpw-thread', args=(t.id,)))
