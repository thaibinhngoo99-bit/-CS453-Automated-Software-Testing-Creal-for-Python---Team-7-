@pytest.mark.django_db
def test_segment_user_data_view_requires_admin_access(site, client, django_user_model):
    user = django_user_model.objects.create(username='first')
    segment = Segment(type=Segment.TYPE_STATIC, count=1)
    segment.save()
    client.force_login(user)
    url = reverse('segment:segment_user_data', args=(segment.id,))
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == '/admin/login/?next=%s' % url