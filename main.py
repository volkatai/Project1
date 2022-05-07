from flask import Flask, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


def find_out_starting_point(user_id, req, res):
    pass


def find_out_destination(user_id, req, res):
    pass


def offer_route(user_id, req, res):
    pass


states = {
    1: find_out_starting_point,
    2: find_out_destination,
    3: offer_route
}
session_state = {}


@app.route('/post', methods=['POST'])
def main():
    #     logging.info(f'Request: {request.json!r}')
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    handle_dialog(response, request.json)
    #     logging.info(f'Response: {response!r}')
    return json.dumps(response)


#
#
def handle_dialog(res, req):
    user_id = req['session']['user_id']
    #
    # если пользователь новый, то просим его представиться.
    if req['session']['new']:
        res['response']['text'] = 'Привет! Назови свое имя!'
        # создаем словарь в который в будущем положим имя пользователя
        sessionStorage[user_id] = {
            'first_name': None
        }
        return


#
#     # если пользователь не новый, то попадаем сюда.
#     # если поле имени пустое, то это говорит о том,
#     # что пользователь еще не представился.
#     if sessionStorage[user_id]['first_name'] is None:
#         # в последнем его сообщение ищем имя.
#         first_name = get_first_name(req)
#         # если не нашли, то сообщаем пользователю что не расслышали.
#         if first_name is None:
#             res['response']['text'] = \
#                 'Не расслышала имя. Повтори, пожалуйста!'
#         # если нашли, то приветствуем пользователя.
#         # И спрашиваем какой город он хочет увидеть.
#         else:
#             sessionStorage[user_id]['first_name'] = first_name
#             res['response'][
#                 'text'] = 'Приятно познакомиться, ' \
#                           + first_name.title() \
#                           + '. Я - Алиса. Какой город хочешь увидеть?'
#             # получаем варианты buttons из ключей нашего словаря cities
#             res['response']['buttons'] = [
#                 {
#                     'title': city.title(),
#                     'hide': True
#                 } for city in cities
#             ]
#     # если мы знакомы с пользователем и он нам что-то написал,
#     # то это говорит о том, что он уже говорит о городе,
#     # что хочет увидеть.
#     else:
#         # ищем город в сообщение от пользователя
#         city = get_city(req)
#         # если этот город среди известных нам,
#         # то показываем его (выбираем одну из двух картинок случайно)
#         if city in cities:
#             res['response']['card'] = {}
#             res['response']['card']['type'] = 'BigImage'
#             res['response']['card']['title'] = 'Этот город я знаю.'
#             res['response']['card']['image_id'] = random.choice(cities[city])
#             res['response']['text'] = 'Я угадал!'
#         # если не нашел, то отвечает пользователю
#         # 'Первый раз слышу об этом городе.'
#         else:
#             res['response']['text'] = \
#                 'Первый раз слышу об этом городе. Попробуй еще разок!'
#
#
# def get_city(req):
#     # перебираем именованные сущности
#     for entity in req['request']['nlu']['entities']:
#         # если тип YANDEX.GEO то пытаемся получить город(city),
#         # если нет, то возвращаем None
#         if entity['type'] == 'YANDEX.GEO':
#             # возвращаем None, если не нашли сущности с типом YANDEX.GEO
#             return entity['value'].get('city', None)
#
#
# def get_first_name(req):
#     # перебираем сущности
#     for entity in req['request']['nlu']['entities']:
#         # находим сущность с типом 'YANDEX.FIO'
#         if entity['type'] == 'YANDEX.FIO':
#             # Если есть сущность с ключом 'first_name',
#             # то возвращаем ее значение.
#             # Во всех остальных случаях возвращаем None.
#             return entity['value'].get('first_name', None)
#
#
if __name__ == '__main__':
    app.run()
