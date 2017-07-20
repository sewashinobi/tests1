# You should be able to use the python interpreter to run this script,
# and it should display 3 test failures. You need to fix the tests so
# that they all pass.
#
# IMPORTANT:
# Only modify the code where indicated. Do not modify the intent of the test
#
import unittest

class PythonTests(unittest.TestCase):
    def test_multipliers(self):
        # Fix this loop and function definition so that the test
        # passes. 'multipliers' should become a list of functions. The
        # first should be a function that multiplies its parameter by
        # 0, the second by 1, the third by 2, and so on.
        
        # MODIFY IN HERE ONLY
        
        multipliers = []
        for val in range(6):
            multiplier = lambda x: x * val
            multipliers.append(multiplier)

        # END MODIFY IN HERE ONLY

        # Call each function with the parameter 5. We expect to get
        # the 5 times table.
        expected_result = [0, 5, 10, 15, 20, 25]
        actual_result = []
        for multiplier in multipliers:
            actual_result.append(multiplier(5))

        self.assertEqual(actual_result, expected_result)

    def test_person(self):
        # What is wrong with this class definition that causes the test to fail?

        # MODIFY IN HERE ONLY
        
        class Person(object):
            def __init__(self, name, children=[]):
                self.name = name
                self.children = children

            def add_child(self, child):
                self.children.append(child)

            def __repr__(self):
                return '<Person %r>' % self.name

        # END MODIFY IN HERE ONLY

        # Create a family tree where dick is the parent of harry, and
        # harry is the parent of tom. There are 2 ways of adding
        # children - either by passing a list of children to the
        # constructor, or by calling the add_child method.
        tom = Person('tom')
        harry = Person('harry')
        harry.add_child(tom)
        dick = Person('dick', children=[harry])

        self.assertEqual(dick.children, [harry])
        self.assertEqual(harry.children, [tom])
        self.assertEqual(tom.children, [])

    def test_forwarding(self):
        # Define forwarding_property so that it acts as a descriptor
        # such that getting it and setting it actually accesses a
        # 'sub-attribute' of the parent object.

        # MODIFY IN HERE ONLY

        class forwarding_property(object):
            def __init__(self, path):
                self.objectName,self.attrName = path.split('.')

            def __get__(self, instance, owner=None):
                return getattr(getattr(instance, self.objectName), self.attrName)

            def __set__(self, instance, value):
                setattr(getattr(instance, self.objectName), self.attrName, value)

            def __delete__(self, instance):
                delattr(getattr(instance, self.objectName), self.attrName)

        # END MODIFY IN HERE ONLY

        # For example, instances of 'B' contain an instance of 'A'
        # (called obj). Access to b.blah should be forwarded to
        # b.obj.some_attribute.
        class A(object):
            some_attribute = 'old_value'
            def __init__(self):
                self.c_inst = C()

        
        class B(object):
            # The 'blah' attribute should mirror 'obj.some_attribute'
            blah = forwarding_property('obj.some_attribute')
            c_size = forwarding_property('obj.c_inst.size')
            def __init__(self):
                self.obj = A()
        
        
        class C(object):
            def __init__(self):
                self.size = 3
        
        
        # Here's the test:
        b = B()
        self.assertEqual(b.blah, 'old_value')
        b.blah = 'new_value'
        b.c_size = 42
        self.assertEqual(b.blah, 'new_value')
        self.assertEqual(b.obj.some_attribute, 'new_value')
        self.assertEqual(b.obj.c_inst.size, 42)


if __name__ == '__main__':
    unittest.main()
