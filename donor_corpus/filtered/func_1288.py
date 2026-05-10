@pytest.mark.django_db
def test_segment_delete_view_raises_permission_denied(rf, segmented_page, user):
    segment = segmented_page.personalisation_metadata.segment
    request = rf.get('/'.format(segment.pk))
    request.user = user
    view = SegmentModelDeleteView(instance_pk=str(segment.pk), model_admin=SegmentModelAdmin())
    view.request = request
    message = 'User have no permission to delete variant page objects.'
    with pytest.raises(PermissionDenied):
        view.delete_instance()