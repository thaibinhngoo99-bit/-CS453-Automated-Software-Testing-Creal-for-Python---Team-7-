@pytest.mark.django_db
def test_segment_delete_view_delete_instance(rf, segmented_page, user):
    user.is_superuser = True
    user.save()
    segment = segmented_page.personalisation_metadata.segment
    canonical_page = segmented_page.personalisation_metadata.canonical_page
    variants_metadata = segment.get_used_pages()
    page_variants = Page.objects.filter(pk__in=variants_metadata.values_list('variant_id', flat=True))
    assert canonical_page
    assert page_variants
    assert variants_metadata
    request = rf.get('/'.format(segment.pk))
    request.user = user
    view = SegmentModelDeleteView(instance_pk=str(segment.pk), model_admin=SegmentModelAdmin())
    view.request = request
    view.delete_instance()
    with pytest.raises(segment.DoesNotExist):
        segment.refresh_from_db()
    canonical_page.refresh_from_db()
    assert not page_variants.all()
    assert not variants_metadata.all()