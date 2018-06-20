package blockchain_demo;
public class Threaded_People extends Thread{

    People people;

    public Threaded_People(Exchange exchange){
        this.people = new People(exchange);
    }

    public void run(){
        this.people.start_generating_transactions();
    }

}
