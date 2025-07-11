import lexer_owo
import parser_owo

class BasicExecute:
    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)

    def walkTree(self, node):
        if isinstance(node, int):
            return node
        if isinstance(node, str):
            return node

        if node is None:
            return None

        if node[0] == 'program':
            if node[1] is None:
                self.walkTree(node[2])
            else:
                self.walkTree(node[1])
                self.walkTree(node[2])

        if node[0] == 'num':
            return node[1]

        if node[0] == 'str':
            return node[1]

        if node[0] == 'print':
            value = self.walkTree(node[1])
            if isinstance(value, str) and value[0] == '"':
                print(value[1:-1])  # Menggunakan metode slicing
            else:
                return value

        if node[0] == 'if_stmt':
            result = self.walkTree(node[1])
            branch = node[2][1] if result else node[2][2]
            return self.walkTree(branch)

        if node[0] == 'condition_eqeq':
            return self.walkTree(node[1]) == self.walkTree(node[2])

        if node[0] == 'fun_def':
            self.env[node[1]] = node[2]
            print("nggawe fungsi: '%s'" % node[1])
            self.printEnv()

        if node[0] == 'fun_call':
            try:
                return self.walkTree(self.env[node[1]])
            except LookupError:
                print("fungsine ora ono '%s'" % node[1])
                return 0

        if node[0] == 'add':
            left_value = self.walkTree(node[1])
            right_value = self.walkTree(node[2])
            if isinstance(left_value, int) and isinstance(right_value, int):
                return left_value + right_value
            else:
                raise TypeError("Invalid operands for addition: %s and %s" % (left_value, right_value))
        elif node[0] == 'sub':
            return self.walkTree(node[1]) - self.walkTree(node[2])
        elif node[0] == 'mul':
            return self.walkTree(node[1]) * self.walkTree(node[2])
        elif node[0] == 'div':
            return int(self.walkTree(node[1]) / self.walkTree(node[2]))

        if node[0] == 'var_assign':
            self.env[node[1]] = self.walkTree(node[2])
            print("nggawe variabel: '%s' = %s" % (node[1], self.env[node[1]]))
            self.printEnv()
            return node[1]

        if node[0] == 'pow':
            base = self.walkTree(node[1])
            exponent = self.walkTree(node[2])
            return base ** exponent

        if node[0] == 'var':
            try:
                return self.env[node[1]]
            except LookupError:
                print("variabel ora ono '%s'" % node[1])
                return 0

        if node[0] == 'for_loop':
            if node[1][0] == 'for_loop_setup':
                loop_setup = self.walkTree(node[1])

                loop_count = self.env[loop_setup[0]]
                loop_limit = loop_setup[1]

                for i in range(loop_count + 1, loop_limit + 1):
                    res = self.walkTree(node[2])
                    if res is not None:
                        print(res)
                    self.env[loop_setup[0]] = i
                del self.env[loop_setup[0]]
                self.printEnv()

        if node[0] == 'for_loop_setup':
            return (self.walkTree(node[1]), self.walkTree(node[2]))

    def printEnv(self):
        print("infone :")
        for key, value in self.env.items():
            print(key, "=", value)
        print("------------------")


if __name__ == '__main__':
    lexer = lexer_owo.leksikal()
    parser = parser_owo.sintaksis()
    env = {}
    while True:
        try:
            text = input('owo > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            BasicExecute(tree, env)
