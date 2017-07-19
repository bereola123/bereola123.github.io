import java.util.Scanner;

public class ifelseJava
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
      //System.out.print("Enter a number: "); 
      //int x = keyboard.nextInt();
      
      //if (x > 500)
      //   System.out.println("X is really big");
      //else if (x > 50)
      //   System.out.println("X is sort of big");
      //else if (x < 0)
      //   System.out.println("X is negative!");
      //else
      //   System.out.println("X is not very interesting") ;   
      
      int testScore;
      char letterGrade;
      
      System.out.print("Enter your numeric test score and " + "I will tell you the grade: ");
      testScore = keyboard.nextInt();
      letterGrade = getLetterGrade(testScore);
      System.out.println("**** Your letter grade is: " + letterGrade);  
   }
   public static char getLetterGrade (int score)
   {
      char grade;
      
      if (score < 60)
         grade = "F";
      else if (score < 70)
         grade = "D";
      else if (score < 80)
         grade = "C";
      else if (score <90)
         grade = "B";
      else
         grade = "A";
   }
}
