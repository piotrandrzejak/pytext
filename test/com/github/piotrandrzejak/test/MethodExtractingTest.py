'''
Created on 9 wrz 2016

@author: piotr.andrzejak
'''
import unittest
from com.github.piotrandrzejak.java import JavaCodeAnalyzer


class MethodExtractingTest(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        global content
        content = "public static void methodName() {\n" 
        content += "int a = 4;\n" 
        content += "System.out.println(\"this is: \", \+ a;\n}" 

    def test_shouldReturnMethodBody(self):
        # given
        methodName = "methodName"
        expectedResult = "int a = 4;\n" 
        expectedResult += "System.out.println(\"this is: \", \+ a;"
        
        # when
        methodBody = JavaCodeAnalyzer.getMethodContent(methodName)
        
        # then
        self.assertEqual(expectedResult, methodBody, "method body")
        