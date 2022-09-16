import requests


class RequestHandler:

    def get(self, url, headers=None):
        try:
            result = requests.get(url=url, headers=headers)
            result.raise_for_status()
            return True, result

        except Exception as e:
            result = " ".join(["ERROR", str(e.response.status_code), str(e.response.url), str(e.response.reason)])
            return False, result
