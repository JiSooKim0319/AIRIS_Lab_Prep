try:
    print("나누기 전용 계산기입니다.")
    # num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    # num2 = int(input("두 번째 숫자를 입력하세요 : "))
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print(" {0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error ! 잘못된 값을 입력하셨습니다. ")
    print("다시 입력해주세요!")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)