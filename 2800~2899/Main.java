import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int apple = scanner.nextInt();
        int array[] = new int[apple+1];
        char direct;
        int sum = 0;
        int left = 1;
        int right = m;
        int dropApple;
        int answer = 0;

        array[0] = 1;
        direct = '<';
        
        for(int i=0; i<apple; i++) {
            dropApple = scanner.nextInt();

            if(dropApple < left){
                left -= (left-dropApple);
                right -= (left-dropApple);
                answer += (left-dropApple);
            } else if(right < dropApple) {
                left += (dropApple - right);
                right += (dropApple - right);
                answer += (dropApple - right);
            }


            
        }
        System.out.println(answer);
        
        scanner.close();
    }
}