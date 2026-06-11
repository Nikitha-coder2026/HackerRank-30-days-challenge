/* ------------HackerRank 30 days challenge-------*/
/* -------------------Day 21: Generics-----------*/

import java.util.*;

class Printer <T> {
     /**
     * Method Name: PrintArray
     * print each element on a new line. Do not return anything.
     * @param a generic array
     **/

     // write your code here
     public <T> void printArray(T[] array){
         // we use a "For-Each" loop to iterate through
         for(T element: array){
             System.out.println(element);
         }
     }
}

public class Solution {

      public static void main (String args[]){
             Scanner scanner = new Scanner(System.in);
             int n = scanner.nextInt();
             Integer[] intArray = new Integer[n];
             for (int i = 0; i < n; i++) {
                 intArray[i] = scanner.nextInt();
             }

             n = scanner.nextInt();
             String[] stringArray = new String[n];
             for (int i = 0; i < n; i++) {
                 stringArray[i] = scanner.next();
             }

             Printer<Integer> intPrinter = new Printer<Integer>();
             Printer<String> stringPrinter = new Printer<String>();
             intPrinter.printArray(intArray);
             stringPrinter.printArray(stringArray);
             if(Printer.class.getDeclaredMethods().length > 1){
                 System.out.println("The Printer class should only have 1 method named printArray."); 
             }
      }
}
