import requests


class RequestHandler:

    def get(self, url, headers=None):
        try:
            result = requests.get(url=url, headers=headers)
            result.raise_for_status()
        except Exception as e:
            print("ERROR " + str(e.response.status_code))

        return result
