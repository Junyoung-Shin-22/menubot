import argparse

class ParserException(Exception):
    pass

class Parser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(status=2, message=message)

    def exit(self, status=0, message=None):
        if status:
            raise ParserException(message)
    
    def parse_args(self, *args, **kwargs):
        try:
            return super().parse_args(*args, **kwargs)
        except ParserException as e:
            return None

PARSER = Parser(add_help=False, prog='ㅈㅁㅁ')

PARSER.add_argument('-c', dest='category', type=str, help='카테고리 ("기본" 또는 "컵라면")', default='전체')
PARSER.add_argument('-n', dest='amount', type=int, help='출력할 개수 (1~10)', default=1)

PARSER_HELP = PARSER.format_help()

if __name__ == '__main__':
    commands =\
    [
        'ㅈㅁㅁ', 
        'ㅈㅁㅁ -c 컵라면',
        'ㅈㅁㅁ -n 10',
        'ㅈㅁㅁ -c 컵라면 -n 10',
        'ㅈㅁㅁ 이상한 입력']
    
    for command in commands:
        args = command.split()[1:]
        parsed = PARSER.parse_args(args)
        if parsed is not None:
            print(type(parsed), parsed)
        else:
            print(PARSER_HELP)