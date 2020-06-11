def aceleradev_middleware(get_response):

    def middleware(request):
        if request.method == 'GET':
            print('Got a GET method')
        print('==================')
        print('>>>>>> Acelera Dev')
        response = get_response(request)
        print('Online na codenation')
        return response
    
    return middleware