import os
#pytest requires functions to start running

def test_development_config(test_app):
    test_app.config.from_object('src.config.DevelopmentConfig')
    assert test_app.config['SECRET_KEY'] == 'my_precious'
    assert not test_app.config['TESTING']
    assert test_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_URL')


def test_testing_config(test_app):
    def test_production_config(test_app):
        test_app.config.from_object("src.config.ProductionConfig")
        assert test_app.config["SECRET_KEY"] == os.getenv("SECRET_KEY", "my_precious")  # updated
        assert not test_app.config["TESTING"]
        assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")


def test_production_config(test_app):
    test_app.config.from_object('src.config.ProductionConfig')
    assert test_app.config['SECRET_KEY'] == 'my_precious'
    assert not test_app.config['TESTING']
    assert test_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_URL')