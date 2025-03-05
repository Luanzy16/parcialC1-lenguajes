# Generated from cal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .calParser import calParser
else:
    from calParser import calParser

# This class defines a complete listener for a parse tree produced by calParser.
class calListener(ParseTreeListener):

    # Enter a parse tree produced by calParser#Add.
    def enterAdd(self, ctx:calParser.AddContext):
        pass

    # Exit a parse tree produced by calParser#Add.
    def exitAdd(self, ctx:calParser.AddContext):
        pass


    # Enter a parse tree produced by calParser#Div.
    def enterDiv(self, ctx:calParser.DivContext):
        pass

    # Exit a parse tree produced by calParser#Div.
    def exitDiv(self, ctx:calParser.DivContext):
        pass


    # Enter a parse tree produced by calParser#Sub.
    def enterSub(self, ctx:calParser.SubContext):
        pass

    # Exit a parse tree produced by calParser#Sub.
    def exitSub(self, ctx:calParser.SubContext):
        pass


    # Enter a parse tree produced by calParser#Mul.
    def enterMul(self, ctx:calParser.MulContext):
        pass

    # Exit a parse tree produced by calParser#Mul.
    def exitMul(self, ctx:calParser.MulContext):
        pass


    # Enter a parse tree produced by calParser#Parens.
    def enterParens(self, ctx:calParser.ParensContext):
        pass

    # Exit a parse tree produced by calParser#Parens.
    def exitParens(self, ctx:calParser.ParensContext):
        pass


    # Enter a parse tree produced by calParser#Imaginary.
    def enterImaginary(self, ctx:calParser.ImaginaryContext):
        pass

    # Exit a parse tree produced by calParser#Imaginary.
    def exitImaginary(self, ctx:calParser.ImaginaryContext):
        pass


    # Enter a parse tree produced by calParser#Real.
    def enterReal(self, ctx:calParser.RealContext):
        pass

    # Exit a parse tree produced by calParser#Real.
    def exitReal(self, ctx:calParser.RealContext):
        pass



del calParser