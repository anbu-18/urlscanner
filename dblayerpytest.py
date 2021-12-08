import pytest
import dblayer



class Testing():
    
    def test_a_insertvalue(self):
        try:
            newrecord = "http://www.google.com"
            response = dblayer.insert_record(newrecord)
            if response == 1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False

    def test_b_updatevalue(self):
        try:
            newrecord = "http://www.yahoo.com"
            response = dblayer.update_record(1,newrecord,True)
            if response == 1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False
                
    def test_c_vanishrecord(self):
        try:
            response = dblayer.update_record(1," ",False)
            if response == 1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False

    def test_d_deletetable(self):
        try:
            response = dblayer.delete_table()
            if response ==1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False
            

#pytest.main(["dblayerpytest.py","--capture=sys"])
