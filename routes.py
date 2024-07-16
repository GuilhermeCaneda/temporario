from flask import Blueprint

from queries import find_by_cpf, find_by_name, find_by_similar_name, find_by_razao, find_by_similar_razao, find_by_name_cpf

routes = Blueprint('routes', __name__)

routes.add_url_rule('/cpf', view_func=find_by_cpf, methods=['GET'])
routes.add_url_rule('/name', view_func=find_by_name, methods=['GET'])
routes.add_url_rule('/similar_name', view_func=find_by_similar_name, methods=['GET'])
routes.add_url_rule('/razao', view_func=find_by_razao, methods=['GET'])
routes.add_url_rule('/similar_razao', view_func=find_by_similar_razao, methods=['GET'])
routes.add_url_rule('/name_cpf', view_func=find_by_name_cpf, methods=['GET'])
