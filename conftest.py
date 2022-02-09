import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory,CategoryFactory,ProductFactory

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)


@pytest.fixture
def new_user1(db,user_factory):
    user = user_factory.create()
    return user



# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user("test-user")
#     print('user created')
#     return user

# @pytest.fixture
# def new_user_factory():
#     def create_app_user(
#         username:str,
#         password:str = None,
#         first_name:str = "firstname",
#         last_name:str = "lastname",
#         email:str ="test@test.com",
#         is_staff: str = False,
#         is_superuser:str = False,
#         is_active: str = True
#     ):
#         user = User.objects.create_user(username=username,
#             password=password,
#             first_name = first_name,
#             last_name=last_name,
#             email=email,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             is_active=is_active
#             )
#         return user

#     return create_app_user

# @pytest.fixture
# def new_user(db,new_user_factory):
#     return new_user_factory("Test_User","password","Name")

# @pytest.fixture
# def staff_user(db,new_user_factory):
#     return new_user_factory("Staff","password","Staffy",is_staff=True)



