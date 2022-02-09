import pytest
from django.contrib.auth.models import User
from django.contrib.auth.models import User

# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")
# @pytest.mark.django_db
# def test_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True
#     count = User.objects.all().count()
#     print(count)



# # def test_username(user_1):
# #     assert user_1.username=="test-user"
# # def test_username1(user_1):
# #     assert user_1.username == "test-user"

# def test_new_user(new_user):
#     print('checking')
#     assert new_user.username == "Test_User"

# def test_staff(staff_user):
#     print('check staff')
#     assert staff_user.is_staff == True

# @pytest.mark.django_db
# def test_new_user(user_factory):
#     user = user_factory.create()
#     count = User.objects.all().count()
#     print(user.username,count)
#     assert count==1

# @pytest.mark.django_db
# def test_new_user(new_user1):
#     print(new_user1.username)
#     count = User.objects.all().count()
#     assert count==1

def test_product(db,product_factory):
    product = product_factory.create()
    print(product.description)
    assert True 