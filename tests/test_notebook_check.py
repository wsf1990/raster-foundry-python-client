def test_warn_without_notebook_support():
    import rasterfoundry.decorators
    rasterfoundry.decorators.NOTEBOOK_SUPPORT = False
    from rasterfoundry.decorators import check_notebook

    @check_notebook
    def f():
        return 'foo'
    assert f() is None


def test_no_warn_with_notebook_support():
    import rasterfoundry.decorators
    rasterfoundry.decorators.NOTEBOOK_SUPPORT = True
    from rasterfoundry.decorators import check_notebook

    @check_notebook
    def f():
        return 'foo'
    assert f() == 'foo'
