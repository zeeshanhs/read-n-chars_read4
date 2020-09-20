from reader_function import readers


def test_read10():
    x = 10 # this function reads 10 times
    instance = readers(x)
    
    # if you change READN() definition to accept 'self' then you can pass readn() without argument
        # if test fails, print: "test_read10() expected 20" 
    assert instance.readn() == 20, "test_read10() expected 20"

    # assert instance.readn(n) == 20