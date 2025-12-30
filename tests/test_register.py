from tests.endpoints.Register import Register

def test_register_new_user(user):
    # This test registers a new user.
    registration = Register()
    result = registration.create_user(user)

    assert "Current user deleted" in result