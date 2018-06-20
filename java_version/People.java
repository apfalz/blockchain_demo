package blockchain_demo;
import java.util.*;

public class People{
    public  Map<String, Person> people = new HashMap<String, Person>();
    public  Exchange            exchange;
    public  String              names[] = {"Alice", "Bob", "Carly", "Dave", "Emma", "Frank", "Gwen", "Henry", "Iggy", "James", "Karen", "Larry"};
    public  int                 verbose;
    public Random               rand;

    public People(Exchange exchange){
        this.rand     = new Random();
        this.exchange = exchange;
        this.verbose  = 2;
        System.out.println("this.names.length: " + "" + this.names.length);
        for (int i=0; i < this.names.length;i++){

            this.people.put(this.names[i], new Person(this.rand.nextInt(20), i,this.names[i]));
        }

    }
    public void start_generating_transactions(){
        for (int i = 0;i<200;i++){
            Person sender    = this.people.get(this.names[this.rand.nextInt(this.names.length)]);
            Person recipient = this.people.get(this.names[this.rand.nextInt(this.names.length)]);//for now allow sending coin to yourself
            int    amount    = this.rand.nextInt(20);
            String possessed = "/" + ("" + sender.coin_possessed);
            Trade trade      = new Trade(sender, recipient, amount);
            if (this.verbose >= 2){
                System.out.println(sender.name + " wants to send " + ("" + amount) + possessed + " to " + recipient.name);
            }
            this.exchange.receive_request(trade);
            //delay
            try{
                Thread.sleep(this.rand.nextInt(20)*1000);
            }catch(Exception e){
                System.out.println(e);
            }
        }
    }
    // public static void main(String args[])  throws InterruptedException{
    //     Network  net      = new Network();
    //     Exchange exchange = new Exchange("exchange", net);
    //     People people = new People(exchange);
    //     people.start_generating_transactions();
    // }

}
