def thread(request, thread_id, message=''):
    current_thread = get_object_or_404(ForumThread, id=thread_id)
    max_posts_per_page = getattr(settings, 'BFSTPW_MAX_POSTS_PER_PAGE', 20)
    paginator = Paginator(current_thread.forumpost_set.order_by('date_posted'), max_posts_per_page)
    c = Context({'threadlist': [{'id': t.id, 'name': t.thread_title} for t in ForumThread.objects.sortByLastPost()], 'thread': current_thread, 'posts': paginator.page(request.GET.get('page', 1)), 'pages': paginator.page_range, 'message': message})
    return render(request, 'bfstpw/thread.html', c)