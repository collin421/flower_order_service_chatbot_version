from flask import Flask
from .products import products_blueprint
from .branches import branches_blueprint
from .orders import order_blueprint
from .order_view import order_view_blueprint
from .all_orders import all_orders_blueprint
from .chatbot import chatbot_bp

# from .orders import orders_blueprint
# 필요에 따라 추가 블루프린트 임포트

def register_blueprints(app):
    app.register_blueprint(products_blueprint)
    app.register_blueprint(branches_blueprint)
    app.register_blueprint(order_blueprint)
    app.register_blueprint(order_view_blueprint)
    app.register_blueprint(all_orders_blueprint)
    app.register_blueprint(chatbot_bp)
    # app.register_blueprint(orders_blueprint)
    # 추가된 블루프린트 등록