import requests

api_key = "5ee7cd5080fec3eded157d8010b377f6"  # API key를 입력하세요.

def getMovieList():
    datas = []
    sizePerPage = 100
    for i in range(2):
        url = "http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key="+ api_key +"&itemPerPage=" + str(sizePerPage) + "&curPage=" + str(i)  + '&repNationCd=22041011'# API 요청 URL을 입력하세요.
        response = requests.get(url) # GET 요청을 보내고 응답 객체를 받아옵니다.

        try:
            data = response.json() # JSON 형태로 받아온 응답 데이터를 파싱합니다.
            # 결과 확인
            print(data)
            for movie in data['movieListResult']['movieList']:
                datas.append(movie['movieCd'])

        except ValueError as e:
            print('Error:', e)

    return datas

def getGraph(movieCdList):
    datas = {}
    for movieCd in movieCdList:
        url = "http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=" + api_key + "&movieCd=" + str(movieCd)  # API 요청 URL을 입력하세요.

        response = requests.get(url)  # GET 요청을 보내고 응답 객체를 받아옵니다.

        try:
            data = response.json() # JSON 형태로 받아온 응답 데이터를 파싱합니다.
            # 결과 확인
            print(data)
            movieName = "영화 "+data['movieInfoResult']['movieInfo']['movieNm']
            if len(data['movieInfoResult']['movieInfo']['actors']) != 0:
                datas[movieName] = []
                for actor in data['movieInfoResult']['movieInfo']['actors']:
                    actorName = "배우 "+ actor['peopleNm']
                    datas[movieName].append(actorName)
                    if actorName in datas:
                        datas[actorName].append(movieName)
                    else:
                        datas[actorName] = [movieName]
        except ValueError as e:
            print('Error:', e)
    return datas