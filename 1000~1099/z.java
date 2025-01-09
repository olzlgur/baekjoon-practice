import java.io.IOException;
import java.io.*;

// https://www.acmicpc.net/problem/1074
public class z {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
        String[] list = s.split(" ");
      //  int total = Integer.parseInt(list[0]), y = Integer.parseInt(list[1]), x = Integer.parseInt(list[2]);

		System.out.println(recul((long)Math.pow(2,Double.parseDouble(list[0])), -1, Long.parseLong(list[1]), Long.parseLong(list[2])));
	}

    static long recul(long t, long answer, long y, long x){
        if(t == 2){
          //  System.out.println("1: t: " + t + " y: " + y + " x:" + x + " answer: "+ answer);
            if(y == 0 && x == 0){
                return answer + 1;
            } 
            if(y == 0 && x == 1){
                return answer + 2;
            }
            if(y == 1 && x == 0){
                return answer + 3;
            }
            return answer + 4;
            
        } 
        t = t/2;
        if(y < t && x < t){
          //  System.out.println("1: t: " + t + " y: " + y + " x:" + x + " answer: "+ answer);
            return recul(t, answer, y, x);
        }else if(y < t  && x >= t){
           // System.out.println("2: t: " + t + " y: " + y + " x:" + x + " answer: "+ answer);
            return recul(t, answer + t*t, y, x-t);
        }else if(y >= t && x < t){
          //  System.out.println("3: t: " + t + " y: " + y + " x:" + x + " answer: "+ answer);
            return recul(t, answer + 2*t*t, y-t, x);
        }else{
          //  System.out.println("4: t: " + t + " y: " + y + " x:" + x + " answer: "+ answer);
            return recul(t, answer + 3*t*t, y-t, x-t);
        }
    }
}
