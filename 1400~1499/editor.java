import java.io.IOException;
import java.util.*;
import java.io.*;

// https://www.acmicpc.net/problem/1406
public class editor {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String str = br.readLine();
		int n = Integer.parseInt(br.readLine());
		Stack<Character> rStack = new Stack<Character>();
		Stack<Character> lStack = new Stack<Character>();
		int idx = 0;


		for(int i = 0; i < str.length(); i++) {
			lStack.add(str.charAt(i));
		}


		for(int i = 0; i < n; i++) {
			String command = br.readLine();
			char c = command.charAt(0);
            
			switch(c) {
			case 'L':
				if(!lStack.isEmpty()){
					rStack.add(lStack.pop());
				}

				break;
			case 'D':
				if(!rStack.isEmpty()) {
					lStack.add(rStack.pop());
				}

				break;
			case 'B':
				if(!lStack.isEmpty()) {
					lStack.pop();
				}
				break;
			case 'P':
				char t = command.charAt(2);
				lStack.add(t);

				break;
			default:
				break;
			}
		}

		while(!lStack.isEmpty()){
			rStack.add(lStack.pop());
		}
		while(!rStack.isEmpty()){
			bw.write(rStack.pop());
		}
		
		bw.flush();
		bw.close(); 
	}
}
