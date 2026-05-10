def test_call():
    quality_lower = 50
    quality_upper = 100
    tgt_jpeg = Tfda.JpegCompression(quality_lower=quality_lower, quality_upper=quality_upper, p=1.0)
    tgt_transform = test_utils.make_tgt_transform(tgt_jpeg)
    image = test_utils.make_test_image()
    tgt_result = tgt_transform(image=image)
    actual_image = tgt_result['image']
    image_np = image.numpy()
    quality = float(tgt_jpeg.get_param('quality'))
    expected_image = A.image_compression(image_np, quality, image_type='.jpg')
    test_utils.partial_assert_array(expected_image, actual_image, 0.6, 'image', eps=0.1)