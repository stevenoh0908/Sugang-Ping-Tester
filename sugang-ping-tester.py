###############################
#  Sugang Ping Tester v1.0.0  #
# --------------------------- #
# By dev.Coffee               #
# For more information,       #
# Please Contact Below:       #
# officialdevcoffee@gmail.com #
###############################

def split_time_information(reply_message):
    return reply_message.split()[4][5:][:-2]

import os, statistics

PING_TIME = 10
ping_time_list = []
failed_ping_count = 0

print("############################")
print("# 수강신청 핑 테스터 v1.0.0 #")
print("############################")
print("- By dev.Coffee (officialdevcoffee@gmail.com, https://stevenoh0908.kro.kr/dev)")
print("- 이 프로그램은 수강 신청 서버와 컴퓨터 사이의 PING 속도를 가장 정확하게 확인하는 프로그램입니다.")
print("- PING 속도는 컴퓨터가 수강 신청 서버에 요청을 보냈을 때 수강 신청 서버가 반응하기까지 걸리는 시간으로, PING 속도가 빠를수록, 즉 값이 작을수록 수강 신청에 성공할 확률이 높습니다.")
print("- PING과 관련한 보다 자세한 사항을 확인하시고 싶으시다면 Google 검색을 통해 확인하시기 바랍니다.")
print("")

url = input(">> 수강 신청 사이트 주소를 입력 (정확하게!): ")
ping_time_response = input(">> 확인할 횟수를 입력하세요 (자연수, 높을수록 시간이 오래 걸리지만 정확합니다. 엔터를 누르시면 기본값 10이 적용됩니다): ")

if ping_time_response.isnumeric():
    PING_TIME = int(ping_time_response)
    pass

print("")
print("- PING 속도 확인중 . . .")
print("- 조금만 기다리시면 PING 속도가 측정됩니다!")

result_string = os.popen("ping " + str(url) + " -n " + str(PING_TIME)).read()

for i in range(0, PING_TIME):
    if result_string.split('\n')[2+i][:5] == 'Reply':
        ping_time_list.append(int(split_time_information(result_string.split('\n')[2 + i])))
        pass
    else:
        failed_ping_count += 1
        pass
    pass

ping_average = statistics.mean(ping_time_list)
ping_max = max(ping_time_list)
ping_min = min(ping_time_list)
ping_stdev = statistics.stdev(ping_time_list)
ping_success_rate = (PING_TIME - failed_ping_count) / PING_TIME * 100 # % 단위

# PING 측정 결과 출력
print("")
print("- 측정이 완료되었습니다!")
print("")
print("[PING 측정결과]")
print(" -------------------------- ")
print("> 평균: %f ms" % (ping_average))
print("> 최소: %f ms" % (ping_min))
print("> 최대: %f ms" % (ping_max))
print("> 응답 성공 비율: %f %%" % (ping_success_rate))
print("")

# PING 측정 결과를 토대로 한 조언
print("[조언]")

# PING AVG 메세지
print("I. 전반적 PING 속도")
if ping_average <= 35:
    print("- 전반적으로 PING 속도가 좋은 편입니다. 측정 결과인 %f ms는 일반적인 성능의 네트워크 연결에서 안정적인 수준의 속도입니다." % (ping_average))
    pass
else:
    print("- 전반적으로 PING 속도가 좋은 편이 아닙니다. 측정 결과인 %f ms는 네트워크 연결에 문제가 있을 수 있다는 신호로 간주될 수 있습니다." % (ping_average))
    print("a) 네트워크 연결 상태를 확인하세요. 중간에 네트워크가 끊기는 것은 아닌가요?")
    print("b) 공유기 설정을 확인하세요. 공유기 설정이 잘못되어 있거나, 공유기가 다른 공유기들도 사용하는 채널을 사용하고 있어 전파 간섭이 일어나고 있지는 않나요?")
    print("c) 컴퓨터 프로그램 상태를 확인하세요. 컴퓨터에 다른 응용 프로그램, 백그라운드 실행 프로그램이 돌아가고 있는 것은 아닌가요?")
    print("d) 주변에 너무 많은 사람이 같은 네트워크에 접속하고 있지는 않은지 확인하세요. 너무 많은 사람이 같은 네트워크를 동시에 사용하면 당연히 느려질 수 밖에 없어요.")
    pass
print("")

# PING STDEV 메세지
print("II. PING 안정성")
if ping_stdev <= 15:
    print("- 전반적으로 PING 속도가 안정적인 편입니다. 이대로 수강 신청을 해도 괜찮을 것 같네요.")
    pass
elif ping_stdev <= 30:
    print("- PING 속도가 약간 불안정합니다. 설정이 제대로 되어 있는지 다음을 확인해보는 것은 어떨까요?")
    print("a) 공유기 설정을 확인하세요. 공유기가 다른 공유기들도 사용하는 채널을 사용하고 있어 전파 간섭이 일어나고 있지는 않나요?")
    print("b) 컴퓨터 프로그램 상태를 확인하세요. 컴퓨터에 다른 응용 프로그램, 백그라운드 실행 프로그램이 돌아가고 있는 것은 아닌가요?")
    print("c) 주변에 너무 많은 사람이 같은 네트워크에 접속하고 있지는 않은지 확인하세요. 너무 많은 사람이 같은 네트워크를 동시에 사용하면 당연히 느려질 수 밖에 없어요.")
    pass
else:
    print("- PING 속도가 매우 불안정합니다. 무언가가 잘못된 것 같으니, 빨리 설정을 확인해보세요.")
    print("a) 공유기 설정을 확인하세요. 공유기가 다른 공유기들도 사용하는 채널을 사용하고 있어 전파 간섭이 일어나고 있지는 않나요?")
    print("b) 컴퓨터 프로그램 상태를 확인하세요. 컴퓨터에 다른 응용 프로그램, 백그라운드 실행 프로그램이 돌아가고 있는 것은 아닌가요?")
    print("c) 주변에 너무 많은 사람이 같은 네트워크에 접속하고 있지는 않은지 확인하세요. 너무 많은 사람이 같은 네트워크를 동시에 사용하면 당연히 느려질 수 밖에 없어요.")
    pass
print("")

# PING MAX 메세지
print("III. PING이 튀는지의 여부")
if (ping_max - ping_average) <= 10:
    print("- PING이 중간에 튀지 않고 안정적입니다. 괜찮은 네트워크 상태라고 말씀드릴 수 있겠네요!")
    pass
else:
    print("- PING이 중간에 튀고 있습니다. 네트워크가 불안정하다는 신호이니, 다음을 확인해보세요.")
    print("a) 네트워크 연결 상태를 확인하세요. 중간에 네트워크가 끊기는 것은 아닌가요?")
    print("b) 공유기 설정을 확인하세요. 공유기 설정이 잘못되어 있거나, 공유기가 다른 공유기들도 사용하는 채널을 사용하고 있어 전파 간섭이 일어나고 있지는 않나요?")
    print("c) 컴퓨터 프로그램 상태를 확인하세요. 컴퓨터에 다른 응용 프로그램, 백그라운드 실행 프로그램이 돌아가고 있는 것은 아닌가요?")
    print("d) 주변에 너무 많은 사람이 같은 네트워크에 접속하고 있지는 않은지 확인하세요. 너무 많은 사람이 같은 네트워크를 동시에 사용하면 당연히 느려질 수 밖에 없어요.")
    pass
print("")

# PING SUCCESS RATE 메세지
print("IV. PING 성공률")
if int(ping_success_rate) == 100:
    print("- 모든 PING 요청이 성공적으로 되돌아왔습니다. 서버와의 연결이 안정적이라는 좋은 신호입니다.")
    pass
elif ping_success_rate > 80:
    print("- PING 요청 중 일부가 실패했습니다. 서버와의 연결이 불안정하다는 신호로, 주의가 필요합니다. 다음을 확인해보세요.")
    print("a) 네트워크 연결 상태를 확인하세요. 중간에 네트워크가 끊기는 것은 아닌가요?")
    print("b) 공유기 설정을 확인하세요. 공유기 설정이 잘못되어 있거나, 공유기가 다른 공유기들도 사용하는 채널을 사용하고 있어 전파 간섭이 일어나고 있지는 않나요?")
    print("c) 컴퓨터 프로그램 상태를 확인하세요. 컴퓨터에 다른 응용 프로그램, 백그라운드 실행 프로그램이 돌아가고 있는 것은 아닌가요?")
    print("d) 주변에 너무 많은 사람이 같은 네트워크에 접속하고 있지는 않은지 확인하세요. 너무 많은 사람이 같은 네트워크를 동시에 사용하면 당연히 느려질 수 밖에 없어요.")
    pass
else:
    print("- PING 요청이 너무 많이 실패했습니다. 서버와의 연결이 매우 불안정합니다. 다음을 즉시 확인하세요.")
    print("a) 네트워크 연결 상태를 확인하세요. 중간에 네트워크가 끊기는 것은 아닌가요?")
    print("b) 공유기 설정을 확인하세요. 공유기 설정이 잘못되어 있거나, 공유기가 다른 공유기들도 사용하는 채널을 사용하고 있어 전파 간섭이 일어나고 있지는 않나요?")
    print("c) 컴퓨터 프로그램 상태를 확인하세요. 컴퓨터에 다른 응용 프로그램, 백그라운드 실행 프로그램이 돌아가고 있는 것은 아닌가요?")
    print("d) 주변에 너무 많은 사람이 같은 네트워크에 접속하고 있지는 않은지 확인하세요. 너무 많은 사람이 같은 네트워크를 동시에 사용하면 당연히 느려질 수 밖에 없어요.")
    pass
print("")
buffer = input(">> 엔터키를 누르면 종료됩니다. 수강신청 올킬하세요!")
