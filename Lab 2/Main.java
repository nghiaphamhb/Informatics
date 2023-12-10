import java.util.Scanner;
public class Main{
    private static char[]c;
    public static void main (String[] args){
        System.out.println("Enter: ");
        Scanner sc= new Scanner (System.in);
        String str= sc.nextLine();
        c= str.toCharArray();
        System.out.println("Original Message: "+ message(c));
        defineS(c);
        System.out.println("Sequence syndrome S(s1;s2;s3)= "+defineS(c));
        toCorrect(c, defineError(c, defineS(c)));
        System.out.println("Final Received Message: "+ message(c));
    }

    public static String message (char[]c){
        String ms=""+c[2]+c[4]+c[5]+c[6];
        return ms;
    }

    public static String defineS(char[] c ){
        int n1=0, n2=0, n3=0;
        char[] s= new char [3];

        if(c[0]=='1') n1++;
        if(c[1]=='1') n2++;
        if(c[2]=='1') {n1++; n2++;}
        if(c[3]=='1') n3++;
        if(c[4]=='1') {n1++; n3++;}
        if(c[5]=='1') {n2++; n3++;}
        if(c[6]=='1') {n1++; n2++; n3++;}

        if(n1%2==0) s[0]='0';
        else s[0]='1';
        if(n2%2==0) s[1]='0';
        else s[1]='1';
        if(n3%2==0) s[2]='0';
        else s[2]='1';

        String S="";
        for(char z: s){
            S+=z;
        }
        return S;
    }

    public static int defineError (char[]c, String S){
        if(S.equals("000")){
            System.out.println("No error");
            return 7;
        }
        else if(S.equals("001")){
            System.out.println("Error in check bit r3 (r3= "+c[3]+")");
            return 7;
        }
        else if(S.equals("010")){
            System.out.println("Error in check bit r2 (r2= "+c[1]+")");
            return 7;
        }
        else if(S.equals("011")){
            System.out.println("Error in information bit i3 (i3= "+c[5]+")");
            return 5;
        }
        else if(S.equals("100")){
            System.out.println("Error in check bit r1 (r1= "+c[0]+")");
            return 7;
        }
        else if(S.equals("101")){
            System.out.println("Error in information bit i2 (i2= "+c[4]+")");
            return 4;
        }
        else if(S.equals("110")){
            System.out.println("Error in information bit i1 (i1= "+c[2]+")");
            return 2;
        }
        else{
            System.out.println("Error in information bit i4 (i4= "+c[6]+")");
            return 6;
        }
    }
    public static void toCorrect (char[] c, int n){
        if(n==7){}
        else{
            if(c[n]=='1') c[n]='0';
            if(c[n]=='0') c[n]='1';
        }

    }
}