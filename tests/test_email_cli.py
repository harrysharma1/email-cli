import pytest
from cli.email import KCLEmailChecker

class TestEmailCli:
        

        def test_is_correct_format(email_checker):
            email_checker = KCLEmailChecker()
            assert email_checker.is_correct_format("") == False    
            assert email_checker.is_correct_format("k1234567@kcl.ac.uk") == True
            assert email_checker.is_correct_format("john.doe@kcl.ac.uk") == True
            assert email_checker.is_correct_format("jane.1.doe@kcl.ac.uk") == True
            assert email_checker.is_correct_format("john.d.doe@kcl.ac.uk") == True
            assert email_checker.is_correct_format("jane.doe.1@kcl.ac.uk") == False
            assert email_checker.is_correct_format("jane.doe.1@kcl.ac.com") == False
            assert email_checker.is_correct_format("jane.doe.1@kcl.ac") == False

        def test_get_name(email_checker):
            email_checker = KCLEmailChecker()
            assert email_checker.get_name("")  == "Incorrect Format"
            assert email_checker.get_name("k1234567@kcl.ac.uk") == "K Number: K1234567"
            assert email_checker.get_name("john.doe@kcl.ac.uk") == "John Doe"
            assert email_checker.get_name("jane.1.doe@kcl.ac.uk") == "Jane Doe"
            assert email_checker.get_name("john.d.doe@kcl.ac.uk") == "John D. Doe"
            assert email_checker.get_name("jane.doe.1@kcl.ac.uk") == "Incorrect Format"
            assert email_checker.get_name("jane.doe.1@kcl.ac.com") == "Incorrect Format"
            assert email_checker.get_name("jane.doe.1@kcl.ac") == "Incorrect Format"