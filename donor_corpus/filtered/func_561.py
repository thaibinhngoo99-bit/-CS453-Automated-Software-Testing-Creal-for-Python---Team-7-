def newthreadmake(request):
    t = ForumThread(thread_title=request.POST['threadname'])
    t.save()
    message_html = markdown(request.POST['message'], safe_mode='escape')
    t.forumpost_set.create(poster=request.POST['name'], message_body=message_html, date_posted=django.utils.timezone.now())
    return HttpResponseRedirect(reverse('bfstpw-thread', args=(t.id,)))