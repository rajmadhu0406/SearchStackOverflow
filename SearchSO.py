import shlex
import requests
import re
from subprocess import Popen, PIPE
import webbrowser
import os


class SO:
    def __init__(self):
        self.findSolution('TypeError','python')

    # function to run system command, here 'python file.py'
    def execute_and_return(cmd):
        args = shlex.split(cmd)
        # print('args :  ',args, '\n\n')
        proc = Popen(args, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        return out, err

    # function to call the StackOverflow API and return the JSON response
    def make_request(error, lang='python'):
        print("SearchSO > Searching for ===>  " + error)
        response = requests.get(
            "https://api.stackexchange.com/" + "2.2/search?order=desc&tagged={}&sort=activity&intitle={}&site=stackoverflow".format(
                lang, error))
        return response.json()

    # function to open solution link from json objects from API
    def get_urls(json):
        url_list = []
        count = 0
        for i in json['items']:
            if i["is_answered"]:
                url_list.append(i["link"])
            count += 1
            if count == len(i) or count == 5:
                break
        if count == 0:
            for i in json['items']:
                url_list.append(i["link"])
                count += 1
                if count == len(i) or count == 5:
                    break
        for i in url_list:
            webbrowser.open(i)

    # if __name__ == '__main__':

    # function to convert error from binary to utf-8 and making the url request and API calls using the above functions
    def run(filename):
        out, err = execute_and_return('python ' + filename)
        error = err.decode("utf-8").strip().split("\r\n")[-1]
        error.strip()
        if error:  # if(error == ''):
            filter_error = re.split("\n", error)  # error.split(":,\n")
            # print('filter_error: \n', filter_error, '\n--filter_error\n')
            # print('filter_error[0]: \n', filter_error[1], '\n--filter_error[0]\n')
            extra = filter_error[-1].split(':')
            for s in extra:
                get_urls(make_request(s))
            json1 = make_request(filter_error[-1])
            json2 = make_request(filter_error[-2])
            json3 = make_request(error)
            json4 = make_request(filter_error[0])
            get_urls(json1)
            get_urls(json2)
            get_urls(json3)
            get_urls(json4)
        else:
            print("SearchSO: No errors :)")

    # function to get the name of the file it is called in and check for solutions
    def check():
        filename = os.path.basename(__file__)
        filename = str(filename)
        filename.strip()
        # print('--' + filename + '--')
        run(filename)

    # check() for searching a error directly using a string as parameter
    def check(error):
        request = make_request(error)
        get_urls(request)

    def findSolution(question, lang):
        response = make_request(question, lang)
        get_urls(response)


obj = SO()

