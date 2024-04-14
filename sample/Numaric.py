num = input('정수 혹은 소수를 입력하세요: ')

float_num = float(num)
print(f'입력한 숫자의 소수형: {float_num}')

int_num = int(float(num))
print(f'입력한 숫자의 정수형: {int_num}')