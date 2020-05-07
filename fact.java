import java.util.Scanner;
class Factorial{
  static int givefactorial(int n){
    if(n==0|n==1){
      return(1);
    }
    else{
    return((n)*givefactorial(n-1));
    }
  }
  public static void main(String[] args){
    Scanner inp = new Scanner(System.in);
    System.out.print("Enter the number:- ");
    int num = inp.nextInt();
    int output=givefactorial(num);
    System.out.println("Factorial of the number is :- "+ output);
  }
}
