from bottle import post, request, run
import requests
from os import environ

@post('/')
def sendToCrucible():
    crucibleKey, project = request.headers['X-Gitlab-Token'].split(';')

    baseUrl = environ.get('CRUCIBLE_BASE_URL')
    url = '{0}/rest-service-fecru/admin/repositories/{1}/incremental-index'.format(baseUrl, project)
    headers = { 'X-Api-Key': crucibleKey, 'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers)

    # print("status: {0}".format(response.status_code))
    # print("headers: {0}".format(response.headers))
    # print("text: {0}".format(response.text))


if __name__ == "__main__":
    run(host='localhost', reloader=True, port=5000)
