def create_text_date_annotations():
    """Annotate dates in a clinical note

    Return the date annotations found in a clinical note # noqa: E501

    :rtype: TextDateAnnotations
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            annotation_request = TextDateAnnotationRequest.from_dict(connexion.request.get_json())
            note = annotation_request.note
            annotations = get_annotations(note, phi_type=PhiType.DATE)
            res = TextDateAnnotationResponse(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error('Internal error', status, str(error))
    return (res, status)