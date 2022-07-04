# from django.shortcuts import render

# # Create your views here.
# def landing(request):
#     from datetime import datetime

#     context = {
#         "weather": "비",
#         "temperature": 29,
#         "weather_data": {
#             "weather": "맑음",
#             "temperature": 32,
#         },
#         "top_average": [
#             "이정후", "강백호", "전준우", "A", "B"
#         ],
#         "top_hitters": [
#             {
#                 "name": "이정후",
#                 "average": "0.350",
#             },
#             {
#                 "name": "강백호",
#                 "average": "0.349",
#             },
#             {
#                 "name": "전준우",
#                 "average": "0.348",
#             },
#         ],
#         "now": datetime.now()
#     }

#     current_datetime = datetime.now()
#     print(current_datetime.year)
#     print(current_datetime.month)
#     print(current_datetime.day)

    # current_datetime_str = 
    # current_datetime_str = f"{current_datetime.year}-{current_datetime.month}-{current_datetime.day}"

    # context = {

    #     "weather_data":[
    #         {
    #             "weather":"더움",
    #             "temperature":40,
    #         }
    #     ]
    # }

    # context_dict = {
    #     "weather":"맑음",
    #     "temperature":32,
    # }
    # context["weather_data"] = context_dict
    # # print(context)

    # context_list = [
    #     "강남규", "강백호", "전준우",
    # ]
    # context["top_average"] = context_list
    # # context["top_average"][0]

    # context_object = [
    #     {
    #         "name":"강남규",
    #         "average":"0.355",
    #     },
    #     {
    #         "name":"강백호",
    #         "average":"0.349",
    #     },
    #     {
    #         "name":"전준우",
    #         "average":"0.348",
    #     },
    # ]
    # context["top_hitters"] = context_object
    
    # context = {
    #     "status":"pending"
    # }
    
    # # API 통신 한다.
    # is_success = True
    # if is_success:
    #     context["data"] = {}
    # else:   
    #     context["message"] = {}


    # print(f"오늘의 날씨는 {context['weather_data'][0]['weather']}이며, 기온은 {context['weather_data'][0]['temperature']}")
    # return render(request, "landing/index.html", context)

from django.shortcuts import render


def landing(request):
    from datetime import datetime

    context = {
        "weather": "비",
        "temperature": 29,
        "weather_data": {
            "weather": "맑음",
            "temperature": 32,
        },
        "top_average": [
            "이정후", "강백호", "전준우", "A", "B"
        ],
        "top_hitters": [
            {
                "name": "이정후",
                "average": "0.350",
            },
            {
                "name": "강백호",
                "average": "0.349",
            },
            {
                "name": "전준우",
                "average": "0.348",
            },
        ],
        "now": datetime.now()
    }
    current_datetime = datetime.now()
    current_datetime_str = f"{current_datetime.year}-{current_datetime.month}-{current_datetime.day}"

    context["now"] = current_datetime_str
    return render(request, "landing/index.html", context)