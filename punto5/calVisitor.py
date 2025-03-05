# Generated from cal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .calParser import calParser
else:
    from calParser import calParser

# This class defines a complete generic visitor for a parse tree produced by calParser.

class calVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calParser#Add.
    def visitAdd(self, ctx:calParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calParser#Div.
    def visitDiv(self, ctx:calParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calParser#Sub.
    def visitSub(self, ctx:calParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calParser#Mul.
    def visitMul(self, ctx:calParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calParser#Parens.
    def visitParens(self, ctx:calParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calParser#Imaginary.
    def visitImaginary(self, ctx:calParser.ImaginaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calParser#Real.
    def visitReal(self, ctx:calParser.RealContext):
        return self.visitChildren(ctx)



del calParser