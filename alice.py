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
    stops = get_stops(req)
    if not stops:
        res['response']['text'] = f'Я не поняла, повторите ещё раз.'
    elif len(stops) == 1:
        res['response']['text'] = 'Отлично! Теперь введите конечную остановку.'
    elif len(stops) == 2:
        start_stop = stops[0]
        final_stop = stops[1]
        # distance = get_distance(get_geo_info(cities[0], 'coordinates'), get_geo_info(cities[1], 'coordinates'))
        res['response']['text'] = f'Я готова построить маршрут от остановки "{start_stop}" до остановки "{final_stop}"'
    #     res['response']['text'] = 'Расстояние между этими городами: ' + str(round(distance)) + ' км.'
    # else:
    #     res['response']['text'] = 'Слишком много городов!'


def get_stops(req):
    stops = []
    stop = req['request']['original_utterance']
    stops.append(stop)
    return stops


if __name__ == '__main__':
    app.run()
