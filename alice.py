from flask import Flask, request
import logging
import json
# импортируем функции из нашего второго файла geo
# from geo import get_geo_info, get_distance

app = Flask(__name__)

# Добавляем логирование в файл. Чтобы найти файл,
# перейдите на pythonwhere в раздел files, он лежит в корневой папке
# logging.basicConfig(level=logging.INFO, filename='app.log',
#                     format='%(asctime)s %(levelname)s %(name)s %(message)s')


@app.route('/post', methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info('Request: %r', response)
    return json.dumps(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']
    if req['session']['new']:
        res['response']['text'] = 'Привет! Я подскажу тебе на каком автобусе добраться до нужного места!'
        res['response']['text'] = 'Введи начальную остановку.'
        return
    # Получаем города из нашего
    # stops = [get_start_stops(req), get_final_stops(req)]
    start_stop = get_start_stops(req)
    # if not stops:
    #     res['response']['text'] = f'Я не поняла, повторите ещё раз.'
    if start_stop:
        res['response']['text'] = 'Отлично! Теперь введите конечную остановку.'
    final_stop = get_final_stops(req)
    if final_stop:
        # distance = get_distance(get_geo_info(cities[0], 'coordinates'), get_geo_info(cities[1], 'coordinates'))
        res['response']['text'] = f'Я готова построить маршрут от остановки "{start_stop}" до остановки "{final_stop}"'
    #     res['response']['text'] = 'Расстояние между этими городами: ' + str(round(distance)) + ' км.'
    # else:
    #     res['response']['text'] = 'Слишком много городов!'


def get_start_stops(req):
    start_stop = req['request']['original_utterance']
    return start_stop


def get_final_stops(req):
    final_stop = req['request']['original_utterance']
    return final_stop


if __name__ == '__main__':
    app.run()
