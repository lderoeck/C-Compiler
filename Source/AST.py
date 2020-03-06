"""Abstract Syntax Tree"""


class AST:

    def __init__(self):
        self.root = None
        self.depthStack = []

    def simplify(self):
        self.depthStack = [self.root]
        while len(self.depthStack) > 0:
            item = self.depthStack.pop()
            if len(item.children) == 1:
                if (isinstance(item, ASTNodeExpression) or isinstance(item, ASTNodeStatement)) and item.canReplace:
                    # print("replacing:", item.value, "at pos:", item.index)
                    item.parent.replace_child(item.index, item.children[0])

            for i in reversed(item.children):
                self.depthStack.append(i)

        self.depthStack = [self.root]
        while len(self.depthStack) > 0:
            item = self.depthStack.pop()
            item.simplify()

            for i in reversed(item.children):
                self.depthStack.append(i)

    def print_tree(self, _file=None):

        print("digraph G {", file=_file)

        self.depthStack = [self.root]

        while len(self.depthStack) > 0:
            item = self.depthStack.pop()

            item.print_dot(_file)

            for i in item.children:
                print('"', item, '" -> "', i, '"', file=_file)

            for i in reversed(item.children):
                self.depthStack.append(i)

        print("}", file=_file)


'''Core'''


class ASTNode:

    def __init__(self, _val='Undefined'):
        # print("created:", _val)
        self.canReplace = True
        self.parent = None
        self.index = 0
        self.children = []
        self.value = _val

    def add_child(self, child):
        # print("added: ", child.value, "to:", self.value)
        child.parent = self
        child.index = len(self.children)
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def remove_child_at_pos(self, index):
        pass

    def replace_child(self, index, new_child):
        new_child.parent = self
        new_child.index = index
        self.children[index] = new_child

    def print_dot(self, _file=None):
        print('"', self, '"', '[label = "', self.value, '"]', file=_file)

    def simplify(self):
        pass


class ASTNodeLib(ASTNode):

    def __init__(self):
        super().__init__("Lib")


class ASTNodeFunction(ASTNode):

    def __init__(self):
        super().__init__("Function")


class ASTNodeParams(ASTNode):
    def __init__(self):
        super().__init__("Params")


class ASTNodeParam(ASTNode):
    def __init__(self):
        super().__init__("Param")


'''Statements'''


class ASTNodeStatement(ASTNode):
    def __init__(self, _val="Statement"):
        super().__init__(_val)

    pass


class ASTNodeBreak(ASTNodeStatement):

    def __init__(self):
        super().__init__("Break")


class ASTNodeContinue(ASTNodeStatement):

    def __init__(self):
        super().__init__("Continue")


class ASTNodeExpressionStatement(ASTNodeStatement):
    def __init__(self, _val="Expression statement"):
        super().__init__(_val)

    pass


class ASTNodeCompound(ASTNodeStatement):
    def __init__(self, _val="Compound statement"):
        super().__init__(_val)

    pass


class ASTNodeDefinition(ASTNodeStatement):

    def __init__(self):
        super().__init__("Definition")
        self.canReplace = False
        self.type = None
        self.name = None

    def print_dot(self, _file=None):
        print('"', self, '"', '[label = "', self.value, ":", self.type, self.name, '"]', file=_file)


class ASTNodeIf(ASTNodeStatement):

    def __init__(self):
        super().__init__("If statement")
        self.Condition = None
        self.body = None


class ASTNodeLoopStatement(ASTNodeStatement):

    def __init__(self):
        super().__init__("Loop statement")
        self.Condition = None
        self.body = None


class ASTNodeReturn(ASTNodeStatement):

    def __init__(self):
        super().__init__("Return statement")
        self.canReplace = False


'''Expressions'''


class ASTNodeExpression(ASTNode):

    def __init__(self, val="Expression"):
        super().__init__(val)


class ASTNodeConditional(ASTNodeExpression):
    def __init__(self):
        super().__init__("Conditional expression")


class ASTNodeUnaryExpr(ASTNodeExpression):
    def __init__(self, _val="Unary expression"):
        super().__init__(_val)


class ASTNodeTernaryExpr(ASTNodeExpression):
    def __init__(self):
        super().__init__("Ternary expression")


class ASTNodeLiteral(ASTNode):

    def __init__(self, value="Value"):
        super().__init__(value)
        self.isConst = False


class ASTNodeDecrement(ASTNodeUnaryExpr):
    def __init__(self):
        super().__init__("Decrement")


class ASTNodeIncrement(ASTNodeUnaryExpr):
    def __init__(self):
        super().__init__("Increment")


class ASTNodeEqualityExpr(ASTNodeUnaryExpr):
    def __init__(self):
        super().__init__("Equality expression")
        self.canReplace = False
        self.id = None
        self.equality = None

    def print_dot(self, _file=None):
        print('"', self, '"', '[label = "', self.value, ":", self.id, self.equality, '"]', file=_file)


class ASTNodeFunctionCallExpr(ASTNodeUnaryExpr):
    def __init__(self):
        super().__init__("Function call expression")


class ASTNodeIndexingExpr(ASTNodeUnaryExpr):
    def __init__(self):
        super().__init__("Indexing expression")


class ASTNodeInverseExpr(ASTNodeUnaryExpr):
    def __init__(self):
        super().__init__("Inverse expression")


class ASTNodeNegativeExpr(ASTNodeUnaryExpr):

    def __init__(self):
        super().__init__("Negative expression")
        self.canReplace = False

    def simplify(self):

        if isinstance(self.children[0], ASTNodeLiteral):
            if self.children[0].isConst:
                self.children[0].value *= -1
                self.parent.children[:] = [self.children[0] if x == self else x for x in self.parent.children]
                #self.parent.replace_child(self, self.children[0])



class ASTNodePositiveExpr(ASTNodeUnaryExpr):

    def __init__(self):
        super().__init__("Positive expression")


'''Opperations'''


class ASTNodeOpp(ASTNodeExpression):
    def __init__(self, tt="opp"):
        super().__init__(tt)
        self.opperators = []


class ASTNodeAddition(ASTNodeOpp):

    def __init__(self):
        super().__init__("Addition")

    def simplify(self):

        leftovers = []
        tot = self.children[0]
        if not isinstance(tot, float):
            leftovers.append(tot)

        for i in range(len(self.opperators)):
            right = self.children[i+1]

            if isinstance(right, ASTNodeLiteral):
                if isinstance(tot, float):
                    if right.isConst:
                        if self.opperators[i] == "+":
                            tot += right.value
                        else:
                            tot -= right.value

                    else:
                        leftovers.append(right)
                else:
                    if right.isConst:
                        tot = right.value
                    else:
                        leftovers.append(right)
            else:
                leftovers.append(right)

        if len(leftovers) > 0:
            self.children = leftovers
            if isinstance(tot, float) or isinstance(tot, int):
                self.add_child(ASTNodeLiteral(tot))
        else:
            self.parent.replace_child(self.index, ASTNodeLiteral(tot))


class ASTNodeMult(ASTNodeOpp):

    def __init__(self):
        super().__init__("Multiplication")

    def simplify(self):
        return
        leftovers = []
        tot = 1
        for i in self.children:
            if isinstance(i, ASTNodeLiteral):
                if i.isConst:
                    tot = tot * i.value
                else:
                    leftovers.append(i)

        if leftovers:
            self.children = leftovers
            self.add_child(ASTNodeLiteral(tot))
        else:
            self.parent.replace_child(self.index, ASTNodeLiteral(tot))

