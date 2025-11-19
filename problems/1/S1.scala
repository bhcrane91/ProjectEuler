object S1
{ 
    def main(args: Array[String]) 
    { 
        var ans = 0; 
        var arg = 1000;
        for (i <- 1 to arg-1) {
            ans += (if (i % 5 == 0 || i % 3 == 0) i else 0);
        }
        println ("Addition is: "+ ans ); 
    } 
}