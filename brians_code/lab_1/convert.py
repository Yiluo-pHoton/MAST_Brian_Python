import pytest

def fToC(fTemp):
    return (fTemp - 32) * 5/9 # TODO: Fix this line of code

def cToF(cTemp):
    return (cTemp * 9/5) + 32 # TODO: Fix this line of code
    
def test_fToC_freezing():
   assert fToC(32.0)==pytest.approx(0.0) 

def test_cToF_freezing():
   assert cToF(0.0)==pytest.approx(32.0) 

def test_fToC_boiling():
   assert fToC(212.0)==pytest.approx(100.0) 

def test_cToF_boiling():
   assert cToF(100.0)==pytest.approx(212.0) 
