import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;

public class comboMenu {
    public static int total=0;
    public static String log="";
    public static void main(String[] args) {
        
        //would you like to order
        boolean looptrue=true;
        Scanner scanner = new Scanner(System.in);
        int i=0;

        while(looptrue){
            System.out.printf("Would you like to order? (y)es or (n)o? ");
            String choice=scanner.nextLine();
            i=i+1;

            while (!(choice.equals("y") || choice.equals("n"))){//loops until correct input givin
                System.out.println("Wrong input, (y)es or (n)o? ");
                choice=scanner.nextLine();   
            } if (choice.equals("y")) {
                logOrder(String.format("\norder %d", i));
                logOrder(Sandwich( 575, 525, 625));
                logOrder(item("Fry", 100, 175, 225));
                logOrder(item("Drink", 100, 150, 200));
                logOrder(ketchup());
                logOrder(String.format("Cost: %s",money(total)));
                logOrder(String.format("Tax:  %s", money(tax(total))));
                
            } else {looptrue=false;}
        }
        System.out.println(log);
        write(log);

    }

    public static String item(String food, int sp, int mp, int lp){
        String size="";
        int cost=0;
        String result="";

        Scanner scanner = new Scanner(System.in);
        System.out.printf("Would you like a %s? (y)es or (n)o? ", food);
        String choice=scanner.nextLine();

        while (!(choice.equals("y") || choice.equals("n"))){//loops until correct input givin
            System.out.println("Wrong input, (y)es or (n)o? ");
            choice=scanner.nextLine();   
        }

        if (choice.equals("y")){
            System.out.printf("What size?\n(s)mall  %s\n(m)edium %s\n(l)arge  %s\n? ",money(sp),money(mp),money(lp));
            choice=scanner.nextLine();
            while (!(choice.equals("s") || choice.equals("m") || choice.equals("l"))){ //loops until correct input givin
                System.out.println("Wrong input, (s)mall, (m)edium, or (l)arge? ");
                choice=scanner.nextLine();   
            }
            if (choice.equals("s")){
                total=total+sp;
                cost=sp;
                size="small";
            } else if (choice.equals("m")){
                total=total+mp;
                cost=mp;
                size="medium";
            } else{
                total=total+lp;
                cost=lp;
                size="large";
            }
            result=String.format("%s %s %s", food, size, money(cost));
            System.out.println(result);
        } else {result="Not Ordered";}
        return(result);
    }

    public static String Sandwich(int sp, int mp, int lp){
        String size="";
        int cost=0;
        String result="";

        Scanner scanner = new Scanner(System.in);
        System.out.printf("Would you like a Sandwich? (y)es or (n)o? ");
        String choice=scanner.nextLine();

        while (!(choice.equals("y") || choice.equals("n"))){//loops until correct input givin
            System.out.println("Wrong input, (y)es or (n)o? ");
            choice=scanner.nextLine();   
        }

        if (choice.equals("y")){
            System.out.printf("What size?\n(t)ofu  %s\n(c)hicken %s\n(b)eef  %s\n? ",money(sp),money(mp),money(lp));
            choice=scanner.nextLine();
            while (!(choice.equals("t") || choice.equals("c") || choice.equals("b"))){ //loops until correct input givin
                System.out.println("Wrong input, (t)ofu, (c)hicken, or (b)eef? ");
                choice=scanner.nextLine();   
            }
            if (choice.equals("t")){
                total=total+sp;
                cost=sp;
                size="tofu";
            } else if (choice.equals("c")){
                total=total+mp;
                cost=mp;
                size="chicken";
            } else{
                total=total+lp;
                cost=lp;
                size="beef";
            }
            result=String.format("Sandwich %s %s", size, money(cost));
            System.out.println(result);
        } else {result = "Not Ordered";}
        return(result);
    }

    public static int tax(int i) {
        i=i+((i*7)/100);
        return(i);
    }

    public static String ketchup(){
        int count=0;
        Scanner scanner = new Scanner(System.in);
        System.out.println("How many ketchup packets? ");
        count=scanner.nextInt();
        total=total+(count*25);
        return(String.format("%d ketchup packets", count));
    }

    public static String money(int i){
        String moneyStr=Integer.toString(i);
        if(moneyStr.length()<3){moneyStr="0"+moneyStr;}
        int len=moneyStr.length();
        String moneyDec=moneyStr.substring((len-2),(len));
        String moneyNum=moneyStr.substring(0,(len-2));
        return(String.format("$%s.%s",moneyNum, moneyDec));
    }

    public static void logOrder(String entry){
        log=log+entry+"\n";
    }

    public static void write(String input) {
        try {
            FileWriter myWriter = new FileWriter("order.txt");
            myWriter.write(input);
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

}