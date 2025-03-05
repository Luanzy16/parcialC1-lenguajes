from calVisitor import calVisitor

class calcVisitor(calVisitor):
    def visitNumber(self, ctx):
        return complex(ctx.NUMBER().getText())  # Permitir números complejos

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitMul(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right

    def visitDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left / right  

    def visitAdd(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right

    def visitSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left - right

