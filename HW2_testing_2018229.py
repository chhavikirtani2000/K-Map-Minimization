import unittest

from HW2_2018229 import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
                self.assertEqual(minFunc(4,"(0,1,2,3,9,10,13) d(4,5,6)"),"A'B'+B'CD'+C'D")
                self.assertEqual(minFunc(4,"(0,1,5,7) d(2,3)"),"A'B'+A'D")
                self.assertEqual(minFunc(4,"(1,3,9,11,12) d(2,4,14)"),"B'D+BC'D'")
                self.assertEqual(minFunc(4,"(3,6,11,13) d(2,8,10)"),"A'CD'+ABC'D+B'C")
                self.assertEqual(minFunc(4,"(1,3,9,11,12,10) d(2,4)"),"B'C+B'D+BC'D'")
                self.assertEqual(minFunc(4,"(1,4,6) d(12,14,15)"),"A'B'C'D+BD'")
                self.assertEqual(minFunc(4,"(0,1,2,4,5,6,8,9,12,13,14) d-"),"A'D'+BD'+C'")
                self.assertEqual(minFunc(4,"(3,6,13,11,15) d(2,10)"),"A'CD'+ABD+B'C")
                self.assertEqual(minFunc(4,"(0,11,14,15) d(1,2,3,4,5,6,7)"),"A'+BC+CD")
                self.assertEqual(minFunc(4,"(1,3,7,11,15) d(0,2,5)"),"A'B'+CD")
                self.assertEqual(minFunc(4,"(0,3,5,7,11,13,15) d(1,2,4)"),"A'B'+BD+CD")
                self.assertEqual(minFunc(4,"(1,2,4) d(0,3,5,7,11,13,15)"),"A'B'+A'C'")
                self.assertEqual(minFunc(4,"(3,4) d(11,14,15)"),"A'BC'D'+B'CD")
                self.assertEqual(minFunc(3,"(1,4,6) d(2,3)"),"A'C+AC'")
                self.assertEqual(minFunc(3,"(1,2,3) d(4,6)"),"A'B+A'C")
                self.assertEqual(minFunc(3,"(1,2,3) d-"),"A'B+A'C")
                self.assertEqual(minFunc(3,"(1,3,4) d(2)"),"A'C+AB'C'")
                self.assertEqual(minFunc(3,"(3,4) d(2)"),"A'B+AB'C'")
                self.assertEqual(minFunc(3,"(3,4) d(5,7)"),"AB'+BC")
                self.assertEqual(minFunc(3,"(1,3,4) d(5,7)"),"AB'+C")
                self.assertEqual(minFunc(3,"(4,5,7) d(1,3)"),"AB'+C")
                self.assertEqual(minFunc(3,"(1,2,3,4,5,6,7) d(0)"),"1")
                self.assertEqual(minFunc(3,"(1,3,7) d(0,2,5)"),"C")
                self.assertEqual(minFunc(3,"(0,1,5) d(6,7)"),"A'B'+B'C")
                self.assertEqual(minFunc(2,"(1,2) d(3)"),"A+B")
                self.assertEqual(minFunc(2,"(0,1) d(3)"),"A'")
                self.assertEqual(minFunc(2,"(0,1,2) d-"),"A'+B'")
                self.assertEqual(minFunc(2,"() d(2,3)"),"0")
                self.assertEqual(minFunc(1,"(1) d-"),"A")
                self.assertEqual(minFunc(1,"(0) d-"),"A'")
                self.assertEqual(minFunc(1,"() d(1,0)"),"0")
                
                
                
		
                
if __name__=='__main__':
	unittest.main()
