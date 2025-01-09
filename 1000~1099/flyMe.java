import java.io.IOException;
import java.io.*;

// https://www.acmicpc.net/problem/1011
public class flyMe {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		

		for(int i = 0; i < n; i++) {
			
			String command = br.readLine();
			String[] c = command.split(" ");
			int distance = Integer.valueOf(c[1]) - Integer.valueOf(c[0]);
			int max = (int)Math.sqrt(distance);
	
			if(max == Math.sqrt(distance)){
				System.out.println(max * 2 - 1);
			} else if(distance <= max * max + max){
				System.out.println(max * 2);
			} else {
				System.out.println(max * 2 + 1);
			}


		}
	}
}
