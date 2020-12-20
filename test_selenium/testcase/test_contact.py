from test_selenium.page.contact import Contact


class TestContact:
    def test_add_user(self):
        contact=Contact(reuse=True)
        contact.add_member()
