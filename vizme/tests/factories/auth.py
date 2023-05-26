import factory
from async_factory_boy.factory.sqlalchemy import AsyncSQLAlchemyFactory
from faker import Factory as FakerFactory
from pytest_factoryboy import register

from vizme.app.auth.models import User
from vizme.auth.hash import get_password_hash
from vizme.tests.utils import sc_session

faker = FakerFactory.create()


@register
class UserFactory(AsyncSQLAlchemyFactory):
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    email = factory.LazyAttribute(lambda x: faker.email())
    picture_url = "https://goo.su/nnbA0Me"
    hashed_password = factory.LazyAttribute(lambda x: get_password_hash("password"))

    class Meta:
        model = User
        sqlalchemy_session = sc_session
