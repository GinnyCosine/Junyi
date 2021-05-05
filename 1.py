def question1A(string):
    return string[::-1]

def question1B(string):
    reverse = [word[::-1] for word in string.split(' ')]
    return ' '.join(reverse)

if __name__ == '__main__':
    assert question1A('blocking') == 'gnikcolb', '1A wrong'
    assert question1B('The impact of the crash destroyed the car') == 'ehT tcapmi fo eht hsarc deyortsed eht rac', '1B wrong'