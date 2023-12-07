import requests


def calculate_http_traffic(url):
    # Make the request
    response = requests.get(url)

    # Calculate request size
    # Request headers size + actual request content size
    request_size = len(response.request.headers) + len(response.request.body or b'')

    # Calculate response size
    # Response headers size + actual response content size
    response_size = len(response.headers) + len(response.content)

    # Total traffic
    total_size = request_size + response_size

    return {
        'request_size': request_size,
        'response_size': response_size,
        'total_size': total_size
    }


if __name__ == "__main__":
    url = 'https://youtube.com/channel/UCzL89vFZhDsk9IERAVrrCzg'
    traffic = calculate_http_traffic(url)
    print(f"Request Size: {traffic['request_size']} bytes")
    print(f"Response Size: {traffic['response_size']} bytes")
    print(f"Total Traffic: {traffic['total_size']} bytes or {round(traffic['total_size']/1024, 2)}kb")