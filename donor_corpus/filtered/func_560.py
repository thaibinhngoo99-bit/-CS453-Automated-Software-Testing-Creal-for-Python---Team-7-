def post(request, thread_id):
    t = get_object_or_404(ForumThread, id=thread_id)
    posts = t.forumpost_set
    '\n    # TODO: don\'t let users post too quickly\n    session = request.session\n    current_time = time()\n    if (session.get(\'lastposttime\',0) + 10) < current_time:\n        message_html = markdown(request.POST[\'message\'], safe_mode=\'escape\')\n        posts.create(poster=request.POST[\'name\'],message_body=message_html,date_posted=datetime.now())\n\n        msg = \'\'\n\n        session[\'lastposttime\'] = current_time\n    else:\n        msg = "Error: you must wait 10 seconds before posting"\n    '
    message_html = markdown(request.POST['message'], safe_mode='escape')
    posts.create(poster=request.POST['name'], message_body=message_html, date_posted=django.utils.timezone.now())
    pagenum = posts.count() / getattr(settings, 'BFSTPW_MAX_POSTS_PER_PAGE', 20) + 1
    return HttpResponseRedirect(reverse('bfstpw-thread', args=(t.id,)) + '?page=%d' % pagenum)