global global_x


def setup_module(self):
    print("this is setup_module")


def teardown_module(self):
    print("this is teardown_module")


class TestFixture:
    # a = None

    def setup(self):
        print("this is setup")

    def teardown(self):
        print("this is teardown")

    def setup_class(self):
        print("this is setup_class")

    def teardown_class(self):
        print("this is teardown_class")

    def test_001(self):
        print("test001")

    def test_002(self):
        print("test002")
