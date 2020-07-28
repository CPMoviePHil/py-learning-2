# 傳統的if-elif-else
# 的邏輯控制


class TradControlFlow:
    def __init__(self, status_1, status_2, status_3):
        self.is_friend = status_1
        self.is_working = status_2
        self.is_student = status_3
        self.message = ''

    def process(self):
        if self.is_student and self.is_friend:
            self.message = '學弟你好阿'
        elif not self.is_student and self.is_friend:
            self.message = '同學你好阿!'
        elif self.is_student and not self.is_friend:
            self.message = '學生們，給我去當社畜吧'
        else:
            self.message = 'who the fuck are you?'

    def get_message(self):
        return self.message


person1 = TradControlFlow(False, True, True)
person1.process()
person2 = TradControlFlow(False, False, False)
person2.process()
print(f'{person1.get_message()}\n')
print(f'{person2.get_message()}')


# 以上用ternary operator改寫control-flow


class SimpleControlFlow:
    def __init__(self, status_1, status_2, status_3):
        self.is_friend = status_1
        self.is_working = status_2
        self.is_student = status_3
        self.message = ''

    def process(self):
        # 假如if成立做的事if condition else不成立做的事
        self.message = '朋友好!' if self.is_friend else '你不是我朋友'

    def get_message(self):
        return self.message


person3 = SimpleControlFlow(False, False, False)
person3.process()
print(f'{person3.get_message()}')
