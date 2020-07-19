import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        while (T-- > 0) {
            int n = scan.nextInt();
            n = scan.nextInt();

            int[][] mat = new int[n][n];

            

            for(int i = 0; i< mat.length; i++){
                for(int j=0; j<mat[i].length; j++){
                    mat[i][j] = scan.nextInt();
                }
            }

            int no_repeated_rows = 0;
            int no_repeated_cols = 0;
            boolean repeat = true;

            for(int i = 0; i< mat.length; i++){
                repeat = false;
                for(int j=0; j<mat[i].length; j++){
                    for(int k=j+1; k<mat[i].length; k++)
                        if (mat[i][j] == mat[i][k])
                        {
                            no_repeated_rows++;
                            repeat = true;
                            break;
                        }
                    if(repeat)
                        break;
                }
            }

            for(int i = 0; i< mat[0].length; i++){
                repeat = false;
                for(int j=0; j<mat.length; j++){
                    for(int k=j+1; k<mat.length; k++)
                        if (mat[j][i] == mat[k][i])
                        {
                            no_repeated_cols++;
                            repeat = true;
                            break;
                        }
                    if(repeat)
                        break;
                }
            }


            if (no_repeated_cols==0 && no_repeated_rows == 0)
                System.out.println("SAFE");
            else
                System.out.println("DANGER " + no_repeated_rows + " " + no_repeated_cols);

        }
    }


}
