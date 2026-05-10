def test_all_same():
    assert all_same([9, 1, 2, 3, 4]) == False
    assert all_same([[], [], []])
    assert all_same([])
    assert all_same([ColumnRecommendation(0, ColumnClassification.WIN), ColumnRecommendation(2, ColumnClassification.WIN)])
    assert all_same([ColumnRecommendation(0, ColumnClassification.MAYBE), ColumnRecommendation(0, ColumnClassification.WIN)]) == False