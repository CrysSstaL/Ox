import requests

url = 'https://httpbin.org'

def GET(url): # GET
    file = open('get.txt' ,'w')
    response = requests.get(url)
    # Получаем информацию о сайте
    file.write(str(response.request.headers)+'\n')
    file.write(response.text)
    file.close()

def POST(url):  # POST
    file = open('post.txt' ,'w')
    # Создаем response c json обьектом
    response = requests.post(url + '/post', json={'teacher1': ('student1','student2'), 'teacher2': 'student3'})
    file.write(response.text)
    file.close()

def OPTIONS(url): #OPTIONS
    file = open('options.txt' ,'w')
    response = requests.options(url)
    text_response = str(response.headers)
    file.write(str(response) + '\n')
    file.write(text_response + '\n') #Все заголовки
    file.write('Date - ' + response.headers.get('Date') + '\n')  # Получаем дату
    file.write('Access-Control-Allow-Methods - ' + response.headers.get('Access-Control-Allow-Methods') + '\n')
    file.close()
    pass

if __name__ == '__main__':
    GET(url)
    POST(url)
    OPTIONS(url)